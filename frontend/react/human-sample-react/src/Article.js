// 기사제목
// 내용
// 작성일
// 작성자
// props로 전달 받아 표시 하기
// 기본값 설정 사용
// 구조 분해 사용

const Article = ({ data }) => {
  return (
    <>
      <h1>{data.title}</h1>
      <p>{data.contents}</p>
      <p>{data.regDate}</p>
      <p>{data.writer}</p>
    </>
  );
};

export default Article;
