// 운전하고 싶은 차량 선택하기 : 라디오 버튼, 그랜저, 산타페, 제네시스, 코나, 투싼
// 라디오 버튼은 여러 개중에 단 한 개를 선택하는 것

import { useState } from "react";

const RadioBtn = () => {
  const cars = ["그랜져", "산타페", "제네시스", "코나", "투싼"]; // 배열로 목록 관리

  // 선택된 다 하나의 값이므로 state 한 개로 충분
  const [selectedCar, setSelectedCar] = useState("");

  return (
    <>
      <p>라디오 버튼</p>
      {cars.map((car) => (
        <label key={car} style={{ marginRight: "12px" }}>
          <input
            type="radio"
            name="car"
            value={car}
            checked={selectedCar === car}
            onChange={(e) => setSelectedCar(e.target.value)}
          />
          {car}
        </label>
      ))}
      <h3>
        {selectedCar
          ? `선택한 차량 : ${selectedCar}`
          : "운전하고 싶은 차량을 선택하세요."}
      </h3>
    </>
  );
};

export default RadioBtn;
