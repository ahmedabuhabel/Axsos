# Semi-Restructured TV Shows Manager - Django Project

A robust Django web application that implements complete **CRUD (Create, Read, Update, Delete)** operations to manage a television network showcase directory. Built with advanced server-side asynchronous-ready validations, dynamic data parsing, session-backed state preservation, and a responsive **Bootstrap 5** user interface.

---

## 🚀 Features

* **Create**: Dedicated validation input panel to seamlessly inject new shows with proper datetime configurations (`/shows/new`).
* **Read**: 
  * Comprehensive dashboard index roster tracking all sub-entries within a central datatable (`/shows`).
  * Isolated individual profiles displaying exhaustive metadata for a specific series (`/shows/<id>`).
* **Update**: Pre-populated contextual edit forms with automated formatting pipes to safely override current database records (`/shows/<id>/edit`).
* **Delete**: Direct cascading deletion handlers to purge unwanted indices from the filesystem instantly.

---

## 💾 Database Schema Mapping (Models)

The architecture maps out entity requirements via Django's persistent object-relational abstraction layer, managed by a custom advanced validation manager:

```python
from django.db import models

class ShowsManager(models.Manager):
    def basic_validator(self, post_data, show_id=None):
        # Advanced Multi-tier Server Side Validation logic resides here
        pass

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowsManager()

```

---

## 🛡️ Robust Validation & Edge Case Fixes (New Updates!)

This project implements advanced business-logic guardrails through a customized `ShowsManager()` to ensure complete database integrity:

1. **Title Uniqueness (SENSEI BONUS)**: Evaluates input parameters to guarantee that duplicate records cannot be generated during creation.
2. **Context-Aware Exclusions**: The validation routine dynamically detects whether the execution state is an **Insertion** or an **Update**. During updates (`/update`), it utilizes `.exclude(id=show_id)` to prevent the model from triggering false-positive uniqueness flags against its own current record.
3. **Chronological Enforcement (Release Date)**: Parses input text elements into functional Python native dates using `datetime.strptime()` and mathematically verifies that the asset insertion date rests securely in the past (`converted_date >= date.today()`).
4. **Flexible Text Constraints (Description)**: Enforces string filtering via `.strip()`. The field allows a perfectly clean empty payload, but strictly mandates a minimum of 10 structural characters if data is provided.

---

## 🧠 Session-Backed State Retention & PRG Pattern

To enhance User Experience (UX) and circumvent standard web lifecycle vulnerabilities, the application employs a combined **Post/Redirect/Get (PRG)** and temporary state mapping layout:

* **No Form Wipeouts**: If server-side validation checks fail, all legal data parameters are securely cached into `request.session` dictionaries before initiating standard routing changes.
* **Flawless Memory Cleansing (`.pop()`)**: Views rendering user entry forms query cached session keys via `.pop()`. This immediately loads old user data state back into the HTML input variables, while instantly destroying the session cache.
* **Anti-Duplication Shield**: Because failed state forms exit via `redirect` rather than `render`, browser execution environments **cannot duplicate error messages or form submissions** if a user manually refreshes the browser page.

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method | Route URL | View Function | Description |
| --- | --- | --- | --- |
| **GET** | `/` | `views.index` | Root route. Re-routes incoming traffic to `/shows`. |
| **GET** | `/shows` | `views.shows_index` | Renders the primary dashboard table displaying all shows. |
| **GET** | `/shows/new` | `views.new` | Renders creation form canvas filled with popped session states. |
| **POST** | `/shows/create` | `views.create` | Performs uniqueness/past-date validation checks and inserts new records. |
| **GET** | `/shows/<int:show_id>` | `views.show` | Displays comprehensive attributes for a single series. |
| **GET** | `/shows/<int:show_id>/edit` | `views.edit` | Renders the edit layout with combined DB/popped fallback validation states. |
| **POST** | `/shows/<int:show_id>/update` | `views.update` | Validates data modifications, excluding its own entry ID from duplicate checks. |
| **POST/GET** | `/shows/<int:show_id>/delete` | `views.delete` | Purges the isolated row reference out of active memory. |

---

## 📁 Project Workspace Configuration

Ensure your physical layout replicates the following directory setup:

```text
tv_shows_project/
│
├── tv_shows_app/
│   ├── templates/
│   │   ├── index.html        # All Shows Roster View
│   │   ├── add_show.html     # Add New Show Entry Form (Session Safe)
│   │   ├── edit_show.html    # Edit Current Show Form (Exclusion Safe)
│   │   └── show.html         # Specific Show Inspection Panel
│   ├── models.py
│   ├── urls.py
│   └── views.py

```

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


3. Open your browser and point it to the dashboard address: `http://127.0.0.1:8000/`

```

```
