# Django Great Number Game

A simple web-based guessing game built with **Django**. The server selects a random number between 1 and 100, and the user tries to guess it. The application demonstrates the use of **Database-Backed Sessions** for state management, secure form routing, and the **Post/Redirect/Get** pattern to handle form submissions seamlessly.

## Features

- **Random Number Generation**: A target number is securely generated and stored in the server-side session when the user first visits.
- **Feedback System**:
  - Displays **"Too High!"** in a red box if the guess is above the target.
  - Displays **"Too Low!"** in a red box if the guess is below the target.
  - Displays the **Correct Number** in a green box when the user guesses correctly.
- **Session Persistence**: The game "remembers" the target number and the previous result even if the page is refreshed without manual resubmission alerts.
- **Play Again**: A reset button appears only after a correct guess to completely flush the session and start a new game with a fresh random number.

---

## Technical Stack

- **Backend**: Python 3.x, Django 6.x
- **Frontend**: HTML5, Django Template Engine, CSS3
- **State Management**: Django Sessions (Secure, server-side database storage tied to a client-side Session ID cookie)

---

## Project Structure

```text
number_game_project/
│
├── number_game_project/  # Project configuration directory (settings.py, urls.py)
├── game_app/             # Core application directory
│   ├── templates/
│   │   └── index.html    # Main game interface with conditional Django template logic
│   └── views.py          # Django application logic and session handling
├── static/
│   └── style.css         # Custom styling for the game UI
├── manage.py             # Django management script
└── README.md             # Project documentation

```

---

## How to Run

1. **Apply Database Migrations** (Crucial for initializing the mandatory `django_session` storage table):

```bash
python manage.py migrate

```

2. **Run the application**:

```bash
python manage.py runserver

```

3. **Play the game**: Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Key Logic Explained

### Server-Side Session Management

Unlike Flask, which stores raw signed data inside browser cookies (client-side), Django utilizes an explicit server-side abstraction layer. It stores the transactional game state directly inside the local database (`db.sqlite3`), issuing a unique hashed identifier cookie (`sessionid`) to the client browser:

- `request.session["random_number"]`: Stores the target value securely on the backend.
- `request.session["res"]`: Stores the feedback message string.
- `request.session["color"]`: Stores the CSS background color for the result box.

### Absolute CSRF Security Validation

Django explicitly forces Cross-Site Request Forgery security checks via the `{% csrf_token %}` template modifier inside the guessing form, preventing unauthorized external state-changing inbound requests.

### Post/Redirect/Get (PRG)

When a guess is submitted via the `/guess` route (POST), the server updates the `request.session` data and then performs a `redirect("/")`. This ensures that refreshing the page does not re-submit the user's guess, maintaining a clean user experience and avoiding duplicate transaction errors.

### Conditional Rendering

Using the Django Template Engine, the "Play Again" button, guess input fields, and the result box are rendered conditionally based on the context variables extracted from the session:

```html
{% if res %} {% if "was the number" in res %} {% endif %} {% endif %}
```

```

```
