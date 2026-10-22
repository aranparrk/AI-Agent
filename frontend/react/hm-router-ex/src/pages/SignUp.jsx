import styled from "styled-components";
import Button from "../components/common/Button.jsx";
import Input from "../components/common/Input.jsx";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

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
  {
    label: "전화번호",
    type: "tel",
    name: "tel",
    placeholder: "전화번호를 입력하세요",
  },
];

const validate = (form) => {
  const errors = {};

  if (!form.email.includes("@")) {
    errors.email = "이메일 형식이 올바르지 않습니다.";
  }

  if (form.password.length < 8) {
    errors.password = "비밀번호는 8자 이상이어야 합니다.";
  }

  if (form.password !== form.confirmPassword) {
    errors.confirmPassword = "비밀번호가 일치하지 않습니다.";
  }

  if (form.name.trim() === "") {
    errors.name = "이름을 입력해 주세요.";
  }

  if (form.tel.trim() === "") {
    errors.tel = "전화번호를 입력해 주세요.";
  }

  return errors;
};

const SignUp = () => {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    name: "",
    tel: "",
  });

  const [errors, setErrors] = useState({});

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
      tel: "",
    });

    setErrors({});
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const error = validate(form);

    setErrors(error);

    if (Object.keys(error).length === 0) {
      alert(`${form.name}님, 회원가입이 완료되었습니다!`);
      handleReset();
      navigate("/");
    }
  };

  return (
    <Container>
      <Form noValidate onSubmit={handleSubmit}>
        <Title>회원가입</Title>
        {fields &&
          fields.map((field) => (
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
