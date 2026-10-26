import { useState, useEffect } from "react";

// 이름, 닉네임, 주소를 입력 받아 출력해보기 : useState
// useEffect를 언제 호출되는지 확인 해보기

const Information = () => {
  const [name, setName] = useState("");
  const [nickName, setNickName] = useState("");
  const [addr, setAddr] = useState("");

  useEffect(() => {
    console.log("랜더링 완료 이후 호출!!");
    console.log({ name, nickName, addr });
  }, [name]);

  return (
    <>
      <label>
        이름
        <input
          type="text"
          placeholder="이름"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <br />
      <label>
        닉네임
        <input
          type="text"
          placeholder="닉네임"
          value={nickName}
          onChange={(e) => setNickName(e.target.value)}
        />
      </label>
      <br />
      <label>
        주소
        <input
          type="text"
          placeholder="주소"
          value={addr}
          onChange={(e) => setAddr(e.target.value)}
        />
      </label>
      {name && nickName && addr && (
        <div>
          <p>이름 : {name}</p>
          <p>닉네임 : {nickName}</p>
          <p>주소 : {addr}</p>
        </div>
      )}
    </>
  );
};

export default Information;
