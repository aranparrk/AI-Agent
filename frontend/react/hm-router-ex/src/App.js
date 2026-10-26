import "./App.css";
import SignUp from "./pages/SignUp";
import About from "./pages/About";
import Home from "./pages/Home";
import Profile from "./pages/Profile";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Login from "./pages/Login";
import BoardList from "./pages/boards/BoardList";
import BoardWrite from "./pages/boards/BoardWrite";
import BoardDetail from "./pages/boards/BoardDetail";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
          <Route element={<Layout />}>
            <Route path="/home" element={<Home />} />
            <Route path="/board" element={<BoardList />} />
            <Route path="/board/write" element={<BoardWrite />} />
            <Route path="/board/:boardId" element={<BoardDetail />} />

            <Route path="/about" element={<About />} />
            <Route path="/profile/:name" element={<Profile />} />
          </Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
