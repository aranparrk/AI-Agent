import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  const handleChange = (e) => {
    navigate(`/profile/${e.target.value}`);
  };

  const isLoggedIn = localStorage.getItem("isLoggedIn");

  console.log(isLoggedIn);

  return (
    <div>
      <h1>여기가 홈 입니다.</h1>
      <p>가장 먼저 보여지는 페이지 입니다.</p>

      <select defaultValue="" onChange={handleChange}>
        <option value="" disabled>
          프로필 선택
        </option>
        <option value="frontend">프론트엔드</option>
        <option value="backend">백엔드</option>
        <option value="dba">dba</option>
      </select>
    </div>
  );
};

export default Home;
