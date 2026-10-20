import styled from "styled-components";

const StyledInput = styled.input``;

const Wrapper = styled.div``;

const Label = styled.label``;

const ErrorText = styled.p``;

const Input = ({ label, type = "text", name, error, ...rest }) => {
  return (
    <Wrapper>
      <Label>{label}</Label>
      <StyledInput type={type} name={name} {...rest} />
      {error && <ErrorText>{error}</ErrorText>}
    </Wrapper>
  );
};

export default Input;
