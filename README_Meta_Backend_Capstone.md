# 🍋 Meta Backend Capstone Project – Little Lemon

This is a capstone project for the **Meta Back-End Development** course. It showcases a fully functional Django-based restaurant booking and menu management web application.

---

## 🚀 Features

- Menu item listing & detail views (API)
- Restaurant booking system (API)
- Admin CRUD capabilities
- Token-based authentication for API testing
- MySQL database integration

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd LittleLemon
```

### 2. Create and Activate a Virtual Environment
```bash
pipenv shell
pipenv shell  # Windows
# source capstone/bin/activate  # macOS/Linux
```

### 3. Install Required Packages
```bash
pip install django
pip install djoser
pip3 install mysqlclient
pip3 install djangorestframework
```

---


## 🧪 API Endpoints

### Menu
- `GET /restaurant/menu/` – View all menu items
- `GET /restaurant/menu/<int:pk>` – View individual menu item

### Bookings
- `GET /restaurant/booking/` – View booked tables (auth required)

---

## 🧩 HTML Templates

- `/restaurant/` – Loads `index.html` from the **project's `templates/` folder** (already registered in `settings.py`)

---

## 🔐 Authentication Tokens

You can use the following tokens for testing in tools like **Insomnia** or **Postman**:

- **User:** `testuser`
- **Password:** `testing@123!`

```http
Authorization: Token 748deb4c5dd393dd26eaaacaea979144345b7676
```


## 🔧 Migrations and Superuser

```bash
python manage.py makemigrations
python manage.py migrate
---

## 📂 Project Structure

```
little-lemon-web-app/
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── restaurant/
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   └── index.html
│   └── ...
├── manage.py
└── Pipfile
```

---

## 🧼 Final Notes

- Ensure MySQL service is running before using `runserver`.
- Use `python manage.py runserver` to start the development server.
- Use tokens in your API client to test authenticated endpoints.

---

## 👨‍💻 Author

Project by [Your Name], as part of the Meta Back-End Developer Capstone.