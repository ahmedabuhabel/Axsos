# Relational Courses Manager - Django Project

A robust Django web application designed to catalog television network bootcamps and educational courses. This project implements full **CRUD operations** combined with advanced database modeling, leveraging **One-to-One** and **One-to-Many** relational tables alongside custom server-side validation layers and session-backed state preservation.

---

## 🚀 Architectural Features

- **Unified Input & Roster Dashboard (`/`)**: Integrates a dynamic structural course injection panel and a comprehensive data grid tracking entries on a singular responsive canvas.
- **Cascading Deletion Matrix (`/courses/destroy/<id>`)**: Implements an isolated verification screen mirroring defensive design standards before running purging calls against core indices.
- **Relational Architecture Integration**: Splinters standard database attributes across dedicated logical models to ensure a clean normalization structure.
- **Post/Redirect/Get (PRG Pattern)**: Form insertion actions run strictly in the background and terminate via an explicit redirect state, successfully stopping data corruption or form duplication on browser refresh cycles.

---

## 💾 Relational Database Schema Mapping (Models)

The entity relationships explicitly separate text attributes into unified models to maximize database design principles:

1. **`Course` ↔ `Description` (One-to-One)**: Splitting descriptions out into a standalone entity linked using `models.OneToOneField()`. Purging a course cascades automatically (`on_delete=models.CASCADE`) to drop its respective metadata row.
2. **`Course` ↔ `Comment` (One-to-Many / Ninja Bonus)**: Each distinct course acts as a parent host capable of holding an infinite array of comments via `models.ForeignKey()`.

```text
  ┌─────────────────┐             ┌─────────────────┐
  │   Description   │             │     Course      │
  ├─────────────────┤             ├─────────────────┤
  │ id (PK)         │ ◄─────────► │ id (PK)         │
  │ content         │  (1-to-1)   │ name            │
  └─────────────────┘             │ description_id  │
                                  └────────┬────────┘
                                           │
                                           │ (1-to-Many)
                                           ▼
                                  ┌─────────────────┐
                                  │     Comment     │
                                  ├─────────────────┤
                                  │ id (PK)         │
                                  │ content         │
                                  │ course_id (FK)  │
                                  └─────────────────┘

```

```python
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, post_data):
        # Server-side string auditing rules
        pass

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 🛡️ Input Validation Pipeline & State Preservation

Data payloads pass through a rigorous server validation framework managed inside `CourseManager`:

- **Name Constraint**: The course name field passes via `.strip()` and strictly mandates a minimum size of **more than 5 characters**.
- **Description Constraint**: Evaluates content length, preventing processing if text payloads sit at **15 characters or less**.
- **Session Cache Backup**: If validation thresholds trip, string structures are temporarily cached into `request.session` arrays. Upon redirecting back to index, fields are cleanly parsed and pre-populated using `.pop()`, keeping input fields populated without persisting data permanently.

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method  | Route URL                                  | View Function           | Description                                                                                       |
| ------------ | ------------------------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------- |
| **GET**      | `/`                                        | `views.index`           | Renders the primary dashboard roster tracking current courses and containing the creation forms.  |
| **POST**     | `/courses/create`                          | `views.create_course`   | Audits constraints, constructs separate Description objects, and binds new Courses.               |
| **GET**      | `/courses/destroy/<int:course_id>`         | `views.confirm_delete`  | Renders a contextual confirmation screen prompting verification before deleting records.          |
| **POST**     | `/courses/destroy/<int:course_id>/confirm` | `views.delete_course`   | Processes backend queries to purge row instances out of active storage.                           |
| **GET/POST** | `/courses/<int:course_id>/comments`        | `views.course_comments` | **Ninja Bonus Area**. Manages a micro-dashboard tracking specific course reviews and submissions. |

---

## 📁 Workspace Configuration

Ensure your physical directory structure exactly reflects the setup below:

```text
courses_proj/
│
├── courses_app/
│   ├── templates/
│   │   ├── index.html        # Central Course Form & Data Grid
│   │   ├── delete.html       # Isolation Gate Confirmation Layout
│   │   └── comments.html     # Interactive Review Sub-Panel (Ninja Bonus)
│   ├── models.py             # Database Schema Mapping & Core Managers
│   ├── urls.py               # Application Endpoint Registry
│   └── views.py              # Logical Pipeline Controller Handlers

```

---

## 🏃‍♂️ Initial Installation Sequence

1. Initialize your terminal profile, shifting down into the root system folder of your project workspace.
2. Formulate and synchronize target migration components to build your localized database schema:

```bash
python manage.py makemigrations
python manage.py migrate

```

3. Initialize the development web server instance:

```bash
python manage.py runserver

```

4. Access the primary application interface by directing an active browser window to: `http://127.0.0.1:8000/`

```

```
