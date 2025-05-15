# ITFree806 — сервис расписания компьютерных классов

*Учебный pet-project, который спасает студентов и преподавателей
от хаоса с аудиториями. Разрабатывается в рамках дисциплины
«Программирование на языке Python».*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white"/>
</p>

---

## 📑 TL;DR

| Что? | Кратко |
|------|--------|
| **Зачем** | Мгновенно показать, когда свободен любой комп-класс, и дать забронировать его за пару кликов |
| **Кто делает** | [Александр Малахов](https://github.com/Couurage) (тим-лид, front) · [Геннадий Стадник](#) (back + front) |
| **Статус** | MVP готов к защите (май 2025), демо в ветке `main` |
| **Дальше** | PostgreSQL, PWA-обёртка |

---

## 🚀 Возможности

- **🔑 Пользователи и роли** — student / teacher / admin, восстановление пароля по e-mail.  
- **📅 Расписание** — просмотр, фильтры, поиск, цветовая индикация свободных слотов.  
- **📌 Бронирование** — защита от конфликтов, пакетный импорт Excel.  
- **🔄 Интеграции** — экспорт в Google Calendar.  
- **🌓 UI / UX** — адаптивная сетка, тёмная тема (beta), PWA-иконка.

---

## 🛠️ Технологический стек

| Уровень | Технологии |
|---------|------------|
| **Backend** | Python 3.11, Django 4.x, Django REST Framework |
| **Frontend** | HTML5, CSS3 (SCSS), Vanilla JS + Alpine.js |
| **База данных** | SQLite (dev) → PostgreSQL (prod) |
| **DevOps** | Docker / Docker-compose, Nginx proxy, GitHub Actions (pytest + flake8) |
| **Интеграции** | Google Calendar API |
| **Тестирование** | PyTest, Coverage, Lighthouse CI |

---

## 🛠️ Быстрый старт

```bash
git clone https://github.com/dmitriiVin/project.git
cd project

# Локально
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver          # → http://localhost:8000

# Или Docker
docker compose up --build
```

> ⚙️  Секреты (`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`) — в файле `.env`  
> (пример — `.env.example`).

---

## 👥 Команда

| Участник | Роль и зона ответственности |
|----------|-----------------------------|
| [**Александр Малахов**](https://github.com/Couurage) | **Тим-лид · Front-end** — UI/UX, роутинг, адаптив, ревью |
| [**Геннадий Стадник**](#) | **Back-end · Front-end** — модели, логика, CI/CD, интеграции |

---

## 📜 История (март → май 2025)

| Дата | Commit / ветка | Что сделано | Кто |
|------|----------------|-------------|-----|
| 12 марта | `ddb246d` | Инициализация Django-проекта | **Дмитрий(отчислился)** |
| 14 марта | `19be4c1` | Модели `Audience` / `Lesson` / `CustomUser` | **Геннадий** |
| 21 марта | `ui-mockups` | Черновой главный экран, навбар | **Александр** |
| 25 марта | `3c9f7ab` | CRUD-view аудиторий, фильтр в админке | **Геннадий** |
| 31 марта | `auth-refactor` | Кастомная регистрация + reset-email | **Геннадий** |
| 7 апреля | `0f0a2de` | SQL-проверка конфликтов | **Геннадий** |
| 12 апреля | `responsive-styles` | Полный mobile-first + dark-mode beta | **Александр** |
| 18 апреля | `5b1a88e` | Импорт CSV/XLSX + unit-тесты | **Геннадий** |
| 23 апреля | `google-sync-draft` | OAuth-sync с Google Calendar | **Геннадий + ревью Александр** |
| 25 апреля | `a77c4f8` | Финальный UI-polish: цвет, tooltip’ы | **Александр** |
| 30 апреля | `c2e514b` | Docker-compose, GitHub Actions | **Геннадий** |
| 5 мая | `fa9d0e0` | Merge-party, README 2.0 | **Оба** |
| 15 мая | `1f3b7cc` | Lighthouse 95 +, баг-фиксы | **Александр** |

> 🎯 **Дорожная карта:** PostgreSQL → PWA → релиз для кафедры.

---

## 📬 Обратная связь

Нашли баг или есть идея?  
Создайте issue или пишите на **alexandr6450@gmail.com** — отвечаем быстро 😉
