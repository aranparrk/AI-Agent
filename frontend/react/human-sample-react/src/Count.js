import { useState } from "react";

import React from "react";

const Count = () => {
  const [number, setNumber] = useState(0);

  return (
    <>
      <h3>현재 카운트 : {number}</h3>
      <button onClick={() => setNumber(number + 1)}>증가</button>
      <button onClick={() => setNumber(number - 1)}>감소</button>
    </>
  );
};

export default Count;
