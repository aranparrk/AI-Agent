import logo from "./logo.svg";
import "./App.css";
import Article from "./Article";
import { useState, useEffect } from "react";
import Say from "./Say";
import InputEvent from "./InputEvent";
import DropDown from "./DropDown";
import RadioBtn from "./RadioBtn";
import CheckBtn from "./CheckBtn";

// const data = [
//   {
//     id: 1,
//     title: "안녕하세요! 처음 가입했습니다.",
//     content: "오늘 처음 가입했어요. 앞으로 잘 부탁드립니다!",
//     email: "minsu@gmail.com",
//     name: "김민수",
//     regDate: "2026-10-15 09:10",
//     likeCount: 5,
//     commentCount: 3,
//   },
//   {
//     id: 2,
//     title: "React 공부하다가 궁금한 점이 생겼어요.",
//     content: "props와 state의 차이가 정확히 뭔가요?",
//     email: "jiyeon@gmail.com",
//     name: "이지연",
//     regDate: "2026-10-15 09:30",
//     likeCount: 8,
//     commentCount: 6,
//   },
//   {
//     id: 3,
//     title: "오늘 점심 메뉴 추천받아요!",
//     content: "매일 점심 메뉴 고르는 게 제일 어렵네요. 추천 부탁드려요.",
//     email: "junho@naver.com",
//     name: "박준호",
//     regDate: "2026-10-15 10:15",
//     likeCount: 12,
//     commentCount: 9,
//   },
//   {
//     id: 4,
//     title: "Spring Boot 게시판 구현 성공!",
//     content: "드디어 게시글 등록, 조회, 수정, 삭제 기능을 완성했습니다.",
//     email: "sujin@gmail.com",
//     name: "최수진",
//     regDate: "2026-10-15 10:40",
//     likeCount: 20,
//     commentCount: 7,
//   },
//   {
//     id: 5,
//     title: "개발 공부할 때 집중하는 방법 있나요?",
//     content:
//       "오래 앉아서 공부하다 보면 집중력이 떨어지는데 다들 어떻게 하시나요?",
//     email: "hyunwoo@naver.com",
//     name: "정현우",
//     regDate: "2026-10-15 11:20",
//     likeCount: 15,
//     commentCount: 11,
//   },
//   {
//     id: 6,
//     title: "Java와 JavaScript 차이가 헷갈려요.",
//     content: "이름은 비슷한데 문법과 동작 방식이 많이 다르네요.",
//     email: "yuna@gmail.com",
//     name: "김유나",
//     regDate: "2026-10-15 11:45",
//     likeCount: 7,
//     commentCount: 4,
//   },
//   {
//     id: 7,
//     title: "주말에 다들 뭐 하시나요?",
//     content:
//       "이번 주말에는 공부 말고 좀 쉬려고 하는데 할 만한 거 추천해 주세요.",
//     email: "donghyun@naver.com",
//     name: "이동현",
//     regDate: "2026-10-15 12:30",
//     likeCount: 9,
//     commentCount: 8,
//   },
//   {
//     id: 8,
//     title: "SQL JOIN 복습 중입니다.",
//     content: "INNER JOIN과 LEFT JOIN을 다시 공부하고 있어요.",
//     email: "eunji@gmail.com",
//     name: "박은지",
//     regDate: "2026-10-15 13:10",
//     likeCount: 11,
//     commentCount: 5,
//   },
//   {
//     id: 9,
//     title: "VS Code 단축키 추천해 주세요.",
//     content: "코딩 속도를 높이고 싶은데 자주 사용하는 단축키가 궁금합니다.",
//     email: "seungho@naver.com",
//     name: "오승호",
//     regDate: "2026-10-15 14:20",
//     likeCount: 6,
//     commentCount: 2,
//   },
//   {
//     id: 10,
//     title: "오늘도 공부하느라 고생하셨습니다!",
//     content: "하루 종일 코딩하느라 힘들었지만 하나씩 이해하니까 재미있네요.",
//     email: "hayeon@gmail.com",
//     name: "정하연",
//     regDate: "2026-10-15 15:10",
//     likeCount: 18,
//     commentCount: 10,
//   },
// ];

function App() {
  // const [data, setData] = useState([]);

  // useEffect(() => {
  //   fetch("http://localhost:8111/board/list")
  //     .then((response) => response.json())
  //     .then((result) => {
  //       console.log("서버에서 받은 데이터 : ", result);
  //       setData(result);
  //     })
  //     .catch((error) => {
  //       console.error("API 요청 실패 : ", error);
  //     });
  // }, []);

  // return (
  //   // 화면을 그려주는 구간
  //   <>{data && data.map((e) => <Article key={e.id} data={e} />)}</>
  // );

  return (
    <>
      <CheckBtn />
    </>
  );
}

export default App;
