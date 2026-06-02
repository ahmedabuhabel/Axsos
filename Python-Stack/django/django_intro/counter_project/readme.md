# Django Counter Application

A simple **Django** web application that demonstrates the use of **Database-Backed Sessions** to track user activity. The app maintains a page visit counter and a customizable interaction counter, illustrating the **Post/Redirect/Get** pattern and state persistence in a stateless HTTP environment.

## Features

- **Visit Tracking**: Tracks how many times the user has loaded the home page.
- **Custom Counter**: A secondary counter that can be manipulated by the user.
- **Incremental Controls**:
  - Increment the counter by 2.
  - Increment by a custom amount provided via a form.
- **Reset & Clear**:
  - **Reset**: Sets the counter back to zero while maintaining visit history.
  - **Destroy Session**: Clears all session data (including visit history) from both the database and client-side cookies to start fresh.

---

## Technical Stack

- **Backend**: Python 3.x, Django 6.x
- **Frontend**: HTML5 (Django Template Engine)
- **State Management**: Django Sessions (secure, server-side database storage tied to a client-side Session ID cookie)

---

## Project Structure

```text
counter_project/
│
├── counter_project/      # Project configuration directory (settings.py, urls.py)
├── counter_app/          # Core application directory (views.py)
│   └── templates/
│       └── index.html    # Main user interface
├── manage.py             # Django management script
└── README.md             # Project documentation

```

---

## How to Run

1. **Clone the repository** or copy the files.
2. **Apply Database Migrations** (Crucial for initializing the mandatory `django_session` storage table):

```bash
python manage.py migrate

```

3. **Run the server**:

```bash
python manage.py runserver

```

4. **Access the app**: Open your browser and go to `http://127.0.0.1:8000`.

---

## Key Concepts Demonstrated

### 1. The Stateless Nature of HTTP

Every request from the browser is independent. Without a mechanism like **Sessions**, the server would "forget" the user as soon as a page is loaded or a redirect occurs.

### 2. Django Server-Side Sessions

Unlike Flask which stores raw signed data inside browser cookies (client-side), Django utilizes an explicit server-side abstraction layer. It stores the transactional state directly inside the local database (`db.sqlite3`), issuing a unique hashed identifier cookie (`sessionid`) to the client browser for authentication.

### 3. Post/Redirect/Get Pattern

When the user submits a form (like adding a custom amount), the app processes the `POST` request and then issues an immediate HTTP `redirect`. This prevents the duplicate transaction errors and the "Confirm Form Resubmission" warning if the user refreshes the page.

### 4. Absolute CSRF Security Validation

Django explicitly forces Cross-Site Request Forgery security checks via the `{% csrf_token %}` template modifier on all active state-changing inbound requests, checking the legitimacy of the payload origin.

```

```
