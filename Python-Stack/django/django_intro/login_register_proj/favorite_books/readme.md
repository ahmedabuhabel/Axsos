# Favorite Books Application (`favorite_books`)

A highly optimized Django application designed to catalog reading materials and manage peer crowdsourced user bookmarks. This subsystem mounts seamlessly alongside a core authentication module, delivering custom multi-relationship table binding, granular inline authorization tracking, and individual user aggregation dashboards.

---

## 🚀 Key Architectural Features

- **Multi-Relationship Entity Binding**: Establishes dual isolated tracking lanes between identical tables, enabling a single row to explicitly trace both ownership boundaries and communal preference bookmarks independently.
- **Inline Authorization Gatekeeping**: Evaluates runtime session variables to transform view states dynamically. Only the absolute creator of a book instance is granted permission to override attributes or invoke deletion protocols.
- **Smart Back-Navigation (`HTTP_REFERER`)**: Bookmark processing vectors instantly identify user origin headers to execute precise redirects, ensuring a smooth UX whether actions are executed from the main dashboard grid or isolated detail sheets.
- **Post/Redirect/Get (PRG Pattern)**: Form processing blocks for book insertions and modification matrices run strictly in background contexts to prevent data corruption or duplicate form entries upon browser refresh cycles.

---

## 🛡️ Validation Guardrails & Feature Upgrades

- **Catalog Input Validation**: Data passing into the creation worker must clear structural string checks—mandating an absolute book title presence and minimum string constraints for the description area.
- **Dynamic Main-Grid Bookmark Controls (Ninja Bonus)**: The principal dashboard roster scans user preference histories inline. If an item is already bookmarked, it displays a verified message along with an opt-out action hook; otherwise, it presents a single-click bookmark addition tool.
- **Isolated User Preference Ledger (Sensei Bonus)**: Houses a dedicated personal space (`/user/favorites`) that leverages high-speed reverse-relation query filters to pull and render a dedicated personal dashboard containing only the items you liked.

---

## 💾 Relational Database Schema Mapping (Models)

The entity topology utilizes **`related_name`** constraints to cleanly segregate the overlapping One-to-Many (`ForeignKey`) and Many-to-Many (`ManyToManyField`) data paths bound to the unified user directory:

1. **`uploaded_by` (One-to-Many)**: Maps the unique uploader who published the row. Accessible inversely via `user.books_uploaded.all()`.
2. **`users_who_like` (Many-to-Many)**: Maps the communal roster of matching bookmark fans. Accessible inversely via `user.liked_books.all()`.

```text
  ┌──────────────────────┐                 ┌──────────────────────┐
  │   login_app.User     │ ◄─────────────┐ │  favorite_books.Book │
  ├──────────────────────┤               │ ├──────────────────────┤
  │ id (PK)              │               └─┤ id (PK)              │
  │ first_name           │ ◄─────────────┐ │ title                │
  │ last_name            │  books_uploaded │ desc                 │
  └──────────────────────┘   (1-to-Many) │ │ uploaded_by_id (FK)  │
             ▲                           │ └──────────┬───────────┘
             │                           │            │
             │       liked_books         │            │ (Many-to-Many)
             └───────────────────────────┴────────────▼
                                   ┌──────────────────────┐
                                   │  * favorited table * │
                                   ├──────────────────────┤
                                   │ book_id (FK)         │
                                   │ user_id (FK)         │
                                   └──────────────────────┘
```

````

```python
from django.db import models
from login_app.models import User # Foreign app model reference

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    # Track ownership bounds
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)

    # Track communal bookmark clusters
    users_who_like = models.ManyToManyField(User, related_name="liked_books")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method | Route URL                | View Function           | Description                                                                                       |
| ----------- | ------------------------ | ----------------------- | ------------------------------------------------------------------------------------------------- |
| **GET**     | `/books`                 | `views.books_index`     | Main dashboard tracking global book assets and housing the custom creation panel.                 |
| **POST**    | `/books/create`          | `views.create_book`     | Validates input streams, registers the book asset, and automatically bookmarks it for the author. |
| **GET**     | `/books/<id>`            | `views.book_detail`     | Detailed metadata panel tracking full uploader specs, modification panels, and the fan roster.    |
| **POST**    | `/books/<id>/update`     | `views.update_book`     | Secures and processes textual asset modifications for authorized owners.                          |
| **POST**    | `/books/<id>/delete`     | `views.delete_book`     | Destroys the catalog instance permanently if uploader criteria checks pass.                       |
| **POST**    | `/books/<id>/favorite`   | `views.add_favorite`    | Binds the active session user to the target book asset inside the M2M table.                      |
| **POST**    | `/books/<id>/unfavorite` | `views.remove_favorite` | Severs the bookmark link for the active session user from the target book asset.                  |
| **GET**     | `/user/favorites`        | `views.user_favorites`  | **Sensei Bonus Area**. Renders an isolated collection tracking personal favorite books.           |

---

## 📁 Workspace App Tree

Ensure your application folder hierarchy strictly conforms to the layout below:

```text
favorite_books/
│
├── templates/
│   ├── books_index.html     # Main dashboard layout (Includes Ninja Bonus)
│   ├── book_detail.html     # Secure view/edit specs & fan rosters
│   └── user_favorites.html  # Personalized favorites compilation (Sensei Bonus)
├── models.py                # Interconnected schemas and validation managers
├── urls.py                  # Component path mappings
└── views.py                 # Core transactional logic controllers

```

```

```
````
