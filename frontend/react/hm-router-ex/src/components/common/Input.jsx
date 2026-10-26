import styled from "styled-components";

const Wrapper = styled.div`
  margin-bottom: 8px;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 6px;
`;

const StyledInput = styled.input`
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
`;

const ErrorText = styled.p`
  color: ${({ $success }) => ($success ? "#2e9e4f" : "red")};
  font-size: 12px;
  min-height: 16px;
  margin: 4px 0 0;
`;

const Input = ({ label, type = "text", name, error, success, ...rest }) => {
  return (
    <Wrapper>
      <Label>
        {label}
        <StyledInput type={type} name={name} {...rest} />
      </Label>
      <ErrorText $success={!!success && !error}>{error || success}</ErrorText>
    </Wrapper>
  );
};

export default Input;
