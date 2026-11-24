import math  # 수학 관련 라이브러리

# 코사인 유사도 계산, 두 벡터가 얼마나 같은 방향인가?
def cosine(a: list[float], b: list[float]) ->float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)  # 길이로 나눠 방향만 비교

# 유사도가 높은 k개 반환
def top_k(query: list[float], docs: dict[str, list[float]], k: int) -> list[tuple[str, float]]:
    scored = [(title, round(cosine(query, vec), 3)) for title, vec in docs.items()]
    scored.sort(key=lambda t: t[1], reverse=True)
    return scored[:k]


if __name__ == "__main__":   # 진입 지점
    # 차원 의미: [스터디, 모임, 음식]
    docs = {
        "스터디 모임 공지": [1, 1, 0],
        "점심 맛집 추천": [0, 0, 1],
        "오늘의 날씨": [0, 0, 0],
    }
    question1 = [1, 0, 0]          # "스터디 언제 해요?"
    question2 = [0, 1, 1]          # "맛집 모임 언제 해요?"
    for title, score in top_k(question2, docs, 3):
        print(f"{score:.3f}  {title}")