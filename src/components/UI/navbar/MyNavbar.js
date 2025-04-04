import React from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import './MyNavbar.css';

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/login');
  };

  const isLoggedIn = !!localStorage.getItem('access');
  const fullName = `${localStorage.getItem('first_name') || ''} ${localStorage.getItem('last_name') || ''}`.trim();

  return (
    <nav className="navbar">
      <ul className="navbar-links">
          <li><Link to="/">Главная</Link></li>
          <li><Link to="/">Курсы</Link></li>
          <li><Link to="/">О нас</Link></li>
      </ul>
      <ul className="navbar-links">
        {isLoggedIn ? (
          <>
            <li><Link to="/">{fullName || 'Профиль'}</Link></li>
            <li><button onClick={handleLogout}>Выйти</button></li>
          </>
        ) : (
          <>
            <li><Link to="/register">Регистрация</Link></li>
            <li><Link to="/login">Вход</Link></li>
          </>
        )}
      </ul>
    </nav>
  );
}
