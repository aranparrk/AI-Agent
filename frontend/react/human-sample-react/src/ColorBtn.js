import { useState } from "react";
import styled from "styled-components";

const Container = styled.div`
  width: 500px;
  margin: 0 auto;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
`;

const Button = styled.button`
  flex: 1;
  height: 50px;

  background-color: ${(props) => props.$backgroundColor};
  color: white;
  border: none;
  font-size: 20px;
  cursor: pointer;
`;

const ColorDiv = styled.div`
  background-color: ${(props) => props.$backgroundColor};
  width: 500px;
  height: 300px;
  display: flex;
`;

const ColorBtn = () => {
  const [color, setColor] = useState("white");
  const colors = ["green", "orange", "purple", "red", "pink"];

  return (
    <Container>
      <div style={{ display: "flex", width: "100%" }}>
        {colors.map((color) => (
          <Button
            key={color}
            $backgroundColor={color}
            onClick={() => setColor(color)}
          >
            {color}
          </Button>
        ))}
      </div>
      <ColorDiv $backgroundColor={color}></ColorDiv>
    </Container>
  );
};

export default ColorBtn;
