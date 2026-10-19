import { useState, useMemo } from "react";

const getAverage = (numbers) => {
  console.log(numbers, "평균값 계산 중...");
  if (numbers.length === 0) return 0;

  const sum = numbers.reduce((a, b) => a + b);
  return sum / numbers.length;
};

const Average = () => {
  const [list, setList] = useState([]);
  const [number, setNumber] = useState("");

  const average = useMemo(() => getAverage(list), [list]);

  const onInsert = () => {
    const nextList = [...list, parseInt(number)];
    setList(nextList);
    setNumber("");
  };

  return (
    <>
      <label>
        정수입력{" "}
        <input
          type="text"
          value={number}
          onChange={(e) => setNumber(e.target.value)}
        />
      </label>
      <button onClick={onInsert}>등록</button>
      <ul>{list && list.map((e, index) => <li key={index}>{e}</li>)}</ul>
      <p>평균값 : {average}</p>
    </>
  );
};

export default Average;
