```markdown
# Flask Playground App

A simple Flask application that demonstrates passing parameters from the URL to an HTML template and rendering dynamic UI using Jinja2.

---

## 🚀 Features

- Dynamic routing with URL parameters
- Passing data from Flask (backend) to HTML (frontend)
- Rendering multiple elements using Jinja2 loops
- Dynamic styling using template variables (color)

---

## 📁 Project Structure
```

.
├── playground.py
├── templates
│ └── index.html
└── README.md

````

---

## ⚙️ Requirements

- Python 3.x
- Flask

Install Flask:

```bash
pip install flask
````

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

## 🌐 Usage

### Route

```
/play/<num>/<color>
```

### Parameters

- `num` → number of boxes
- `color` → CSS color value

---

## 🔍 Example

```
http://127.0.0.1:5000/play/5/red
```

### Result

- Displays **5 boxes**
- Each box has **red background color**

---

## 🧠 How It Works

### Backend (Flask)

```python
@app.route("/play/<num>/<color>")
def hello_world(num=3, color="blue"):
    num = int(num)
    return render_template("index.html", count=num, color=color)
```

- Receives `num` and `color` from URL
- Converts `num` to integer
- Passes values to template

---

### Frontend (Jinja2 Template)

```html
{% for i in range(count) %}
<div class="box"></div>
{% endfor %}
```

- Generates boxes dynamically based on `count`

```html
background-color: {{ color }};
```

- Applies dynamic color from URL

---

## ⚠️ Notes

- `num` must be a valid number (otherwise the app will crash unless handled)
- `color` must be a valid CSS color (e.g., `red`, `blue`, `#ff0000`)
- Ensure `index.html` is inside a `templates` folder (required by Flask)

---

## 📌 Example URLs

```
http://127.0.0.1:5000/play/3/blue
http://127.0.0.1:5000/play/10/green
http://127.0.0.1:5000/play/6/#ff5733
```

---

```

```
