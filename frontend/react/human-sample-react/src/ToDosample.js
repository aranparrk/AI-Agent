import { useState } from "react";

const sample = [
  { id: 1, text: "HTML 연습" },
  { id: 2, text: "CSS 복습" },
  { id: 3, text: "자바스크립트이해" },
  { id: 4, text: "리액트프로젝트" },
];

const ToDosample = () => {
  const [toDoData, setToDoData] = useState(sample); // 상태관리 (랜더링 조건을 만들기 위해서 사용)
  const [inputText, setInputText] = useState(""); // 입력에 대한 상태관리
  const [nextId, setNextId] = useState(5); // ID증가에 대한 상태관리

  const onClick = () => {
    const nextToDos = [...toDoData, { id: nextId, text: inputText }];
    setNextId(nextId + 1); // ID를 1 증가 시킴
    setToDoData(nextToDos);
    setInputText(""); // input 창을 지워 줌
  };

  return (
    <>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
      />
      <button onClick={onClick}>추가</button>
      <ul>
        {toDoData && toDoData.map((toDo) => <li key={toDo.id}>{toDo.text}</li>)}
      </ul>
    </>
  );
};

export default ToDosample;
