# Django Blogs Routing & Views Project

This repository contains a collection of Django URL paths and their corresponding View implementations. The project covers essential web development routing patterns including dynamic parameter matching (`<int:number>`), state redirects, JSON data responses, and multi-endpoint mapping mimicking a standard RESTful architecture.

## Project Structure and Architecture

To run or review these routes, the implementation follows Django's clean separation of concerns:

- **`urls.py`**: Handles incoming URL pattern matching, structural priorities, and path extractions.
- **`views.py`**: Houses the logic methods responsible for building and returning raw HTTP responses, triggers, or serialized data back to the client browser.

---

## Routes and Implementations

### Q1: Root Path Redirect

Automatically triggers a redirect when a user hits the base domain, safely forwarding their browser instance directly to the primary blog timeline.

```python
def root_method(request):
    return redirect("/blogs/")

```

```python
path("", views.root_method)

```

### Q2: Blogs Index Listing

Displays a placeholder string intended to later accommodate the database query loop that pulls and renders all published blog records.

```python
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

```

```python
path("blogs/", views.index)

```

### Q3: New Blog Form Entry

Renders a temporary template instruction placeholder where the HTML creation form interface will be served to content creators.

```python
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

```

```python
path("blogs/new", views.new)

```

### Q4: Create Operation Action

Acts as the endpoint for processing form submissions. Once data processing concludes, it initiates an absolute redirect back to the central index view.

```python
def create(request):
    return redirect("/blogs/")

```

```python
path("blogs/create", views.create)

```

### Q5: Dynamic Blog Content Display

Uses integer path converters to trap unique resource IDs directly from the request URI, passing them cleanly into the execution view to query specific entries.

```python
def show(request, number):
    return HttpResponse(f"placeholder to display blog {number}")

```

```python
path("blogs/<int:number>", views.show)

```

### Q6: Dynamic Blog Edit Interface

Captures the targeted entity identifier via an active path string to target a specific record, preparing the text baseline for a modification workflow.

```python
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

```

```python
path("blogs/<int:number>/edit", views.edit)

```

### Q7: Destroy Resource Event

Processes a structural deletion command tied to an explicit numeric identifier, cleanly resetting the navigation context with a root-level redirect.

```python
def destroy(request, number):
    return redirect("/blogs/")

```

```python
path("blogs/<int:number>/delete", views.destroy)

```

### Q8: Structured API JSON Response

Bypasses basic raw string streams to return a structured JSON response object holding operational key-value metadata pairs (`title` and `content`).

```python
def response(request):
    return JsonResponse(
        {
            "title": "My First Blog Post",
            "content": "This is the content of the blog post placeholder.",
        }
    )

```

```python
path("blogs/json", views.response)

```

---

## Core Django Routing Concepts Demonstrated

- **Dynamic Path Converters**: Utilized across `Q5`, `Q6`, and `Q7` (`<int:number>`) to successfully trap variable components from structural URL endpoints and forward them as parameters to backend methods.
- **Response Architecture Differentiation**: Showcases both standard text-wrapped `HttpResponse` cycles alongside structured, machine-readable `JsonResponse` formats designed for API consumption.
- **Client-Side State Redirects**: Integrates explicit `redirect()` triggers to efficiently steer client browser workflows back into stable target pathways after structural events occur.
