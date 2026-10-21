import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import Input from "../components/common/Input";
import Button from "../components/common/Button";
import { useState } from "react";

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

const Login = () => {
  const [username, setUsername] = useState("");
  const [inputPassword, setInputPassword] = useState("");

  const navigate = useNavigate();

  const id = "test";
  const password = "test1234";

  const handleLogin = (e) => {
    e.preventDefault();

    if (username === id && inputPassword === password) {
      navigate("/");
    } else {
      alert("아이디 또는 비밀번호가 일치하지 않습니다.");
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
      </LoginForm>
    </Container>
  );
};

export default Login;
