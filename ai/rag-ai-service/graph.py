"""LangGraph RAG 그래프: retrieve → grade → generate | rewrite↺ | abstain → format"""
import operator  # 리스트를 합치는 operator.add 사용
from typing import Annotated, TypedDict  # 상태 필드에 추가 동작 지정, 그래프의 상태 데이터 구조 정의
from langgraph.graph import END, START, StateGraph  # LangGraph의 상태 기반 그래프 생성
from engine import ABSTAIN_MESSAGE, Chunk, body_of  # 검색 근거가 없을 때 사용할 메시지
from settings import Settings

# 그래프에서 공유하는 상태
# TypedDict: 딕셔너리 구조에 자료형 구조를 지정
class RagState(TypedDict, total=False):
    question: str   # 사용자가 입력한 원래 질문을 보존
    query: str      # 검색에 사용할 문장으로, 재검색 과정에서 변경될 수 있음
    board_ids: list[int]   # Spring이 보낸 READY 허용목록
    top_k: int
    chunks: list[Chunk]
    attempts: int    # rewrite 횟수
    answer: str
    abstained: bool
    sources: list[dict]
    trace: Annotated[list[str], operator.add]

# 그래프를 생성하는 함수: engine (StubEngine / AtlasEngine), settings: 환경 설정 객체
def build_graph(engine, settings: Settings):  # 타입 힌트
    # 검색
    def retrieve(state: RagState) -> dict:
        ids = state.get("board_ids") or []
        chunks = engine.search(state["query"], ids, state.get("top_k", 4)) if ids else []
        return {"chunks": chunks, "trace": ["retrieve"]}

    # 검색 결과 평가
    def grade(state: RagState) -> dict:
        kept = [c for c in state["chunks"] if c.score >= engine.min_score]
        return {"chunks": kept, "trace": ["grade"]}

    # 조건에 따른 분기
    def route_after_grade(state: RagState) -> str:
        if state["chunks"]:
            return "generate"
        if state.get("board_ids") and state.get("attempts", 0) < settings.max_rewrites:
            return "rewrite"
        return "abstain"

    # 질문 재작성
    def rewrite(state: RagState) -> dict:
        return {
            "query": engine.rewrite(state["question"]),
            "attempts": state.get("attempts", 0) + 1,
            "trace": ["rewrite"],
        }

    # 답변 생성
    def generate(state: RagState) -> dict:
        return {"answer": engine.generate(state["question"], state["chunks"]),
                "abstained": False, "trace": ["generate"]}

    # 답변 보류
    def abstain(state: RagState) -> dict:
        return {"answer": ABSTAIN_MESSAGE, "abstained": True, "chunks": [], "trace": ["abstain"]}

    # 출처 정리
    def format_(state: RagState) -> dict:
        # 같은 글의 여러 청크는 점수가 가장 높은 것 하나만 출처로 보여 줌
        best: dict[int, Chunk] = {}
        for c in state.get("chunks", []):
            if c.board_id not in best or c.score > best[c.board_id].score:
                best[c.board_id] = c
        sources = [
            {"board_id": c.board_id, "title": c.title, "author": c.author,
            "snippet": body_of(c.text)[:120], "score": c.score}
            for c in sorted(best.values(), key=lambda c: c.score, reverse=True)
        ]
        return {"sources": sources, "trace": ["format"]}

    # 노드와 간선 연결
    g = StateGraph(RagState)
    # 노드 등록
    g.add_node("retrieve", retrieve)
    g.add_node("grade", grade)
    g.add_node("rewrite", rewrite)
    g.add_node("generate", generate)
    g.add_node("abstain", abstain)
    g.add_node("format", format_)

    # 일반 간선  연결
    g.add_edge(START, "retrieve")
    g.add_edge("retrieve", "grade")

    # 조건부 간선 연결
    g.add_conditional_edges(
        "grade",
        route_after_grade,
        {
            "generate" : "generate",
            "rewrite" : "rewrite",
            "abstain" : "abstain",
        }
    )

    g.add_edge("rewrite", "retrieve")
    g.add_edge("generate", "format")
    g.add_edge("abstain", "format")
    g.add_edge("format", END)
    return g.compile() # 정의한 그래프를 실행 가능한 형태로 컴파일 후 반환

# 그래프 실행
def run_graph(graph, question: str, board_ids: list[int], top_k: int) -> dict:
    # 초기 상태를 전달 받아 그래프를 실행하고, 최종 상태를 반환
    return graph.invoke({
        "question" : question,
        "query" : question,
        "board_ids" : board_ids,
        "top_k" : top_k,
        "attempts" : 0,
        "trace" : []
    })