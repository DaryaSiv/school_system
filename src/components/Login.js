import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [form, setForm] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // 1. Вход
      const res = await axios.post('http://localhost:8000/api/login/', form);
      const access = res.data.access;
      const refresh = res.data.refresh;

      localStorage.setItem('access', access);
      localStorage.setItem('refresh', refresh);

      // 2. Получение имени и фамилии
      const userRes = await axios.get('http://localhost:8000/api/me/', {
        headers: { Authorization: `Bearer ${access}` },
      });

      const { first_name, last_name } = userRes.data;
      localStorage.setItem('first_name', first_name);
      localStorage.setItem('last_name', last_name);

      navigate('/'); // переход на главную страницу

    } catch (err) {
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h2>Вход</h2>
      <input
        name="username"
        placeholder="Имя пользователя"
        onChange={handleChange}
        required
      />
      <input
        name="password"
        type="password"
        placeholder="Пароль"
        onChange={handleChange}
        required
      />
      <button path="/" type="submit">Войти</button>
    </form>
  );
}
