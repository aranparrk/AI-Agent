from fastapi import FastAPI

# 프로그램의 메인 역할을 함
# 1. 서버 초기화: 설정, RAG엔진, LangGraph를 최초 생성
# 2. 서비스 인증: Spring Boot가 전달하는 서비스 트큰 검증
# 3. 게시글 색인: /index로 전달받은 게시글 저장
# 4. 게시글 삭제: /index/{board_id}로 색인 데이터 삭제
# 5. AI 질의: /query로 전달받은 질문 처리

import logging  # 서버 실행 정보 및 오류 기록
import secrets  # 서버 토큰 안정 비교
from contextlib import asynccontextmanager  # 서버 시작 및 종료 시 작업 관리
# Depends: API 요청 전에 인증 함수 실행, Request: 현재 요청 및 앱 상태 접근
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.concurrency import run_in_threadpool  # 동기 함수를 별도 스레드 풀에서 실행

from engine import create_engine
from graph import build_graph, run_graph
from schemas import DeleteResponse, IndexResponse, IndexRequest, QueryResponse, QueryRequest
from settings import Settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s - %(message)s")
log = logging.getLogger("rag")

@asynccontextmanager  # 서버의 시작과 종료 시점을 구부하여 초기화 및 정리 작업을 수행
async def lifespan(app: FastAPI):
    # 서버 시작 시 한 번: 설정 → 엔진 → 그래프 (요청마다 만들지 않음)
    settings = Settings()
    engine = create_engine(settings)
    app.state.settings = settings
    app.state.engine = engine
    app.state.graph = build_graph(engine, settings)
    log.info("RAG 엔진 준비 완료: %s", engine.name)
    yield
    client = getattr(engine, "client", None)      # Atlas 엔진이면 MongoClient 정리
    if client is not None:
        client.close()

app = FastAPI(title="Board RAG AI Service", lifespan=lifespan)

# 외부에서 전달된 서비스 토큰이 서버에 설정된 토큰과 같은지 확인
def verify_token(request: Request, x_service_token: str = Header(default="")) -> None:
    expected = request.app.state.settings.service_token
    if not secrets.compare_digest(x_service_token, expected):
        raise HTTPException(status_code=401, detail="서비스 토큰이 올바르지 않습니다.")


@app.get("/health")
def health():
    return {"status": "OK"}

# 게시글 등록 및 수정 시 Spring Boot가 호출하는 API
@app.post("/index", response_model=IndexResponse, dependencies=[Depends(verify_token)])
async def index(req: IndexRequest, request: Request):
    engine = request.app.state.engine
    try:
        n = await run_in_threadpool(engine.index, req.board_id, req.title, req.content, req.author, req.email)
    except Exception as e:
        log.exception("색인 실패")
        raise HTTPException(status_code=502, detail=f"색인 실패: {type(e).__name__}") from e
    return IndexResponse(board_id=req.board_id, chunks=n)

# 게시글 삭제 시 호출
@app.delete("/index/{board_id}", response_model=DeleteResponse, dependencies=[Depends(verify_token)])
async def delete(board_id: int, request: Request):
    engine = request.app.state.engine
    try:
        n = await run_in_threadpool(engine.delete, board_id)
    except Exception as e:
        log.exception("삭제 실패")
        raise HTTPException(status_code=502, detail=f"삭제 실패: {type(e).__name__}") from e
    return DeleteResponse(board_id=board_id, deleted=n)

# AI 질문 처리 API
@app.post("/query", response_model=QueryResponse, dependencies=[Depends(verify_token)])
async def query(req: QueryRequest, request: Request):
    graph = request.app.state.graph
    try:
        result = await run_in_threadpool(run_graph, graph, req.question, req.board_ids, req.top_k)
    except Exception as e:
        log.exception("질의 실패")
        raise HTTPException(status_code=502, detail=f"질의 실패: {type(e).__name__}") from e
    return QueryResponse(
        answer=result["answer"],
        abstained=result["abstained"],
        sources=result.get("sources", []),
        trace=result["trace"],
    )