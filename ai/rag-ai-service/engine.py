# RAG 엔진을 대신하는 임시 클래스
class StubEngine:
    name = "stub"
    min_score = 0.0

    def __init__(self, settings): # 생성자
        self.store = {}

    # 게시글 저장
    def index(self, board_id, title, content, author, email):
        self.store[board_id] = [content]
        return 1

    # 게시글 삭제
    def delete(self, board_id):
        return len(self.store.pop(board_id, []))

# 엔진 생성 함수
def create_engine(settings):
    return StubEngine(settings)
