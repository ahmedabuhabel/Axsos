# Users - Django CRUD Project

A simple, responsive web application built with Python (Django framework) and Bootstrap 5. This project demonstrates core CRUD (Create and Read) operations using the Django Object-Relational Mapper (ORM) and a MySQL/SQLite database backend.

## 🚀 Features

- **Read (Display Data):** Automatically fetches and lists all recorded users from the database in a clean, responsive Bootstrap table.
- **Create (Insert Data):** Captures user registration data (`First Name`, `Last Name`, `Email`, and `Age`) via an integrated front-end form and commits it to the database.
- **Post/Redirect/Get Pattern:** Avoids form re-submission bugs on page refresh by securely handling inputs and executing server-side routing redirects.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.13+, Django 5.x
- **Frontend:** HTML5, Bootstrap 5
- **Database:** Django ORM (configured for MySQL / SQLite)

---

## 📂 Project Structure Overview

```text
├── your_project_name/
│   ├── settings.py
│   └── urls.py
├── your_app_name/
│   ├── models.py      # Contains the Users database schema
│   ├── views.py       # Handles the business logic for rendering and processing forms
│   ├── urls.py        # Maps routes ('/' and '/create') to specific views
│   └── templates/
│       └── index.html # Frontend view integrated with Bootstrap 5
├── manage.py
└── README.md

```

---

## 💾 Database Schema (Models)

The application uses a custom `Users` model defined in `models.py`:

```python
from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 🗺️ Application Routes

| Method   | Route     | Description                                                                         |
| -------- | --------- | ----------------------------------------------------------------------------------- |
| **GET**  | `/`       | Renders `index.html` displaying the list of all registered users.                   |
| **POST** | `/create` | Processes form submissions, saves a new user records via ORM, and redirects to `/`. |

---

## 🏃‍♂️ How to Run the Project Locally

### 1. Clone the repository and navigate to the project root

```bash
cd your-project-folder

```

### 2. Set up your virtual environment & install Django

```bash
# Create environment
python -m venv djangoPy3Env

# Activate environment (Mac/Linux)
source djangoPy3Env/bin/activate

# Activate environment (Windows)
djangoPy3Env\Scripts\activate

# Install Django
pip install django

```

### 3. Apply Migrations

Generate and run migrations to create the database schema tables.

```bash
python manage.py makemigrations
python manage.py migrate

```

### 4. Fire up the Development Server

```bash
python manage.py runserver

```

Open your browser and navigate to `http://localhost:8000/` to view the running application!

---

## 💡 Shell Commands Cheat Sheet

If you need to interact with the database directly using the **Django Shell** (`python manage.py shell`), here are some common queries implemented in this project setup:

- **Get all records sorted by first name:**
  `Users.objects.order_by('first_name')`
- **Update a record (e.g., ID 3):**
  `user = Users.objects.get(id=3); user.last_name = "Pancakes"; user.save()`
- **Delete a record (e.g., ID 2):**
  `Users.objects.get(id=2).delete()`

```

```
