import styled from "styled-components";

const StyledButton = styled.button`
  background-color: orangered;
  color: white;
  width: 100%;
  height: 20px;
  &:hover {
    background-color: red;
  }

  & + & {
    margin-top: 10px;
  }
`;

const Button = ({ children, ...props }) => {
  return <StyledButton {...props}>{children}</StyledButton>;
};

export default Button;
