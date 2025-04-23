import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // ✅ импортируем
import Input from './UI/input/Input';
import './styles/auth.css'; // ✅ поправил импорт (не надо писать `styles = ...`)

export default function Register() {
  const navigate = useNavigate(); // ✅ используем хук для редиректа

  const [form, setForm] = useState({
    username: '',
    email: '',
    password: '',
    first_name: '',
    last_name: '',
    role: 'student',
  });

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // 1. Регистрируем пользователя
      await axios.post('http://localhost:8000/api/register/', form);
  
      // 2. Выполняем вход
      const loginRes = await axios.post('http://localhost:8000/api/login/', {
        username: form.username,
        password: form.password,
      });
  
      const access = loginRes.data.access;
      const refresh = loginRes.data.refresh;
  
      localStorage.setItem('access', access);
      localStorage.setItem('refresh', refresh);
  
      // 3. Получаем имя и фамилию
      const userRes = await axios.get('http://localhost:8000/api/me/', {
        headers: { Authorization: `Bearer ${access}` },
      });
  
      const { first_name, last_name } = userRes.data;
      localStorage.setItem('first_name', first_name);
      localStorage.setItem('last_name', last_name);
  
      navigate('/');
    } catch (err) {
      console.error(err);
    }
  };
  

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      <h2>Регистрация</h2>
      <Input name="username" placeholder="Имя пользователя" onChange={handleChange} required />
      <Input name="email" type="email" placeholder="Email" onChange={handleChange} required />
      <Input name="first_name" placeholder="Имя" onChange={handleChange} />
      <Input name="last_name" placeholder="Фамилия" onChange={handleChange} />
      <select name="role" onChange={handleChange}>
        <option value="student">Ученик</option>
        <option value="teacher">Учитель</option>
      </select>
      <input name="password" type="password" placeholder="Пароль" onChange={handleChange} required />
      <button path="/" type="submit">Зарегистрироваться</button>
    </form>
  );
}
