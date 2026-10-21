import { Outlet } from "react-router-dom";
import styled from "styled-components";

const Header = styled.header`
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
`;

const Main = styled.main`
  min-height: 70vh;
  padding: 30px;
`;

const Footer = styled.footer`
  background-color: #eee;
  padding: 20px;
  text-align: center;
`;

const Layout = () => {
  return (
    <>
      <Header>헤더영역</Header>
      <Main>
        <Outlet />
      </Main>
      <Footer>푸터영역</Footer>
    </>
  );
};

export default Layout;
