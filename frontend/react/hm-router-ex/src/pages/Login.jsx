import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import Input from "../components/common/Input";
import Button from "../components/common/Button";
import { useState } from "react";
import AxiosApi from "../api/AxiosApi.jsx";

const Container = styled.div`
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f6f8;
`;

const LoginForm = styled.form`
  width: 100%;
  max-width: 400px;
  padding: 40px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  box-sizing: border-box;
`;

const KakaoBtn = styled.button`
  width: 100%;
  height: 50px;
  color: #191919;
  background-color: #fee500; /* 카카오 노란색 */
  font-size: 15px;
  font-weight: 700;
  border: none;
  border-radius: 18px;
  cursor: pointer;
`;

// 카카오 인가 코드 요청 주소 (client_id = REST API 키, 공개돼도 되는 값)
const KAKAO_AUTH_URL =
  "https://kauth.kakao.com/oauth/authorize?response_type=code" +
  `&client_id=${process.env.REACT_APP_KAKAO_CLIENT_ID}` +
  "&redirect_uri=" +
  encodeURIComponent(process.env.REACT_APP_KAKAO_REDIRECT_URI);

const Login = () => {
  const [username, setUsername] = useState("");
  const [inputPassword, setInputPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await AxiosApi.memberLogIn(username, inputPassword);

      // 응답: { grantType, accessToken, accessTokenExpiresIn, refreshToken, refreshTokenExpiresIn }
      localStorage.setItem("accessToken", response.data.accessToken);
      localStorage.setItem("refreshToken", response.data.refreshToken);
      localStorage.setItem("email", username); // 화면 표시용 (내 댓글 삭제 버튼 등)
      localStorage.setItem("isLogin", "TRUE");
      navigate("/home", { replace: true }); // 뒤로가기로 로그인 화면에 다시 오지 않도록
    } catch (error) {
      console.error("로그인 실패:", error);
      alert(
        error.response?.data?.message ?? "이메일 또는 비밀번호가 틀립니다."
      );
    }
  };

  return (
    <Container>
      <LoginForm onSubmit={handleLogin}>
        <h2>로그인</h2>

        <Input
          label="아이디"
          name="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="아이디를 입력하세요"
        />

        <Input
          label="비밀번호"
          type="password"
          name="password"
          value={inputPassword}
          onChange={(e) => setInputPassword(e.target.value)}
          placeholder="비밀번호를 입력하세요"
        />

        <Button type="submit">로그인</Button>
        <KakaoBtn
          type="button"
          onClick={() => (window.location.href = KAKAO_AUTH_URL)}
        >
          카카오로 로그인
        </KakaoBtn>
        <Button type="button" onClick={() => navigate("/signup")}>
          회원가입
        </Button>
      </LoginForm>
    </Container>
  );
};

export default Login;
