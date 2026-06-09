# Books and Authors Manager - Django Project

A clean and interactive Django web application designed to manage a **Many-to-Many relationship** between **Books** and **Authors**. Users can create books and authors independently, view their full specifications, and establish dynamic reverse connections between them via an automated dashboard interface.

---

## 🚀 Features

### 📚 Books Management Dashboard (`/books`)

- Displays an input form to create books along with a complete dynamic list table.
- **Book Details Page (`/books/<id>`)**: Displays specific book attributes, an assigned authors roster, and a filtered dropdown menu to seamlessly inject new authors to that exact book.

### ✍️ Authors Management Dashboard (`/authors`)

- Displays an input form to register authors along with an overall roster list table.
- **Author Details Page (`/authors/<id>`)**: Displays specific author details, their entire bibliography roster, and a filtered dropdown menu to assign additional books to that specific author.

---

## 💾 Database Schema Mapping (Models)

The architectural structure utilizes Django’s built-in `ManyToManyField` with automated lookup capabilities:

```python
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method | Route URL                           | View Function              | Description                                              |
| ----------- | ----------------------------------- | -------------------------- | -------------------------------------------------------- |
| **GET**     | `/`                                 | `views.index`              | Redirects automatically to the main books directory.     |
| **GET**     | `/books`                            | `views.books_index`        | Renders the books log dashboard.                         |
| **POST**    | `/create_book`                      | `views.create_book`        | Validates and processes book creation data.              |
| **GET**     | `/books/<int:book_id>`              | `views.view_book`          | Renders the single book specification page.              |
| **POST**    | `/books/<int:book_id>/add_author`   | `views.add_author_to_book` | Links a chosen author entry to the active book instance. |
| **GET**     | `/authors`                          | `views.authors_index`      | Renders the authors log dashboard.                       |
| **POST**    | `/create_author`                    | `views.create_author`      | Validates and processes author creation data.            |
| **GET**     | `/authors/<int:author_id>`          | `views.view_author`        | Renders the single author profile spec page.             |
| **POST**    | `/authors/<int:author_id>/add_book` | `views.add_book_to_author` | Links a chosen book entry to the active author instance. |

---

## 📁 Project Workspace Configuration

Make sure your template infrastructure maps exactly to the workspace tree below:

```text
books_authors_proj/
│
├── books_authors_app/
│   ├── templates/
│   │   ├── books.html         # Main Books Log UI
│   │   ├── view_book.html     # Single Book & Author Association UI
│   │   ├── authors.html       # Main Authors Log UI
│   │   └── view_author.html   # Single Author & Book Association UI
│   ├── models.py
│   ├── urls.py
│   └── views.py

```

---

## 💡 Smart Query Architecture Optimization

To secure exceptional UX parameters and clean form validation loops, the database integration layer leverages specialized exclusions:

- **Inside Book Profile Views:**
  `Authors.objects.exclude(books=current_book)` ensures that authors who are already linked to the active book are automatically hidden from the dropdown selection panel.
- **Inside Author Profile Views:**
  `Books.objects.exclude(authors=current_author)` suppresses currently assigned book items from generating within selection inputs, preventing data injection overlap bugs.

---

## 🏃‍♂️ Initial Execution Sequence

1. Synchronize migrations and push target structures directly onto your backend database system:

```bash
python manage.py makemigrations
python manage.py migrate

```

2. Fire up the local web deployment server environment:

```bash
python manage.py runserver

```

3. Pull up your browser and interface directly via: `http://127.0.0.1:8000/books`

```

```
