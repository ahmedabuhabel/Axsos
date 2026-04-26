# Flask Routing Demo App

A simple web application built with Flask to demonstrate basic routing, dynamic URL parameters, and custom error handling.

---

## 🚀 Features

- Basic route handling (`/`, `/champion`)
- Dynamic routes with parameters (`/say/<name>`, `/repeat/<num>/<name>`)
- Type-safe URL parameters using `<int:num>`
- Custom 404 error handler
- Debug mode enabled for development

---

## 📁 Project Structure

```

.
├── app.py
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

## 🌐 Available Routes

### 1. Home Route

```
GET /
```

Response:

```
Hello World!
```

---

### 2. Champion Route

```
GET /champion
```

Response:

```
Champion!
```

---

### 3. Say Hello (Dynamic)

```
GET /say/<name>
```

Example:

```
/say/Ahmed
```

Response:

```
Hi Ahmed!
```

---

### 4. Repeat Name (Dynamic with Integer)

```
GET /repeat/<int:num>/<name>
```

- `num` must be an integer
- `name` is a string

Example:

```
/repeat/3/Ahmed
```

Response:

```
Ahmed Ahmed Ahmed
```

---

## ⚠️ Error Handling

### Custom 404 Page

If a route is not found, the app returns:

```
No response
```

With HTTP status code:

```
404
```

---

## 🧠 Notes

- `<int:num>` ensures only integers are accepted in the `/repeat` route
- Invalid URLs like `/repeat/abc/test` trigger the 404 handler
- Debug mode (`debug=True`) is for development only

---

## 📌 Example Test URLs

```
http://127.0.0.1:5000/
http://127.0.0.1:5000/champion
http://127.0.0.1:5000/say/Ali
http://127.0.0.1:5000/repeat/5/Ali
http://127.0.0.1:5000/unknown-route
```
