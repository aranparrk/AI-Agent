// Props : 부모 컴포넌트에서 자식 컴포넌트로 전달되는 데이터

// 함수형 컴포넌트 생성 : 화살표 함수
// props : 객체로 이루어져 있음 (키와 값으로 구성된 속성들이 존재)
// 구조 분해 / 비구조화 할당 : {}
const WelcomeProps = ({
  name = "없음",
  gender = "F",
  age = 0,
  addr = "서울",
}) => {
  return (
    <>
      <h3>이름 : {name}</h3>
      <p>성별 : {gender}</p>
      <p>나이 : {age}</p>
      <p>주소 : {addr}</p>
    </>
  );
};

export default WelcomeProps;
