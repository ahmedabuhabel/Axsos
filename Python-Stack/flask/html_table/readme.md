# Flask Users Table App

A simple Flask web application that displays a list of users in a styled table using Bootstrap and Jinja2 templating.

---

## 🚀 Features

- Render dynamic data using Flask
- Display users in a responsive table
- Use Jinja2 loops to iterate over data
- Generate full names dynamically
- Styled with Bootstrap

---

## 📁 Project Structure

```

.
├── html_table.py
├── templates/
│   └── index.html
└── README.md

```

---

## ⚙️ Requirements

- Python 3.x
- Flask

Install Flask:

```bash
pip install flask
```

---

## ▶️ Running the Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

## 🌐 Route

### Home Route

```
GET /
```

Displays a table of users.

---

## 🧠 How It Works

### Backend (Flask)

```python
@app.route("/")
def home():
    users = [
        {"first_name": "Michael", "last_name": "Choi"},
        {"first_name": "John", "last_name": "Supsupin"},
        {"first_name": "Mark", "last_name": "Guillen"},
        {"first_name": "KB", "last_name": "Tonel"},
    ]
    return render_template("index.html", users=users)
```

---

### Frontend (Jinja2 Template)

```html
{% for user in users %}
<tr>
  <th scope="row">{{ loop.index }}</th>
  <td>{{ user.first_name }}</td>
  <td>{{ user.last_name }}</td>
  <td>{{ user.first_name }} {{ user.last_name }}</td>
</tr>
{% endfor %}
```

---

## 🎨 UI Styling

Uses Bootstrap 5:

```html
<link
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
  rel="stylesheet"
/>
```

Table styling:

```html
<table class="table table-dark"></table>
```

---

## 📌 Example Output

| #   | First Name | Last Name | Full Name     |
| --- | ---------- | --------- | ------------- |
| 1   | Michael    | Choi      | Michael Choi  |
| 2   | John       | Supsupin  | John Supsupin |
| 3   | Mark       | Guillen   | Mark Guillen  |
| 4   | KB         | Tonel     | KB Tonel      |
