"""RAG 그래프 테스트 (stub 엔진 — OpenAI·Atlas 없이 실행)
실행: 프로젝트 루트에서  pytest -v
"""
import os

os.environ.setdefault("SERVICE_TOKEN", "test-token")
os.environ["RAG_ENGINE"] = "stub"

import pytest
from fastapi.testclient import TestClient

from app import app
from engine import ABSTAIN_MESSAGE, StubEngine
from graph import build_graph, run_graph
from settings import Settings

HEADERS = {"X-Service-Token": os.environ["SERVICE_TOKEN"]}


# ───────── 1. 그래프 단위 테스트 (FastAPI 없이 그래프만) ─────────
@pytest.fixture
def graph_and_engine():
    settings = Settings()
    engine = StubEngine(settings)
    engine.index(1, "스터디 모임 안내", "파이썬 스터디는 매주 목요일 저녁 7시에 모입니다.", "홍길동", "a@a.com")
    engine.index(2, "주차 안내", "건물 지하 2층에 주차할 수 있습니다.", "김철수", "b@b.com")
    return build_graph(engine, settings), engine


def test_generate_path(graph_and_engine):
    """관련 글이 있으면 retrieve → grade → generate → format"""
    graph, _ = graph_and_engine
    r = run_graph(graph, "파이썬 스터디 언제 모여?", [1, 2], 4)
    assert r["abstained"] is False
    assert r["trace"] == ["retrieve", "grade", "generate", "format"]
    assert r["sources"][0]["board_id"] == 1


def test_rewrite_then_abstain(graph_and_engine):
    """관련 글이 없으면 rewrite 루프를 돈 뒤 abstain"""
    graph, _ = graph_and_engine
    r = run_graph(graph, "점심 메뉴 추천해줘", [1, 2], 4)
    assert r["abstained"] is True
    assert r["answer"] == ABSTAIN_MESSAGE
    assert "rewrite" in r["trace"]
    assert r["trace"][-2:] == ["abstain", "format"]
    assert r["sources"] == []


def test_empty_allowlist_abstains_immediately(graph_and_engine):
    """허용목록이 비면 검색도 재작성도 하지 않고 바로 abstain"""
    graph, _ = graph_and_engine
    r = run_graph(graph, "파이썬 스터디 언제 모여?", [], 4)
    assert r["abstained"] is True
    assert r["trace"] == ["retrieve", "grade", "abstain", "format"]


def test_allowlist_is_respected(graph_and_engine):
    """허용목록 밖의 글(1번)은 출처로 나오면 안 됨"""
    graph, _ = graph_and_engine
    r = run_graph(graph, "파이썬 스터디 언제 모여?", [2], 4)
    assert all(s["board_id"] != 1 for s in r["sources"])


# ───────── 2. API 통합 테스트 (Spring 이 부르는 그대로) ─────────
@pytest.fixture
def client():
    with TestClient(app) as c:   # with 를 써야 lifespan(엔진·그래프 생성)이 실행됨
        yield c


def test_token_required(client):
    r = client.post("/query", json={"question": "안녕", "boardIds": [1]})
    assert r.status_code == 401


def test_index_and_query_api(client):
    r = client.post("/index", headers=HEADERS, json={
        "boardId": 10, "title": "MT 공지", "content": "MT는 12월 5일 가평으로 갑니다.",
        "author": "운영진", "email": "admin@a.com"})
    assert r.status_code == 200 and r.json()["chunks"] >= 1

    r = client.post("/query", headers=HEADERS,
                    json={"question": "MT 어디로 가?", "boardIds": [10], "topK": 4})
    body = r.json()
    assert r.status_code == 200
    assert body["abstained"] is False
    assert body["sources"][0]["boardId"] == 10      # 응답이 camelCase 인지도 확인
    print("\ntrace:", body["trace"], "\nanswer:", body["answer"])

    r = client.delete("/index/10", headers=HEADERS)
    assert r.json()["deleted"] >= 1