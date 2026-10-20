import styled, { css } from "styled-components";

const Container = styled.div`
  width: 1024px;
  margin: 0 auto;
  display: flex;
  padding: 1rem;
  background: ${(props) => props.color || "blue"};
`;

const Button = styled.button`
  background: white;
  color: black;
  border-radius: 4px;
  padding: 8px;
  box-sizing: border-box;
  font-weight: bold;
  &:hover {
    background: rgba(255, 255, 255, 0.5);
  }
  ${(props) =>
    props.inverted &&
    css`
      background: none;
      border: 2px solid white;
      color: white;
      &:hover {
        background: white;
        color: black;
      }
    `};
  & + button {
    margin-left: 1rem;
  }
`;

const Styled = () => {
  return (
    <Container color="orangered">
      <Button>일반 버튼</Button>
      <Button inverted={true}>반전 버튼</Button>
    </Container>
  );
};

export default Styled;
