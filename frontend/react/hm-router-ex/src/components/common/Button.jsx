import styled from "styled-components";

const StyledButton = styled.button`
  background-color: #ff5a36;
  color: white;
  width: 100%;
  height: 44px;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;

  &:hover {
    background-color: #e64a2b;
  }

  & + & {
    margin-top: 10px;
    background-color: #f3f4f6;
    color: #555;
  }

  & + &:hover {
    background-color: #e5e7eb;
  }
`;

const Button = ({ children, ...props }) => {
  return <StyledButton {...props}>{children}</StyledButton>;
};

export default Button;
