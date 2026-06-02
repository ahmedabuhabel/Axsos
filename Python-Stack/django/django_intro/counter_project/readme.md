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
