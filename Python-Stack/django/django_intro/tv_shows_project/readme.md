# Semi-Restructured TV Shows Manager - Django Project

A robust Django web application that implements complete **CRUD (Create, Read, Update, Delete)** operations to manage a television network showcase directory. Built with server-side validations, dynamic data parsing, and a responsive **Bootstrap 5** user interface.

---

## 🚀 Features

- **Create**: Dedicated validation input panel to seamlessly inject new shows with proper datetime configurations (`/shows/new`).
- **Read**:
  - Comprehensive dashboard index roster tracking all sub-entries within a central datatable (`/shows`).
  - Isolated individual profiles displaying exhaustive metadata for a specific series (`/shows/<id>`).
- **Update**: Pre-populated contextual edit forms with automated formatting pipes to safely override current database records (`/shows/<id>/edit`).
- **Delete**: Direct cascading deletion handlers to purge unwanted indices from the filesystem instantly.

---

## 💾 Database Schema Mapping (Models)

The architecture maps out entity requirements via Django's persistent object-relational abstraction layer:

```python
from django.db import models

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method  | Route URL                     | View Function       | Description                                                     |
| ------------ | ----------------------------- | ------------------- | --------------------------------------------------------------- |
| **GET**      | `/`                           | `views.index`       | Root route. Re-routes incoming traffic to `/shows`.             |
| **GET**      | `/shows`                      | `views.shows_index` | Renders the primary dashboard table displaying all shows.       |
| **GET**      | `/shows/new`                  | `views.new_show`    | Renders the creation form canvas.                               |
| **POST**     | `/shows/create`               | `views.create`      | Validates and processes structural payloads for new insertions. |
| **GET**      | `/shows/<int:show_id>`        | `views.view_show`   | Displays comprehensive attributes for a single series.          |
| **GET**      | `/shows/<int:show_id>/edit`   | `views.edit_show`   | Renders the edit layout with pre-populated field states.        |
| **POST**     | `/shows/<int:show_id>/update` | `views.update`      | Validates and saves updated field data into the database.       |
| **POST/GET** | `/shows/<int:show_id>/delete` | `views.delete_show` | Purges the isolated row reference out of active memory.         |

---

## 📁 Project Workspace Configuration

Ensure your physical layout replicates the following directory setup:

```text
tv_shows_project/
│
├── tv_shows_app/
│   ├── templates/
│   │   ├── index.html        # All Shows Roster View
│   │   ├── new.html          # Add New Show Entry Form
│   │   ├── edit.html         # Edit Current Show Form
│   │   └── show_details.html # Specific Show Inspection Panel
│   ├── models.py
│   ├── urls.py
│   └── views.py

```

---

## 💡 Key Implementations & Edge Case Fixes

- **HTML5 Date Inputs Match (`|date:'Y-m-d'`)**: Form edit fields enforce native format parsing specifications ($YYYY-MM-DD$). This project utilizes Django pipe processing tokens (`value="{{ show.release_date|date:'Y-m-d' }}"`) to completely bypass browser formatting interpretation errors.
- **Textarea Value Allocation**: Adheres to strict DOM syntax hierarchies by populating `<textarea>` structural inner-contexts (`<textarea>{{ show.description }}</textarea>`) rather than assigning flat `value` attributes.
- **Post/Redirect/Get (PRG Pattern)**: All active execution calls (`/create`, `/update`, `/delete`) process backend queries in the background and terminate into a definitive `redirect` state. This prevents duplicate form submissions upon user browser refresh calls.

---

## 🏃‍♂️ Initial Execution Sequence

1. Synchronize migrations and build target structures within your active backend database:

```bash
python manage.py makemigrations
python manage.py migrate

```

2. Start up the local development engine instance:

```bash
python manage.py runserver

```

3. Open your browser and point it to the dashboard address: `http://127.0.0.1:8000/shows`

```

```
