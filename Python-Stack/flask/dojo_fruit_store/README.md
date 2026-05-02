# Dojo Fruit Store

A Flask web application for a local fruit store where students can order fruits (Strawberries, Raspberries, and Apples). The application manages order processing, displays a gallery of available fruits by reading files from the server's directory, and tracks customer information.

## Features

- **Order Form**: A dynamic checkout system where users select fruit quantities and provide personal details (Name and Student ID).
- **Order Confirmation**: Displays a detailed summary of the order, including the total count of items and a timestamp.
- **Dynamic Fruit Gallery**: Automatically generates a gallery page by scanning the `static/img` folder for image files.
- **Responsive Design**: Built with Bootstrap for a clean, mobile-friendly user interface.

---

## Technical Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, Jinja2 Templates, Bootstrap 4
- **File System**: Python `os` module for dynamic image loading

---

## Project Structure

```text
fruit_store/
│
├── server.py           # Main Flask application and routing
├── static/
│   ├── css/
│   │   └── bootstrap.css
│   └── img/            # Store fruit images here (e.g., apple.jpg)
├── templates/
│   ├── index.html      # Main order form
│   ├── checkout.html   # Order success page
│   └── fruits.html     # Dynamic image gallery
└── README.md
```

---

## Installation and Setup

1.  **Install Flask**:

    ```bash
    pip install Flask
    ```

2.  **Prepare Directory**:
    Ensure you have a `static/img` directory and populate it with images of fruits (e.g., `apple.png`, `strawberry.jpg`).

3.  **Run the Server**:

    ```bash
    python server.py
    ```

4.  **Access the Application**:
    Navigate to `http://localhost:5000` in your web browser.

---

## Key Logic

### Dynamic Image Loading

The `/fruits` route utilizes `os.path` and `os.listdir` to fetch all filenames from the server's local storage. This allows the store to update its catalog by simply adding or removing files from the `img` folder without modifying the source code.

### Order Processing

The `/checkout` route receives data via a `POST` request, calculates the order details, and renders the `checkout.html` template. It captures:

- Fruit quantities (Strawberry, Raspberry, Apple).
- User data (First Name, Last Name, Student ID).
- Server-side logging of form data to the terminal for debugging.
