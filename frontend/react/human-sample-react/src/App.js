import logo from "./logo.svg";
import "./App.css";
import Article from "./Article";

const data = [
  {
    title: "정치",
    contents: "민주당과 국민의 힘이 열심히 싸우고 있어요",
    writer: "조성봉 기자",
    date: "2026-10-15 PM 03:12",
  },
  {
    title: "경제",
    contents: "코스피가 왜 이럴까??",
    writer: "이현주 기자",
    date: "2026-10-15 PM 03:13",
  },
  {
    title: "사회",
    contents: "부산에 상어가 집에를 안가고 있음",
    writer: "안유진 기자",
    date: "2026-10-15 PM 03:14",
  },
  {
    title: "문화",
    contents: "사람들이 책을 읽지 않아서 서점이 망함",
    writer: "장원영 기자",
    date: "2026-10-15 PM 03:15",
  },
  {
    title: "스포츠",
    contents: "엘지가 승리해서 플레이오프 진출",
    writer: "박해민 기자",
    date: "2026-10-15 PM 03:15",
  },
];

function App() {
  return (
    // 화면을 그려주는 구간
    <>{data && data.map((e, index) => <Article key={index} data={e} />)}</>
  );
}

export default App;
