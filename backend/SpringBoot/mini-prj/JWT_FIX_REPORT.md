# JWT 적용 오류 분석 및 수정 결과

검증일: 2026-11-09 (한국 시간)

## 프로젝트 구조
- Java 21, Spring Boot 4.0.8, Spring Security, JJWT 0.13.0, Gradle.
- Controller → Service → Repository → JPA Entity 구조.
- AuthController: 회원가입, 이메일 중복 확인, 로그인.
- MemberController: 회원 조회/수정/탈퇴, 회원별 게시글·댓글 목록.
- BoardController / CommentController: 게시글·댓글 CRUD, 검색·페이징, 좋아요.
- 기존 Member 식별자: id, email, pwd. Board 시간 필드: regDate.
- TokenDto: grantType, accessToken, accessTokenExpriesIn. 기존 응답 필드의 철자도 유지했다.

## 수정 전 실제 컴파일 오류 (5건)
1. BoardController는 searchBoard(int, int, String, String)을 호출하지만 복사된 Service는 searchBoard(String, int, int)만 제공했다.
2. BoardRepository에는 findAllByOrderByRegDateDesc()가 있는데 Service가 findAllByOrderByRegTimeDesc()를 호출했다.
3. Board에는 regDate가 있는데 Service가 getRegTime()을 호출했다.
4. MemberController가 호출하는 BoardService.getMyBoardPage()가 누락되었다.
5. MemberController가 호출하는 CommentService.getMyCommentPage()가 누락되었다.

추가 실행 오류: 정렬 필드 regTime/rgeTime은 실제 Entity에 없다.

## 수정한 운영 코드
| 파일 | 수정 이유 |
| --- | --- |
| src/main/java/com/human/mini_prj/service/BoardService.java | 기존 regDate/Repository 메서드로 연결. 기존 검색 인자·검색 유형 및 getMyBoardPage 복원. 기존 조회수 증가, DTO의 조회수·좋아요 수·댓글 수, 게시글 삭제 시 댓글·좋아요 정리 복원. JWT 작성자 확인 유지. |
| src/main/java/com/human/mini_prj/service/CommentService.java | 기존 Controller가 사용하는 getMyCommentPage 연결 메서드 추가. 댓글 삭제에도 기존 checkWriter 적용. 현재 getMemberCommentPage도 유지. |
| src/main/java/com/human/mini_prj/service/AuthService.java | 회원가입 시 기존 PasswordEncoder로 pwd를 암호화하여 로그인 BCrypt 비교와 일치시킴. |
| src/main/java/com/human/mini_prj/service/BoardLikeService.java | 기존 boardId/email 인자와 응답 DTO를 유지하면서 요청 email이 토큰 사용자와 일치하는지 검증. 불일치 시 기존 ErrorResponse 구조로 403 반환. |
| src/main/java/com/human/mini_prj/exception/GlobalExceptionHandler.java | 기존 CustomException의 지정 상태(로그인 실패 401, 좋아요 권한 오류 403)를 반영. 상태 미지정 예외는 기존 400 유지. 응답 필드 구조 유지. |
| src/main/java/com/human/mini_prj/security/TokenProvider.java | 서명·만료 검증에 추가로 sub, exp, auth 필수값과 기존 Authority 열거형 값을 확인. 누락·잘못된 타입의 claim으로 인한 인증 생성 오류 방지. |
| src/main/java/com/human/mini_prj/security/JwtFilter.java | 검증 후 Authentication 생성 직전에 토큰이 만료되는 경우도 인증 실패로 처리. 기존 Bearer 방식 및 공개 경로 처리 유지. |
| src/main/java/com/human/mini_prj/security/SecurityUtil.java | 인증되지 않은 Authentication도 로그인 사용자로 취급하지 않도록 확인. |
| src/main/java/com/human/mini_prj/config/SecurityConfig.java | 기존 Controller에서 허용한 localhost:3001을 전역 CORS 허용 목록에도 추가. 기존 3000/5173 유지. |

Entity, DTO, Repository, Controller는 이번 작업에서 변경하지 않았다.
application.properties, DB_PASSWORD 및 JWT_SECRET 환경 변수 설정도 변경하지 않았다.
작업 시작 전에 존재하던 사용자 변경은 보존했다.

## 인증·인가 흐름
1. /auth/signup → AuthService → BCrypt 해시를 Member.pwd에 저장.
2. /auth/login → findByEmail → PasswordEncoder.matches → TokenProvider.createToken.
3. 토큰 sub=email, auth=기존 Authority 이름, exp=만료 시각.
4. Authorization: Bearer 토큰 → JwtFilter → 검증 → Authentication → SecurityContext.
5. 기존 SecurityFilterChain이 공개 경로와 인증 필요 경로를 구분.
6. 기존 Service의 SecurityUtil.currentEmail()로 작성자·수정자·탈퇴자 확인.
7. 세션을 생성하지 않고 각 요청에서 토큰을 검증한다.

역할 이름은 Authentication authorities로 복원된다. 현재 프로젝트의 접근 규칙은 authenticated() 기반이며 새 관리자 전용 경로는 임의로 추가하지 않았다.

## 테스트 관련 변경
- build.gradle: 테스트 실행 전용 H2 의존성 추가.
- src/test/resources/application-test.properties: 별도 H2 메모리 DB와 실행 시 생성되는 테스트 JWT 키 사용. 운영 키 하드코딩 없음.
- 기존 MiniPrjApplicationTests, ItemRepositoryTest: test 프로필 지정. 기존 테스트와 상품 기능 유지.
- TokenProviderTest 신규: 정상/만료/변조/다른 서명 키/형식 오류/필수 claim 누락·타입 오류 검증.
- JwtSecurityIntegrationTest 신규: 실제 Spring 컨텍스트·Security 필터·Controller·Service·Repository를 연결한 MockMvc 통합 테스트 4개.
  - 회원가입 → BCrypt 저장 → 로그인 → 토큰 응답 필드·권한 → 보호 API 접근, 세션 미생성, 잘못된 로그인 401.
  - 공개 API·Swagger 접근, 인증 없는 쓰기 차단, 잘못된 토큰 차단, CORS 사전 요청.
  - 게시글·댓글 생성, 타인 수정·삭제 차단, 좋아요 타인 사칭 차단, 조회수·집계·검색·회원별 목록, 작성자 게시글 삭제 및 연관 데이터 삭제.
  - 토큰 사용자 회원 정보 수정, 타인 탈퇴 차단, 본인 탈퇴.

## 실제 실행 결과
- 수정 전 ./gradlew compileJava --offline: 컴파일 오류 5건 재현.
- 수정 후 ./gradlew compileJava --offline: 성공.
- ./gradlew clean build: 성공.
- 최종 추가 검증 반영 후 ./gradlew build: BUILD SUCCESSFUL.
- 최종 테스트: 20개 실행, 실패 0, 오류 0, 건너뜀 0.
  - MiniPrjApplicationTests: 1
  - ItemRepositoryTest: 14
  - JwtSecurityIntegrationTest: 4
  - TokenProviderTest: 1
- git diff --check: 통과.
- HTML 테스트 결과: build/reports/tests/test/index.html
- 실행 JAR: build/libs/mini-prj-0.0.1-SNAPSHOT.jar

## 검증 범위와 남은 사항
- 테스트는 H2 메모리 DB에서 실행했다. 실제 운영 MySQL 연결 및 브라우저 프런트엔드 연동은 실행하지 않았다.
- 기존 평문 비밀번호는 BCrypt 비교와 호환되지 않는다. 기존 계정 데이터는 변경하지 않았으며 해당 계정에는 별도 재설정/변환이 필요하다. 새 회원가입 → 로그인은 검증했다.
- 기존 application.properties의 ddl-auto=create를 유지했다. 이번 검증에서는 운영 DB로 애플리케이션을 실행하지 않았다.
- 현재 방식은 기존과 동일한 stateless 토큰 인증이다. 회원 삭제·비밀번호 변경 시 이미 발급된 토큰을 즉시 폐기하는 기능은 추가하지 않았다.

## 참고한 공식 자료
- JJWT API/사용법: https://github.com/jwtk/jjwt
- Spring Security MockMvc 연동: https://docs.spring.io/spring-security/reference/7.2/servlet/test/mockmvc/setup.html
