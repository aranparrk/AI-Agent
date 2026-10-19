import { useState, useEffect } from "react";
import "./App.css";

const sample = [
  { id: 1, text: "HTML 연습" },
  { id: 2, text: "CSS 복습" },
  { id: 3, text: "자바스크립트이해" },
  { id: 4, text: "리액트프로젝트" },
];

const ToDosample = () => {
  const [toDoData, setToDoData] = useState(() => {
    const storeTodos = localStorage.getItem("todos");
    return storeTodos ? JSON.parse(storeTodos) : sample;
  }); // 상태관리 (랜더링 조건을 만들기 위해서 사용)
  const [inputText, setInputText] = useState(""); // 입력에 대한 상태관리
  const [nextId, setNextId] = useState(5); // ID증가에 대한 상태관리

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(toDoData));
  }, [toDoData]);

  const onClick = () => {
    const nextToDos = [...toDoData, { id: nextId, text: inputText }];
    setNextId(nextId + 1); // ID를 1 증가 시킴
    setToDoData(nextToDos);
    setInputText(""); // input 창을 지워 줌
  };

  const onRemove = (id) => {
    const nextToDos = toDoData.filter((todo) => todo.id !== id);
    setToDoData(nextToDos);
  };

  return (
    <div className="todo-container">
      <h1>📝 My ToDo List</h1>
      <p>오늘 할 일을 관리해보세요.</p>

      <div className="todo-input">
        <input
          type="text"
          placeholder="할 일을 입력하세요"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.nativeEvent.isComposing) {
              onClick();
            }
          }}
        />
        <button onClick={onClick}>추가</button>
      </div>

      <ul className="todo-list">
        {toDoData.map((toDo) => (
          <li key={toDo.id} onDoubleClick={() => onRemove(toDo.id)}>
            📌 {toDo.text}
          </li>
        ))}
      </ul>

      <p className="todo-guide">💡 더블클릭하면 삭제됩니다.</p>
    </div>
  );
};

export default ToDosample;
