import { useState } from "react";

const MemberPractice = () => {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [members, setMembers] = useState([
    { id: 1, name: "김철수", age: 25 },
    { id: 2, name: "이영희", age: 28 },
    { id: 3, name: "박민수", age: 30 },
  ]);
  const [errorMessage, setErrorMessage] = useState("");

  const addMember = () => {
    if (!name.trim()) {
      setErrorMessage("이름을 입력해주세요.");
      return;
    }

    if (!age) {
      setErrorMessage("나이를 입력해주세요.");
      return;
    }

    if (Number(age) <= 0) {
      setErrorMessage("나이는 1 이상을 입력해주세요.");
      return;
    }

    if (!Number.isInteger(Number(age))) {
      setErrorMessage("나이는 정수를 입력해주세요.");
      return;
    }

    setMembers([
      ...members,
      // 여기에 새로운 회원 객체 추가!
      {
        id:
          members.length > 0
            ? Math.max(...members.map((member) => member.id)) + 1
            : 1,
        name: name.trim(),
        age: Number(age),
      },
    ]);

    setName("");
    setAge("");
    setErrorMessage("");
  };

  const onRemove = (id) => {
    setMembers(members.filter((member) => member.id !== id));
  };

  return (
    <>
      <input
        type="text"
        placeholder="이름"
        onChange={(e) => {
          setName(e.target.value);
          setErrorMessage("");
        }}
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
            <th>관리</th>
          </tr>
        </thead>
        <tbody>
          {members.map((member) => (
            <tr key={member.id}>
              <td>{member.name}</td>
              <td>{member.age}</td>
              <td>
                <button onClick={() => onRemove(member.id)}>삭제</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <p>{errorMessage}</p>
    </>
  );
};

export default MemberPractice;
