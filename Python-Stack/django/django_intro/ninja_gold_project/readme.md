# Django Ninja Gold Game (Refactored Edition)

A dynamic web-based strategy game built with **Django** that processes resource collection and state persistence. This edition utilizes **Database-Backed Sessions** to maintain the player's chronological activity log, featuring custom contextual HTML rendering and a streamlined **URL Parameter Route Matrix** instead of traditional hidden inputs.

## Features

- **URL-Driven Location Routing (Ninja Bonus)**: Decouples form payload sizes by passing destination endpoints (`farm`, `cave`, `house`, `quest`) directly as parameters within the HTTP POST action routing stream.
- **Dynamic Risk Matrix**:
  - **Farm**: Generates between 10 and 20 gold.
  - **Cave**: Accumulates between 5 and 10 gold.
  - **House**: Interaction yields between 2 and 5 gold.
  - **Quest**: Introduces a pursuit matrix where players can either win up to 50 gold or face a penalty payout of up to 50 gold.
- **Reverse-Chronological Activity Log**: Inserts structural activity payloads at the front-end position (`Index 0`) of the native storage array, ensuring that the most recent transactional update renders at the absolute top of the viewport.
- **Traditional Structural Layout Guards**: Implements explicit `{% if %}` conditional block evaluations within the template wrapper to cleanly isolate empty-state fallbacks from active transaction tracking logs.

---

## Technical Stack

- **Backend**: Python 3.x, Django 6.x
- **Frontend**: HTML5, Django Template Engine, CSS3
- **State Management**: Django Sessions (Secure, server-side database storage tied to a client-side Session ID cookie)

---

## Project Structure

```text
ninja_gold_project/
│
├── ninja_gold_project/   # Project configuration directory (settings.py, urls.py)
├── gold_app/             # Core application directory
│   ├── templates/
│   │   └── index.html    # Main game layout with explicit structural logic blocks
│   └── views.py          # State controllers, location routers, and stack insertions
├── manage.py             # Django management script
└── README.md             # Project documentation
How to Run
Apply Database Migrations (Crucial for initializing the mandatory django_session storage table):

Bash
python manage.py migrate
Run the application server:

Bash
python manage.py runserver
Play the game: Open your browser and navigate to http://127.0.0.1:8000.

Key Concepts & Code Architecture Demonstrated
1. URL Parameter Processing (Sessionless Payloads)
Forms bypass standard multi-input structures. Instead, the application binds the targeted zone explicitly inside the form's action URI attribute:

HTML
<form action="/process_money/farm" method="post">
The application sub-router maps this variable parameter instantly inside urls.py via path('process_money/<str:location>', views.process_money), eliminating hidden structural input elements from the DOM tree.

2. Reverse Array Stack Insertion
To enforce an active real-time dashboard design where newly generated events appear at the absolute top of the user interface, the controller targets position zero explicitly during array runtime allocation:

Python
current_activities.insert(0, {'text': activity_text, 'class': style_class})
3. Explicit Template Condition Isolation
Rather than using automatic empty fallback defaults, the interface handles state presentation through explicit boolean evaluations of the passed context array list variables:

HTML
{% if activities %}
    {% for activity in activities %}
        <p>{{ activity.text }}</p>
    {% endfor %}
{% else %}
    <p>No activities yet. Start hunting for gold!</p>
{% endif %}
This guarantees strict layout control by clearly isolating initial zero-state interface frames from live multi-element rendering blocks.
```
