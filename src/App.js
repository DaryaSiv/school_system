import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Navbar from './components/UI/navbar/MyNavbar.js';
import Register from './components/Register';
import Login from './components/Login';
import ProtectedPage from './components/ProtectedPage';

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<ProtectedPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  );
}

export default App;

