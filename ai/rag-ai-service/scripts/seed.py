"""시연용 데이터: 회원 2명(강사·학생)과 게시글을 Spring API 로 넣습니다.

Spring(:8111)과 FastAPI(:8000)를 모두 켠 뒤:  python scripts/seed.py
글을 쓰면 Spring 이 커밋 후 자동으로 색인을 요청합니다(5차시 이후).
"""
import json
import urllib.error
import urllib.request

SPRING = "http://localhost:8111"

USERS = [
    {"email": "teacher@test.com", "pwd": "1234", "name": "강사"},
    {"email": "student@test.com", "pwd": "1234", "name": "학생"},
]

POSTS = {
    "teacher@test.com": [
        ("스터디 모임 공지", "매주 목요일 저녁 7시, 302호에서 스터디 모임을 합니다. 노트북을 꼭 챙겨 오세요."),
        ("과제 제출 안내", "미니 프로젝트 과제 마감은 11월 26일 자정입니다. 깃허브 저장소 주소를 게시판에 댓글로 남겨 주세요."),
        ("LazyInitializationException 해결", "트랜잭션이 끝난 뒤 지연 로딩(LAZY) 연관 엔티티에 접근하면 LazyInitializationException 이 납니다. "
                                              "필요한 연관 엔티티를 join fetch 로 함께 조회하거나, 서비스 계층에서 DTO 로 바꿔서 반환하세요."),
        ("JWT 401 오류가 계속 날 때", "Access Token 이 만료되면 401 이 납니다. 프론트의 응답 인터셉터가 /auth/reissue 로 재발급한 뒤 "
                                    "원래 요청을 다시 보내는지 개발자 도구 Network 탭에서 확인하세요."),
        ("카카오 로그인 KOE006", "KOE006 은 리다이렉트 URI 불일치입니다. 카카오 콘솔, .env.local, application.properties 세 곳의 주소가 "
                               "글자 하나까지 같아야 합니다."),
        ("발표 준비 안내", "최종 발표는 11월 27일입니다. 시연 영상을 미리 녹화해 두고, 발표 전날 시드 데이터와 재색인을 확인하세요."),
    ],
    "student@test.com": [
        ("점심 맛집 추천", "학교 앞 김치찌개 집이 가성비가 좋아요. 점심시간에는 12시 전에 가야 자리가 있습니다."),
        ("Gradle 빌드가 안 될 때", "gradlew 권한 오류가 나면 chmod +x gradlew 를 실행하고, IntelliJ 에서 Gradle JVM 을 Java 21 로 맞추세요."),
        ("conda 환경에서 모듈을 못 찾을 때", "PyCharm 인터프리터와 터미널이 모두 rag-ai 환경인지 확인하세요. base 에 설치하면 안 됩니다."),
        ("내 프로젝트 진행 상황", "게시판 AI 도우미에 댓글 색인 기능을 추가하는 중입니다. 다음 주에 채팅방 @AI 기능도 붙일 예정입니다."),
    ],
}


def call(method, path, body=None, token=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(SPRING + path, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req) as res:
            text = res.read().decode()
            return json.loads(text) if text else None
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} 실패: {e.code} {e.read().decode()}")


def main():
    for u in USERS:
        call("POST", "/auth/signup", u)                          # 이미 있으면 false 를 돌려줌 (무시)
        token = call("POST", "/auth/login", {"email": u["email"], "pwd": u["pwd"]})["accessToken"]
        for title, content in POSTS[u["email"]]:
            ok = call("POST", "/board/write", {"title": title, "content": content}, token)
            print(("✔" if ok else "✘"), u["name"], "-", title)
    print("완료: 게시판 목록에서 배지가 '검색 가능'이 되는지 확인하세요.")


if __name__ == "__main__":
    main()