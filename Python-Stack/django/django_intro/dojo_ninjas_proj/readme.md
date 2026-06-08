# Dojos and Ninjas Manager - Django Project

A web application built with Python using the Django framework and styled with Bootstrap 5. This project manages a One-to-Many relationship between **Dojos** and **Ninjas** (where one Dojo can host multiple Ninjas).

## 🚀 Features

- **Add a Dojo:** Creates a new Dojo location with a name, city, state, and custom description.
- **Add a Ninja:** Cascades and assigns a new Ninja to an existing Dojo selected dynamically via a dropdown menu.
- **Display Structure:** Lists all created Dojos sequentially, showcasing their details alongside bulleted rosters of their respective assigned Ninjas.
- **Delete Dojo (Bonus Feature):** Provides a delete button for each Dojo, securely purging the Dojo record and automatically cascading data deletion to remove all its associated Ninjas.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.13+, Django 5.x
- **Frontend:** HTML5, Bootstrap 5 (via CDN)
- **Database Backend:** SQLite / MySQL via Django ORM

---

## 💾 Database Relationship Schema (Models)

The core mechanics of this task rely on the relationship built inside `models.py`:

```python
from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # The ForeignKey creates the One-to-Many relationship linking Ninjas to Dojos
    dojo = models.ForeignKey(Dojos, on_delete=models.CASCADE, related_name="ninjas")

```

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method | Route URL                    | Target View Function | Description                                                                                                                  |
| ----------- | ---------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **GET**     | `/`                          | `views.index`        | Renders the dashboard showing all Dojos, their respective Ninjas, and both input forms.                                      |
| **POST**    | `/create_dojo`               | `views.create_dojo`  | Processes new Dojo form information and saves it to the database.                                                            |
| **POST**    | `/create_ninja`              | `views.create_ninja` | Fetches the specific `Dojo` object instance using its submitted ID, instantiates a new Ninja object linked to it, and saves. |
| **POST**    | `/delete_dojo/<int:dojo_id>` | `views.delete_dojo`  | Removes a selected Dojo by its unique primary key `id` along with its linked Ninjas.                                         |

---

## 🏃‍♂️ How to Run and Initialize the Project Locally

### 1. Set up your Virtual Environment & Install Django

```bash
# Create the environment
python -m venv djangoPy3Env

# Activate environment (Mac/Linux)
source djangoPy3Env/bin/activate

# Activate environment (Windows)
djangoPy3Env\Scripts\activate

# Install requirements
pip install django

```

### 2. Prepare and Synchronize the Database Schema

Execute the migration scripts to build the appropriate tables for your Dojos and Ninjas apps.

```bash
python manage.py makemigrations
python manage.py migrate

```

### 3. Start the Development Server

```bash
python manage.py runserver

```

Visit `http://localhost:8000/` in your web browser to view your fully functional dashboard interface.

---

## 💡 Key Front-End Concept Implemented

The Ninja registration dropdown component enforces database integrity through clean interface specifications:

```html
<select name="dojo_id" class="form-select" required>
  <option value="" selected disabled>Select a Dojo</option>
  {% for dojo in all_dojos %}
  <option value="{{ dojo.id }}">{{ dojo.name }}</option>
  {% endfor %}
</select>
```

- `value=""` & `required`: Prevents form processing bugs by blocking invalid submissions.
- `selected disabled`: Keeps the placeholder clean and limits user interaction solely to valid database entry parameters.

```

```
