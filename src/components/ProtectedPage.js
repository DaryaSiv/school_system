import React, { useEffect, useState } from 'react';
import './styles/NewsPage.css'; // для оформления

export default function ProtectedPage() {
  const [newsList, setNewsList] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('access');

    if (!token) {
      setNewsList([]);
      return;
    }

    // Пока новости фейковые — потом можно заменить на API-запрос
    const mockNews = [
      {
        id: 1,
        title: 'Запуск новой системы тестирования',
        content: 'Теперь учителя могут создавать интерактивные тесты и делиться ими с учениками.',
        date: '2025-04-03',
      },
      {
        id: 2,
        title: 'Поддержка ИИ-помощника в уроках',
        content: 'Добавлена возможность использовать AI-помощника для генерации заданий.',
        date: '2025-04-01',
      },
      {
        id: 3,
        title: 'Обновление дизайна личного кабинета',
        content: 'Интерфейс стал более удобным для учителей и учеников.',
        date: '2025-03-25',
      },
    ];

    setNewsList(mockNews);
  }, []);

  if (!localStorage.getItem('access')) {
    return (
      <div className="news-container">
        <h2>Нет доступа. Пожалуйста, войдите в систему.</h2>
      </div>
    );
  }

  return (
    <div className="news-container">
      <h2>Новости системы</h2>
      <div className="news-list">
        {newsList.map((news) => (
          <div className="news-card" key={news.id}>
            <h3>{news.title}</h3>
            <p className="news-date">{news.date}</p>
            <p>{news.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

