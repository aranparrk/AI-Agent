import "./App.css";
import SignUp from "./pages/SignUp";
import About from "./pages/About";
import Home from "./pages/Home";
import Profile from "./pages/Profile";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route element={<Layout />}>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/profile/:name" element={<Profile />} />
            <Route path="/signup" element={<SignUp />} />
          </Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
