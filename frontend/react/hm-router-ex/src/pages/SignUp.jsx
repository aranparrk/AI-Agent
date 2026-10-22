import styled from "styled-components";
import Button from "../components/common/Button.jsx";
import Input from "../components/common/Input.jsx";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import AxiosApi from "../api/AxiosApi.jsx";

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 32px 16px;
  box-sizing: border-box;
`;

const Form = styled.form`
  background-color: white;
  width: 500px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
`;

const Title = styled.div`
  text-align: center;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 28px;
  letter-spacing: -0.5px;
`;

const fields = [
  {
    label: "이메일",
    type: "email",
    name: "email",
    placeholder: "이메일을 입력하세요",
  },
  {
    label: "비밀번호",
    type: "password",
    name: "password",
    placeholder: "비밀번호를 입력하세요",
  },
  {
    label: "비밀번호확인",
    type: "password",
    name: "confirmPassword",
    placeholder: "비밀번호를 입력하세요",
  },
  {
    label: "이름",
    type: "text",
    name: "name",
    placeholder: "이름을 입력하세요",
  },
];

// 정규식
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const PWD_REGEX =
  /^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,20}$/;
const NAME_REGEX = /^[가-힣a-zA-Z]{2,10}$/;

const SignUp = () => {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    name: "",
  });

  // 실시간 유효성 검사
  const isEmail = EMAIL_REGEX.test(form.email);
  const isPwd = PWD_REGEX.test(form.password);
  const isPwdCheck =
    form.confirmPassword !== "" && form.password === form.confirmPassword;
  const isName = NAME_REGEX.test(form.name);

  const isAllValid = isEmail && isPwd && isPwdCheck && isName;

  // 오류 메시지
  const errors = {
    email: form.email && !isEmail ? "이메일 형식이 올바르지 않습니다." : "",

    password:
      form.password && !isPwd
        ? "영문, 숫자, 특수문자 포함 8~20자로 입력하세요."
        : "",

    confirmPassword:
      form.confirmPassword && !isPwdCheck
        ? "비밀번호가 일치하지 않습니다."
        : "",

    name: form.name && !isName ? "한글 또는 영문 2~10자로 입력하세요." : "",
  };

  const handleChange = (e) => {
    const { name, value } = e.target;

    setForm({ ...form, [name]: value });
  };

  const handleReset = () => {
    setForm({
      email: "",
      password: "",
      confirmPassword: "",
      name: "",
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!isAllValid) {
      alert("입력 내용을 확인해 주세요.");
      return;
    }

    try {
      const response = await AxiosApi.memberSignUp(
        form.email,
        form.password,
        form.name
      );

      if (response.data === false) {
        alert("회원가입에 실패했습니다.");
        return;
      }

      alert(`${form.name}님, 회원가입이 완료되었습니다!`);
      handleReset();
      navigate("/");
    } catch (error) {
      console.error("회원가입 실패:", error);
      alert("회원가입 중 오류가 발생했습니다.");
    }
  };

  return (
    <Container>
      <Form noValidate onSubmit={handleSubmit}>
        <Title>회원가입</Title>

        {fields.map((field) => (
          <Input
            key={field.name}
            label={field.label}
            type={field.type}
            name={field.name}
            placeholder={field.placeholder}
            value={form[field.name]}
            onChange={handleChange}
            error={errors[field.name]}
          />
        ))}

        <Button type="submit">가입하기</Button>
        <Button type="button" onClick={handleReset}>
          다시 작성
        </Button>
      </Form>
    </Container>
  );
};

export default SignUp;
