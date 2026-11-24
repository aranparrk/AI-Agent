import re
from dataclasses import dataclass
from langchain_core.output_parsers import StrOutputParser  # LLM이 반환한 메시지 객체에서 답변 텍스트만 추출
from langchain_core.prompts import ChatPromptTemplate      # LLM에게 전달할 질문과 지시문을 정해진 형식으로 구성
from langchain_text_splitters import RecursiveCharacterTextSplitter
from settings import Settings

@dataclass
class Chunk:
    board_id: int
    title: str
    author: str
    text: str
    score: float = 0.0

# ───────────────────────── 공통 도우미 ─────────────────────────
def make_splitter(settings: Settings) -> RecursiveCharacterTextSplitter:
    # \n\n → \n → ". " → 공백 순서로 자연스러운 경계를 찾아 자름
    return RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )


def chunk_texts(splitter: RecursiveCharacterTextSplitter, title: str, content: str) -> list[str]:
    """청크마다 제목을 붙여 둡니다. 본문만 있는 청크도 어떤 글인지 검색될 수 있게 하기 위함."""
    pieces = splitter.split_text(content) if content.strip() else []
    if not pieces:
        pieces = [""]
    return [f"제목: {title}\n{p}".strip() for p in pieces]


def body_of(text: str) -> str:
    """청크 앞의 '제목:' 줄을 뗀 본문 (출처 미리보기용)."""
    lines = text.split("\n", 1)
    return lines[1].strip() if len(lines) > 1 and lines[0].startswith("제목:") else text.strip()


def format_context(chunks: list[Chunk]) -> str:
    """프롬프트에 넣을 근거 목록. LLM 이 [#글번호]로 인용할 수 있게 번호를 붙임."""
    return "\n\n".join(f"[#{c.board_id}] {c.title} (작성자: {c.author})\n{body_of(c.text)}" for c in chunks)


def bigrams(text: str) -> set[str]:
    """글자 2개 묶음. 공백·기호는 빼고 소문자로."""
    s = re.sub(r"[^0-9a-zA-Z가-힣]", "", text.lower())
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) > 1 else ({s} if s else set())


# 질문에서 검색에 도움이 안 되는 말 (스텁 재작성용)
_STOP = ["하나요", "인가요", "있나요", "되나요", "할까요", "어때", "알려줘", "알려 줘", "궁금해", "뭐야", "언제", "어디", "어떻게", "무엇", "?", "？"]

ANSWER_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "너는 커뮤니티 게시판 도우미다. 아래 [게시글]에 있는 내용만 근거로 한국어로 짧게 답한다.\n"
     "- 게시글에 없는 내용은 추측하지 말고 '게시판에서 찾지 못했습니다'라고 답한다.\n"
     "- 근거로 쓴 문장 끝에 [#글번호]를 붙인다. 예: 매주 목요일에 모입니다 [#1]\n"
     "- 3문장 이내로 답한다."),
    ("human", "[게시글]\n{context}\n\n[질문]\n{question}"),
])

REWRITE_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "사용자 질문을 게시판 검색에 알맞은 짧은 검색 문장으로 바꾼다. "
     "핵심 명사와 키워드만 남기고 한 줄로만 출력한다."),
    ("human", "{question}"),
])

ABSTAIN_MESSAGE = "게시판에서 관련 내용을 찾지 못했습니다. 질문을 바꾸거나 관련 글을 먼저 올려 주세요."


# ───────────────────────── 스텁 엔진 (1~5차시) ─────────────────────────
class StubEngine:
    """OpenAI·Atlas 없이 동작하는 대역. 2-gram 겹침 비율로 점수를 내고, 메모리에 저장합니다."""

    name = "stub"

    def __init__(self, settings: Settings):
        self.splitter = make_splitter(settings)
        self.min_score = settings.stub_min_score
        self.store: dict[int, list[Chunk]] = {}     # board_id → 청크들 (재시작하면 사라짐)

    def index(self, board_id, title, content, author, email):
        texts = chunk_texts(self.splitter, title, content)
        self.store[board_id] = [Chunk(board_id, title, author, t) for t in texts]   # 수정 시 통째로 교체
        return len(texts)

    def delete(self, board_id):
        return len(self.store.pop(board_id, []))

    def search(self, query, board_ids, k):
        q = bigrams(query)
        if not q:
            return []
        allowed = set(board_ids)
        scored = []
        for bid, chunks in self.store.items():
            if bid not in allowed:          # 허용목록 밖은 아예 보지 않음
                continue
            for c in chunks:
                score = len(q & bigrams(c.text)) / len(q)
                scored.append(Chunk(c.board_id, c.title, c.author, c.text, round(score, 3)))
        scored.sort(key=lambda c: c.score, reverse=True)
        return scored[:k]

    def generate(self, question, chunks):
        best = chunks[0]
        body = body_of(best.text).replace("\n", " ")[:150]
        return f"'{best.title}' 글에 따르면: {body} [#{best.board_id}]"

    def rewrite(self, question):
        q = question
        for w in _STOP:
            q = q.replace(w, " ")
        return " ".join(q.split()) or question

# Atlas 엔진
class AtlasEngine:
    """OpenAI 임베딩 + MongoDB Atlas Vector Search + ChatOpenAI."""
    name = "atlas"

    def __init__(self, settings: Settings):  # DB, 임베딩, LLM 초기화
        from langchain_mongodb import MongoDBAtlasVectorSearch
        from langchain_openai import ChatOpenAI, OpenAIEmbeddings
        from pymongo import MongoClient

        if not settings.openai_api_key or not settings.mongodb_uri:
            raise RuntimeError("RAG_ENGINE=atlas 에는 OPENAI_API_KEY 와 MONGODB_URI 가 필요합니다.")

        self.splitter = make_splitter(settings)
        self.min_score = settings.min_score
        self.client = MongoClient(settings.mongodb_uri, serverSelectionTimeoutMS=5000)
        self.collection = self.client[settings.mongodb_db][settings.mongodb_collection]

        # OpenAIEmbeddings 객체 생성, 내부 지역 변수 임
        embeddings = OpenAIEmbeddings(
            model=settings.openai_embedding_model,
            dimensions=settings.embedding_dimensions,
            api_key=settings.openai_api_key
        )

        # MongoDBAtlasVectorSearch 객체 생성
        self.store = MongoDBAtlasVectorSearch(
            collection=self.collection,             # MongoDB 컬렉션
            embedding=embeddings,                   # 임베딩 객체
            index_name=settings.atlas_index_name,   # Atlas 벡터 검색 인덱스 이름
            text_key="text",                        # 원본 텍스트를 저장할 필드명
            embedding_key="embedding",              # 임베딩 벡터를 저장할 필드명
            relevance_score_fn="cosine"             # 유사도 계산 방식
        )
        llm = ChatOpenAI(model=settings.openai_chat_model, temperature=0, api_key=settings.openai_api_key)
        # LangChain Runnable 체인: 프롬프트 → 모델 → 문자열 파서
        self.answer_chain = ANSWER_PROMPT | llm | StrOutputParser()      # 질문과 검색된 자료를 이용해 답변을 생성하는 체인
        self.rewrite_chain = REWRITE_PROMPT | llm | StrOutputParser()    # 질문을 LLM을 이용해 다시 작성하는 체인

    def index(self, board_id, title, content, author, email):
        self.collection.delete_many({"boardId": board_id})  # 수정 시 이전 청크 교체
        texts = chunk_texts(self.splitter, title, content)
        metadatas = [
            {"boardId": board_id, "title": title, "author": author, "owner": email, "chunkNo": i}
            for i in range(len(texts))
        ]
        self.store.add_texts(texts, metadatas=metadatas)
        return len(texts)

    def delete(self, board_id):
        return self.collection.delete_many({"boardId": board_id}).deleted_count

    def search(self, query, board_ids, k):
        if not board_ids:
            return []
        results = self.store.similarity_search_with_score(
            query, k=k, pre_filter={"boardId": {"$in": board_ids}},  # 허용목록 필터 (filter 필드)
        )
        return [
            Chunk(
                board_id=int(doc.metadata["boardId"]),
                title=doc.metadata.get("title", ""),
                author=doc.metadata.get("author", ""),
                text=doc.page_content,
                score=round(float(score), 3),
            )
            for doc, score in results
        ]

    def generate(self, question, chunks):
        return self.answer_chain.invoke({"question": question, "context": format_context(chunks)})

    def rewrite(self, question):
        return self.rewrite_chain.invoke({"question": question}).strip() or question

def create_engine(settings: Settings):
    if settings.rag_engine == "atlas":
        return AtlasEngine(settings)
    return StubEngine(settings)
