# Secure User Authentication System - Django Project

A highly secure, robust Django user authentication engine implementing complete **Registration and Login** architectures. Featuring comprehensive multi-tier data cleaning, cryptographic password hashing, age gating restrictions, and session-backed state retention designed to eliminate form wipeouts during validation faults.

---

## 🚀 Architectural Features

- **Dual-Form Dashboard (`/`)**: A unified, responsive user interface separating Registration and Login workflows side-by-side using Bootstrap 5.
- **Cryptographic Security**: Enforces zero plain-text leaks by cryptographically salting and hashing credentials using **`bcrypt`** before database storage.
- **Session-Backed State Retention**: Prevents tedious user form re-entry. If a submission triggers a validation fault, prior valid inputs are temporarily mapped to `request.session` variables, keeping fields pre-populated on redirect.
- **Post/Redirect/Get (PRG Pattern)**: Form submissions are processed as isolated background tasks that always resolve into a distinct redirect state, blocking duplicate submissions or unexpected error duplication during browser updates.
- **Strict Gatekeeping (Login Wall)**: Protects downstream authenticated routes (`/success`) by checking session state configurations; unauthenticated visitors are auto-routed back to the home layout.

---

## 🛡️ Data Validation Engine & Guardrails

This project leverages a custom validation pipeline via an extended `UserManager(models.Manager)` to secure data input:

### 📝 Registration Guardrails

- **Name Constraints**: Both `first_name` and `last_name` must contain a minimum of 2 structural, non-whitespace characters (enforced via `.strip()`).
- **Format-Compliant Email Parsing**: Validates syntax against a strict Regular Expression pattern to guarantee legitimate address structures (`example@domain.com`).
- **Uniqueness Constraints (Ninja Bonus)**: Direct database scanning calls (`self.filter(email=email).exists()`) explicitly reject duplicate emails.
- **Password Architecture**: Mandates an 8-character structural minimum. Explicitly confirms a strict character match against the secondary validation confirmation input (`confirm_password`).
- **Chronological Check (Ninja Bonus)**: Evaluates input birthday strings to verify the timestamp rests safely in the past.
- **Age-Gate Enforcement (Sensei Bonus)**: Evaluates structural leap-year variables and month configurations to mathematically confirm the registering user is **at least 13 years old**.

### 🔑 Login Guardrails

- **Presence Checking**: Ensures required fields are not submitted blank.
- **Encrypted Verification**: cross-references the targeted email with current database indices, securely evaluating input strings against the hashed record via `bcrypt.checkpw()`.

---

## 💾 Database Schema Mapping (Models)

The entity relationships and schema rules are defined as follows:

```python
from django.db import models

class UserManager(models.Manager):
    def register_validator(self, post_data):
        # Multi-tier registration safety validations
        pass

    def login_validator(self, post_data):
        # Multi-tier login verification routines
        pass

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

```

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method | Route URL   | View Function    | Description                                                                                             |
| ----------- | ----------- | ---------------- | ------------------------------------------------------------------------------------------------------- |
| **GET**     | `/`         | `views.index`    | Renders the primary registration and login panel with active context variables.                         |
| **POST**    | `/register` | `views.register` | Validates payloads, handles password hashing, creates user accounts, and initialises the session state. |
| **POST**    | `/login`    | `views.login`    | Audits login details, verifies hashed values, and sets the active session block.                        |
| **GET**     | `/success`  | `views.success`  | **Protected Dashboard Area**. Accessible only if `user_id` exists in the active session.                |
| **GET**     | `/logout`   | `views.logout`   | Clears the current session dictionary via `.flush()` and routes back to the root landing screen.        |

---

## 📁 Workspace Structural Configurations

Ensure your repository layout reflects the following file hierarchy:

```text
login_register_proj/
│
├── login_register_app/
│   ├── templates/
│   │   ├── index.html        # Central Authorization Panel (Dual Form Layout)
│   │   └── success.html      # Protected Authenticated Welcome Dashboard
│   ├── models.py             # Contains UserManager and User Model with Date-parsing
│   ├── urls.py               # Route Registry Mapping
│   └── views.py              # Contains Auth Processing and Security Checks

```

---

## 🏃‍♂️ Setup & Local Execution Sequence

1. Clone or clone the file tree down into your local environment workspace.
2. Initialize your local terminal engine and install required third-party crypt-security libraries:

```bash
pip install bcrypt

```

3. Generate and synchronize target table structures inside the database system:

```bash
python manage.py makemigrations
python manage.py migrate

```

4. Boot up the local development engine instance:

```bash
python manage.py runserver

```

5. Direct your active web browser to: `http://127.0.0.1:8000/`

```

```
