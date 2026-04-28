# Flask Checkerboard App

A dynamic web application built with Flask that generates a customizable checkerboard grid using HTML, CSS, and JavaScript.

---

## 🚀 Features

- Dynamic checkerboard generation
- Adjustable rows and columns via URL
- Customizable colors
- Jinja2 template rendering
- JavaScript-based DOM generation
- Custom 404 error handling

---

## 📁 Project Structure

```

.
├── chekboard.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
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

Server will run at:

```
http://127.0.0.1:5000/
```

---

## 🌐 Routes & Usage

### 1. Default Board

```
/
```

- 8 rows × 8 columns
- Colors: black & white

---

### 2. Custom Columns

```
/<columns>
```

Example:

```
/10
```

- 8 rows × 10 columns

---

### 3. Custom Rows & Columns

```
/<rows>/<columns>
```

Example:

```
/6/12
```

- 6 rows × 12 columns

---

### 4. Full Customization

```
/<rows>/<columns>/<color1>/<color2>
```

Example:

```
/8/8/red/blue
```

- 8×8 board
- Colors: red & blue

---

## 🧠 How It Works

### Backend (Flask)

- Handles routing and parameters from URL
- Passes data to template using `render_template`

```python
return render_template(
    "index.html",
    rows=rows,
    columns=columns,
    color1=color1,
    color2=color2
)
```

---

### Frontend (HTML + Jinja2)

- Injects variables into JavaScript:

```html
<script>
  const rows = {{ rows }};
  const columns = {{ columns }};
  const color1 = "{{ color1 }}";
  const color2 = "{{ color2 }}";
</script>
```

---

### JavaScript (Dynamic Grid)

- Creates the checkerboard dynamically:

```javascript
for (let i = 0; i < rows; i++) {
  for (let j = 0; j < columns; j++) {
    if ((i + j) % 2 === 0) {
      // color1
    } else {
      // color2
    }
  }
}
```

- Uses `(i + j) % 2` to alternate colors

---

## ⚠️ Error Handling

- Any invalid route returns:

```
No response
```

- HTTP Status Code: `404`

---

## 📌 Example URLs

```
http://127.0.0.1:5000/
http://127.0.0.1:5000/10
http://127.0.0.1:5000/5/7
http://127.0.0.1:5000/8/8/green/yellow
```

---

## 🎨 Notes

- Colors must be valid CSS values (e.g., `red`, `blue`, `#ff0000`)
- Grid is generated entirely in JavaScript
- Flask is used only to pass configuration values

---
