// 이름
// 비밀번호
// 나이
// 주소
// 이메일을 입력 받기
// 전부 입력 완료 되었을 때 확인 버튼을 누르면 입력 받은 결과를 출력하기

import { useState } from "react";

const InputEvent = () => {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [addr, setAddr] = useState("");
  const [email, setEmail] = useState("");

  return (
    <>
      <p>입력 연습</p>
      <input
        type="text"
        placeholder="이름 입력"
        onChange={(e) => setName(e.target.value)}
        value={name}
      />
      <input
        type="text"
        placeholder="나이 입력"
        onChange={(e) => setAge(e.target.value)}
        value={age}
      />
      <input
        type="text"
        placeholder="주소 입력"
        onChange={(e) => setAddr(e.target.value)}
        value={addr}
      />
      <input
        type="email"
        placeholder="이메일 입력"
        onChange={(e) => setEmail(e.target.value)}
        value={email}
      />
      <p>이름 : {name}</p>
      <p>나이 : {age}</p>
      <p>주소 : {addr}</p>
      <p>이메일 : {email}</p>
    </>
  );
};

export default InputEvent;
