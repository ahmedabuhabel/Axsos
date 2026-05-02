# Great Number Game

A simple web-based guessing game built with **Flask**. The server selects a random number between 1 and 100, and the user tries to guess it. The application demonstrates the use of **Sessions** for state management and the **Post/Redirect/Get** pattern to handle form submissions.

## Features

- **Random Number Generation**: A target number is generated and stored in the session when the user first visits.
- **Feedback System**:
  - Displays **"Too High!"** in a red box if the guess is above the target.
  - Displays **"Too Low!"** in a red box if the guess is below the target.
  - Displays the **Correct Number** in a green box when the user guesses correctly.
- **Session Persistence**: The game "remembers" the target number and the previous result even if the page is refreshed.
- **Play Again**: A reset button appears only after a correct guess to clear the session and start a new game.

---

## Technical Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, Jinja2 Templates, CSS3
- **State Management**: Flask Sessions (signed cookies)

---

## Project Structure

```text
great_number_game/
│
├── server.py           # Flask application logic and session handling
├── static/
│   └── style.css       # Custom styling for the game UI
├── templates/
│   └── index.html      # Main game interface with conditional Jinja2 logic
└── README.md
```

---

## How to Run

1.  **Install Flask**:

````bash
    pip install Flask
    ```
2.  **Run the application**:
    ```bash
    python server.py
    ```
3.  **Play the game**: Open your browser and navigate to `http://localhost:5000`.

---

## Key Logic Explained

### Session Management
The application uses Flask's `session` object to bridge the gap between stateless HTTP requests:
*   `session["random_number"]`: Stores the target value.
*   `session["res"]`: Stores the feedback message string.
*   `session["color"]`: Stores the CSS background color for the result box.

### Post/Redirect/Get (PRG)
When a guess is submitted via the `/guess` route (POST), the server updates the session data and then performs a `redirect("/")`. This ensures that refreshing the page does not re-submit the user's guess, maintaining a clean user experience.

### Conditional Rendering
Using Jinja2, the "Play Again" button and the result box are rendered conditionally:
```html
{% if session['res'] %}
    <!-- Box displays only if a guess has been made -->
{% endif %}
````

```

```
