# Django Multiple Apps Architecture Project

A modular Django web application demonstrating web ecosystem partitioning by constructing and deploying three independent backend apps (`blogs`, `surveys`, and `users`) within a centralized single-project infrastructure. This architecture models professional freelance development, allowing key modular components to be plugged out and reused easily across future technical implementations.

## Project Structure and Routing Architecture

The project splits traffic routing streams sequentially. Initial prefixes are parsed at the project level, transferring sub-route handling to the matching app container:

- **`blogs/`** (`blogs_app`): Manages general content workflows, dynamic parameterized entry lookups, and deletion routing.
- **`surveys/`** (`surveys_app`): Collects localized feedback parameters and configuration pathways.
- **`users/`** (`users_app`): Coordinates stateless authentication boundaries (`/register`, `/login`, `/users`).

---

## Endpoint Routings & URL Manifest

### 1. Blogs Application (`/blogs`)

- **`GET /` (Root Alternative)**: Triggers the main blog compilation stream _(Ninja Bonus implementation)_.
- **`GET /blogs`**: Displays a placeholder listing structural logs of all published records.
- **`GET /blogs/new`**: Renders placeholder configuration maps to add a new post layout.
- **`POST /blogs/create`**: Seamlessly intercepts form data and executes a clean HTTP redirect loop back to `/blogs`.
- **`GET /blogs/<number>`**: Dynamically captures URL route parameters to isolate specific record lookups (`placeholder to display blog number: <number>`).
- **`GET /blogs/<number>/edit`**: Renders custom editing dashboards tailored to target record variables.
- **`POST /blogs/<number>/delete`**: Intercepts structural deletion calls and redirects safely back to `/blogs`.

### 2. Surveys Application (`/surveys`)

- **`GET /surveys`**: Displays a central layout log for tracking generated user research frameworks.
- **`GET /surveys/new`**: Returns a placeholder template schema letting end-users inject new questionnaire designs.

### 3. Users Application (Root Context `/`)

- **`GET /register`**: Formats registration parameters to allow profile entry creations.
- **`GET /users/new`**: Maps explicitly to the **same exact controller method** handling the registration endpoint to maximize structural logic reuse.
- **`GET /login`**: Displays standard user access and security validation placeholders.
- **`GET /users`**: Lists the baseline context manifest containing recorded system profile listings.

---

## Technical Implementations

### Project Main Router (`project_name/urls.py`)

Configured with open-ended string matching controls to map specialized sub-applications while allowing root-level direct routes to capture specific system behaviors cleanly:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("surveys/", include("surveys.urls")),
    path("", include("users.urls")),  # Catches root-level /register and /login directly
    path("", include("blogs.urls")),  # Ninja Bonus: Forwards absolute base root hits to blogs
]

```

### Shared Logic Execution (`users/urls.py` & `views.py`)

Demonstrates target routing parameters where alternative URL routes point to a shared monolithic controller method without causing execution loops:

```python
# users/urls.py
urlpatterns = [
    path('register', views.register),
    path('users/new', views.register),  # Reuses same method as /register
]

```

---
