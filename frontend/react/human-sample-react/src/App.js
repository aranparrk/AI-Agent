import logo from "./logo.svg";
import "./App.css";
import WelcomeProps from "./WelcomeProp";

function App() {
  // 자바스크립트 문법 구간
  const name = "안유진"; // 표현식 포함 하기
  // 성별, 나이, 주소 변수를 만들어 화면에 표시해보기
  const gender = "F";
  const age = "33";
  const addr = "충남 아산시";
  const score = "60";

  return (
    // 화면을 그려주는 구간
    <>
      <WelcomeProps
        name="안유진"
        gender="여자"
        age={20}
        addr="충남 아산시"
      ></WelcomeProps>
      <WelcomeProps
        name="장원영"
        gender="여자"
        age={22}
        addr="충남 천안시"
      ></WelcomeProps>
      <WelcomeProps
        name="리즈"
        gender="여자"
        age={23}
        addr="충남 보령시"
      ></WelcomeProps>
    </>
  );
}

export default App;
