# Counter Application

A simple **Flask** web application that demonstrates the use of **Sessions** to track user activity. The app maintains a page visit counter and a customizable interaction counter, illustrating the **Post/Redirect/Get** pattern and state persistence in a stateless HTTP environment.

## Features

- **Visit Tracking**: Tracks how many times the user has loaded the home page.
- **Custom Counter**: A secondary counter that can be manipulated by the user.
- **Incremental Controls**:
  - Increment the counter by 2.
  - Increment by a custom amount provided via a form.
- **Reset & Clear**:
  - **Reset**: Sets the counter back to zero while maintaining visit history.
  - **Destroy Session**: Clears all session data (including visit history) and starts fresh.

---

## Technical Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5 (Jinja2 Templates)
- **State Management**: Flask Sessions (signed cookies)

---

## Project Structure

```text
counter/
│
├── server.py           # Flask application logic and routing
├── templates/
│   └── index.html      # Main user interface
└── README.md           # Project documentation
```

---

## How to Run

1.  **Clone the repository** or copy the files.
2.  **Install Flask**:
    ```bash
    pip install Flask
    ```
3.  **Run the server**:
    ```bash
    python server.py
    ```
4.  **Access the app**: Open your browser and go to `http://localhost:5000`.

---

## Key Concepts Demonstrated

### 1. The Stateless Nature of HTTP

Every request from the browser is independent. Without a mechanism like **Sessions**, the server would "forget" the user as soon as a page is loaded or a redirect occurs.

### 2. Flask Sessions

This app uses `session` to store data in a secure, signed cookie. This allows the `visits` and `count` variables to persist across multiple requests and redirects.

### 3. Post/Redirect/Get Pattern

When the user submits a form (like adding a custom amount), the app processes the `POST` request and then issues a `redirect`. This prevents the "Confirm Form Resubmission" warning if the user refreshes the page.

---

## Security Note

The `app.secret_key` is used to sign the session cookies. In a production environment, this should be a complex, random string stored in an environment variable rather than hardcoded in the script.

```

```
