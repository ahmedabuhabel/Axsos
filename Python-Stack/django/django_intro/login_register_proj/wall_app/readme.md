# CodingDojo Wall (Social Feed Grid) - Django Project

A robust, enterprise-ready Django web application that models a responsive social networking micro-feed layout (akin to a Facebook news feed). This project seamlessly integrates a secure custom **Login/Registration authentication framework** with a dual-tier nested relational structure (**Messages ↔ Comments**) featuring secure author gatekeeping and complex time-gated deletion policies.

---

## 🚀 Key Architectural Features

- **Authenticated Route Gatekeeping (Login Wall)**: Protects the centralized feed directory (`/wall/`); any unauthenticated session access attempts automatically cascade back to the root landing dashboard (`/`).
- **Multi-Tier Relational Feed Grid**: Leverages a nested database mapping to display historical user messages, with each entry managing its own downstream thread of user comments.
- **Chronological Sorting Pipeline**:
  - Enforces an inverted timeline layout for primary messages, rendering the **most recent posts at the top** of the active feed block (`order_by('-created_at')`).
  - Enforces standard chronological ordering for sub-threads, displaying the **oldest comments at the top** of their respective parent message stacks first.
- **Post/Redirect/Get (PRG Pattern Enforcement)**: All active injection operations (`/post_message`, `/post_comment`) evaluate structures strictly in the background and terminate via an explicit redirect state. This safely guarantees that user browser updates (page refreshes) cannot duplicate submissions or trigger unexpected form errors.

---

## 🛡️ Validation Guardrails & Gated Access Controls

Advanced logical validation matrices and security blocks are integrated into custom object managers:

1. **Author Deletion Gatekeeping (Ninja Bonus)**: Restricts data removal actions. A user can explicitly view and click a `delete` reference hook **only** if their active session ID (`request.session['user_id']`) matches the primary user foreign key bound to that specific message instance.
2. **Temporal 30-Minute Access Gating (Sensei Bonus)**: The system dynamically computes time differentials using native Python `timezone` properties. A user is permitted to drop an asset instance **only if less than 30 minutes have elapsed** since the initial timestamp injection (`timezone.now() < created_at + timedelta(minutes=30)`).
3. **Empty Payload Prevention**: Both message and comment inputs undergo structural string scrubbing (`.strip()`) to reject whitespace-only submissions.

---

## 💾 Relational Database Schema Mapping (Models)

The object relational topology links three standalone structural entities across overlapping One-to-Many (`ForeignKey`) database vectors:

```text
  ┌────────────────┐               ┌────────────────┐
  │      User      │ ◄───────────┐ │    Message     │
  ├────────────────┤             │ ├────────────────┤
  │ id (PK)        │             └─┤ id (PK)        │
  │ first_name     │ ◄───────────┐ │ message        │
  │ last_name      │ (1-to-Many) │ │ user_id (FK)   │
  └────────────────┘             │ └───────┬────────┘
           ▲                     │         │
           │                     │         │ (1-to-Many)
           │ (1-to-Many)         │         ▼
           │                     │ ┌────────────────┐
           │                     │ │    Comment     │
           │                     │ ├────────────────┤
           └─────────────────────┴─┤ id (PK)        │
                                   │ comment        │
                                   │ user_id (FK)   │
                                   │ message_id (FK)│
                                   └────────────────┘

```

```python
from django.db import models
from login_app.models import User
from django.utils import timezone
from datetime import timedelta

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_be_deleted(self):
        # Sensei Bonus: Evaluates the 30-minute expiration countdown window
        return timezone.now() < self.created_at + timedelta(minutes=30)

class Comment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 🗺️ Application Routes (URL Endpoints)

### 🔑 Authentication App Endpoints (`login_app`)

- **GET** `/` : Renders the central registration and login dashboard panels.
- **POST** `/register` : Processes verification rules, applies cryptographic salts/hashes, and commits new users.
- **POST** `/login` : cross-references credentials using `bcrypt.checkpw` and constructs session hashes.
- **GET** `/logout` : Flushes active cookies via `.flush()` and routes back to the root entry screen.

### 📰 Social Feed App Endpoints (`wall_app`)

- **GET** `/wall/` : **Protected Core Route**. Renders the nested message feed grid.
- **POST** `/wall/post_message` : Processes and links a structural text message block to the logged-in user.
- **POST** `/wall/post_comment/<int:message_id>` : Creates a child comment block linked to a specific parent message.
- **POST** `/wall/delete_message/<int:message_id>` : Executes safe deletion operations if both authorship and the 30-minute time limits pass auditing checks.

---

## 📁 Workspace Structural Configurations

Ensure your project environment reflects the clean decoupled configuration detailed below:

```text
login_register_proj/
│
├── login_app/                 # Authentication System Application
│   ├── models.py              # User Schemas & Validation Logic
│   └── views.py               # Session Controllers & Cryptographic Storage
│
├── wall_app/                  # Social Interaction Engine Application
│   ├── templates/
│   │   └── wall.html          # Dynamic Feed, Threading UI & Action Hooks
│   ├── models.py              # Message/Comment Models & Time-Gating Methods
│   ├── urls.py                # Normalized /wall/ Sub-Route Indices
│   └── views.py               # Feed Aggregators & Permission Handlers
│
└── login_register_proj/       # Core Project Routing Base
    └── urls.py                # Main include() URLconf Registry

```

---

## 跑 🏃‍♂️ Setup & Local Execution Sequence

1. Open your localized CLI terminal and move down into the root folder hosting your project file layout.
2. Install the necessary cryptographic security dependencies:

```bash
pip install bcrypt

```

3. Run database migrations to construct the interconnected tables across your active database engine:

```bash
python manage.py makemigrations
python manage.py migrate

```

4. Fire up the localized Django development engine:

```bash
python manage.py runserver

```

5. Launch your browser window and navigate to the landing index address: `http://127.0.0.1:8000/`

```

```
