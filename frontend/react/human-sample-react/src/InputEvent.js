// 이름
// 비밀번호
// 나이
// 주소
// 이메일을 입력 받기
// 전부 입력 완료 되었을 때 확인 버튼 누르면 입력 받은 결과를 출력 하기

import { useState } from "react";

const InputEvent = () => {
  // 여기에 name 상태 선언하기
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [age, setAge] = useState("");
  const [addr, setAddr] = useState("");
  const [email, setEmail] = useState("");

  // 입력값
  const onChangeName = (e) => setName(e.target.value);
  const onChangePassword = (e) => setPassword(e.target.value);
  const onChangeAge = (e) => setAge(e.target.value);
  const onChangeAddr = (e) => setAddr(e.target.value);
  const onChangeEmail = (e) => setEmail(e.target.value);

  // 확인 버튼을 누른 시점의 결과를 저장할 상태
  const [result, setResult] = useState(null);

  // 모든 입력값이 채워졌는지 검사
  const isAllFilled =
    name.trim() !== "" &&
    password.trim() !== "" &&
    age.trim() !== "" &&
    addr.trim() !== "" &&
    email.trim() !== "";

  // 확인 버튼
  const onSubmit = (e) => {
    // 새로고침 방지
    e.preventDefault();

    if (!isAllFilled) {
      alert("미입력 항목이 존재 합니다.");
      return;
    }

    setResult({ name, password, age, addr, email });
  };

  // 초기화 버튼
  const onReset = () => {
    setName("");
    setPassword("");
    setAge("");
    setAddr("");
    setEmail("");
    setResult(null);
  };

  return (
    <>
      <p>입력 연습</p>
      {/* 여기에 input 작성하기 */}
      <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="이름 입력"
          onChange={onChangeName}
          value={name}
        />
        <input
          type="password"
          placeholder="비밀번호 입력"
          onChange={onChangePassword}
          value={password}
        />
        <input
          type="text"
          placeholder="나이 입력"
          onChange={onChangeAge}
          value={age}
        />
        <input
          type="text"
          placeholder="주소 입력"
          onChange={onChangeAddr}
          value={addr}
        />
        <input
          type="email"
          placeholder="이메일 입력"
          onChange={onChangeEmail}
          value={email}
        />
        <button type="submit" disabled={!isAllFilled}>
          확인
        </button>
        <button type="button" onClick={onReset}>
          초기화
        </button>
      </form>
      {result && (
        <div>
          <p>이름 : {result.name}</p>
          <p>비밀번호 : {"*".repeat(result.password.length)}</p>
          <p>나이 : {result.age}</p>
          <p>주소 : {result.addr}</p>
          <p>이메일 : {result.email}</p>
        </div>
      )}
    </>
  );
};

export default InputEvent;
