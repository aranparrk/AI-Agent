from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

# Spring Boot(Java) 백엔드와 Python(FastAPI + LangGraph) AI 서비스 간의
# 통신 규약(API Contract)을 정의한 Pydantic v2 데이터 전송 객체(DTO)

class CamelModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# Spring Boot에서 게시글이 등록되거나 수정되어 RAG 검색 대상이 되었을 때 Python으로 전달
class IndexRequest(CamelModel):
    board_id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(default="", max_length=20_000) # 20000과 동일, 큰 숫자를 쉽게 확인하는 용도
    author: str = Field(default="", max_length=100)
    email: str = Field(default="", max_length=150)

# 생성된 청크 수 반환
class IndexResponse(CamelModel):
    board_id: int
    chunks: int

# 게시글 수정, 삭제 시 기존 벡터 청크 제거 건수 반환
class DeleteResponse(CamelModel):
    board_id: int
    deleted: int

# 사용자 질문 및 MySQL 기반 검색 허용 목록
class QueryResquest(CamelModel):
    question: str = Field(min_length=1, max_length=500)
    # Spring이 MySQL에서 만든 READY 허용목록, 비어 있으면 검색하지 않고 abstain
    board_ids: list[int] = Field(default_factory=list, max_length=10_000)
    top_k: int = Field(default=4, ge=1, le=10)

# LLM이 답변을 생서할 때 실제로 참조한 청크 단위 출처 정보
class Source(CamelModel):
    board_id: int
    title: str
    author: str = ""
    snippet: str
    score: float

# 생성 답변, 답변 거절 여부 등
class QueryResponse(CamelModel):
    answer: str
    abstained: bool
    sources: list[Source]
    trace: list[str] # LangGraph가 실제로 지나간 노드 순서
