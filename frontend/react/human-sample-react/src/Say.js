import { useState } from "react";

const Say = () => {
  const [message, setMessage] = useState(""); // 상태관리
  const [color, setColor] = useState("black");
  const [name, setName] = useState("");

  // purple, yellow 버튼 추가하기
  // 웰컴, 환영합니다. {}님

  return (
    <>
      <input
        type="text"
        placeholder="이름 입력"
        onChange={(e) => setName(e.target.value)}
        value={name}
      />
      <br />
      <button onClick={() => setMessage(`안녕하세요!! ${name}님`)}>입장</button>
      <button onClick={() => setMessage(`안녕히 가세요 ${name}님`)}>
        퇴장
      </button>
      <button onClick={() => setMessage(`환영합니다. ${name}님`)}>웰컴</button>
      <button onClick={() => setMessage()}>지우기</button>

      <h1 style={{ color }}>{message}</h1>
      <button style={{ color: "red" }} onClick={() => setColor("red")}>
        빨간색
      </button>
      <button style={{ color: "green" }} onClick={() => setColor("green")}>
        초록색
      </button>
      <button style={{ color: "blue" }} onClick={() => setColor("blue")}>
        파란색
      </button>
      <button style={{ color: "purple" }} onClick={() => setColor("purple")}>
        보라색
      </button>
      <button style={{ color: "yellow" }} onClick={() => setColor("yellow")}>
        노란색
      </button>
    </>
  );
};

export default Say;
