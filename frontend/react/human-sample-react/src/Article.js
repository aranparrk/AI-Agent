// 기사제목
// 내용
// 작성일
// 작성자
// props로 전달 받아 표시 하기
// 기본값 설정 사용
// 구조 분해 사용

const Article = ({ data }) => {
  const { title, content, name, regDate, likeCount, commentCount } = data;

  const formattedDate = regDate.slice(0, 16).replace("T", " ");

  return (
    <>
      <h1>제목 | {title}</h1>
      <p>내용 | {content}</p>
      <p>작성자 | {name}</p>
      <p>작성일 | {formattedDate}</p>
      <p>좋아요 | {likeCount}</p>
      <p>댓글수 | {commentCount}</p>
    </>
  );
};

export default Article;
