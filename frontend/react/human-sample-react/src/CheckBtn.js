import { useState } from "react";

const CheckBtn = () => {
  const cars = ["그랜저", "싼타페", "제네시스", "코나", "투싼"];

  const [selectedCar, setSelectedCar] = useState([]);

  const hadleChange = (e) => {
    if (e.target.checked) {
      setSelectedCar([...selectedCar, e.target.value]);
    } else {
      setSelectedCar(selectedCar.filter((car) => car !== e.target.value));
    }
  };

  const handleSelectAll = (e) => {
    if (e.target.checked) {
      setSelectedCar(cars);
    } else {
      setSelectedCar([]);
    }
  };

  return (
    <>
      <p>체크 박스</p>
      <label>
        <input
          type="checkbox"
          onChange={handleSelectAll}
          checked={selectedCar.length == cars.length}
        />
        전체 선택
      </label>
      {cars.map((car) => (
        <label key={car} style={{ marginRight: "12px" }}>
          <input
            type="checkbox"
            value={car}
            onChange={hadleChange}
            checked={selectedCar.includes(car)}
          />
          {car}
        </label>
      ))}
      <h3>
        {selectedCar.length > 0
          ? `선택한 차량 : ${selectedCar.join(", ")}`
          : "운전하고 싶은 차량을 선택하세요."}
      </h3>
    </>
  );
};

export default CheckBtn;
