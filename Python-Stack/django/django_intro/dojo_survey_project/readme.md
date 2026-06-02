# Dojo Survey Application

This repository features a minimalist Django web application designed to capture user feedback via a structured multi-input form and display the collected parameters instantly on a localized results dashboard using standard Model-View-Template (MVT) request execution.

## Project Structure and Architecture

The application handles stateless web forms cleanly by processing data inside a direct request-response lifecycle:

- **`urls.py`**: Maps explicit structural endpoints (`/` and `/result`) to distinct controller methods.
- **`views.py`**: Validates inbound HTTP POST payloads, extracts form submission attributes safely, and binds variables directly into the template context stream.
- **`templates/index.html`**: Renders a standard Bootstrap 5 user registration form protected against cross-site vulnerabilities.
- **`templates/result.html`**: Receives context variables and presents the compiled submission details cleanly using custom styling properties.

---

## Technical Implementations

### 1. Frontend Form Component (`index.html`)

The entry form leverages Bootstrap utility boundaries and enforces input validation rules. It explicitly binds form parameters (`name`, `location`, `favorite_language`, `comment`) to corresponding backend variable keys using secure structural `name` attributes. It is fully integrated with Django's built-in static asset configuration rules.

### 2. Frontend Results Dashboard (`result.html`)

The submission results dashboard relies on template variable injection nodes (e.g., `{{ name }}` and `{{ location }}`) to securely output backend context dictionary data inside clean span containers linked to custom stylesheet definitions.

### 3. Backend Architecture (`views.py` & `urls.py`)

The backend safely validates inbound state methods. Instead of utilizing temporary server databases or active cache sessions, it captures the raw dictionary payload from `request.POST` using secure `.get()` operations and renders the results page directly (`Direct Rendering Workflow`), maximizing performance for sessionless forms.

If an unauthorized user attempts to access the `/result` URL directly via an invalid GET request, the controller securely intercepts the transaction and triggers an absolute redirect back to the central form instance.

---

## Core Django Routing Concepts Demonstrated

- **Direct Template Rendering**: Minimizes database read/write tasks by mapping context parameters straight into a matching layout file without reliance on active server sessions.
- **CSRF Protection**: Seamlessly enforces cross-site scripting guards (`{% csrf_token %}`) inside structural post-submission streams.
- **Multi-Conditional Method Isolation**: Explicitly captures state methods (`request.method == "POST"`) to separate initial template rendering runs from action processing routines.
