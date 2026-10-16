// 테이블 요소에 이벤트 추가하기
// 아이디, 이름, 나이, 주소로 구성된 배열 5개 생성

import { useState, useEffect } from "react";
import "./App.css";

const rowData = [
  { id: 1, name: "김철수", age: 25, address: "서울" },
  { id: 2, name: "이영희", age: 28, address: "부산" },
  { id: 3, name: "박민수", age: 30, address: "대전" },
  { id: 4, name: "최지은", age: 23, address: "수원" },
  { id: 5, name: "정하늘", age: 27, address: "인천" },
];

const Table = () => {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    // 서버에 대한 데이터를 비동기로 요청함
    setMembers(rowData);
  }, []); // [] 마운트 시작을 의미함

  return (
    <table>
      <thead>
        <tr>
          <th>아이디</th>
          <th>이름</th>
          <th>나이</th>
          <th>주소</th>
        </tr>
      </thead>
      <tbody>
        {members &&
          members.map((member) => (
            <tr key={member.id} onClick={() => alert(member.name)}>
              <td>{member.id}</td>
              <td>{member.name}</td>
              <td>{member.age}</td>
              <td>{member.address}</td>
            </tr>
          ))}
      </tbody>
    </table>
  );
};

export default Table;
