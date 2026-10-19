import { useState } from "react";

const MemberPractice = () => {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [members, setMembers] = useState([
    { id: 1, name: "김철수", age: 25 },
    { id: 2, name: "이영희", age: 28 },
    { id: 3, name: "박민수", age: 30 },
  ]);

  const addMember = () => {
    setMembers([
      ...members,
      // 여기에 새로운 회원 객체 추가!
      {
        id: Math.max(...members.map((member) => member.id)) + 1,
        name: name,
        age: Number(age),
      },
    ]);

    setName("");
    setAge("");
  };

  return (
    <>
      <input
        type="text"
        placeholder="이름"
        onChange={(e) => setName(e.target.value)}
        value={name}
      />
      <input
        type="number"
        placeholder="나이"
        onChange={(e) => setAge(e.target.value)}
        value={age}
      />
      <button onClick={addMember}>회원 추가</button>
      <table>
        <thead>
          <tr>
            <th>이름</th>
            <th>나이</th>
          </tr>
        </thead>
        <tbody>
          {members.map((member) => (
            <tr key={member.id}>
              <td>{member.name}</td>
              <td>{member.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default MemberPractice;
