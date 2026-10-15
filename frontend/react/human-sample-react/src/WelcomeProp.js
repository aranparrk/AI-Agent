// Props : 부모 컴포넌트에서 자식 컴포넌트로 전달되는 데이터

const WelcomeProps = (x) => {
  return (
    <>
      <h3>이름 : {x.name}</h3>
      <p>성별 : {x.gender}</p>
      <p>나이 : {x.age}</p>
      <p>주소 : {x.addr}</p>
    </>
  );
};

export default WelcomeProps;
