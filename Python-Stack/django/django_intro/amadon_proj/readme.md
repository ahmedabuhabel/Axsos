# Secure E-Commerce Shopping Cart (Amadon Store) - Django Project

A robust, defensively designed Django e-commerce proof-of-concept application named **Amadon Store**. This project demonstrates how to eliminate critical server-side vulnerabilities common in entry-level transactional systems—specifically preventing form-tampering price manipulation and duplicate credit card charges caused by browser refresh events.

---

## 🚀 Key Architectural Lessons Implemented

### 🛑 Lesson 1: Post/Redirect/Get (PRG Pattern) vs. Form Resubmission

- **The Vulnerability**: In standard pipelines, handling a POST payload and directly rendering a success HTML file leaves the endpoint exposed. If a user refreshes the confirmation page, the browser re-submits the transactional POST payload, resulting in duplicate database entries (and duplicate credit card charges).
- **The Defensive Fix**: The application handles form actions strictly on a background processing route (`/amadon/buy`) and immediately executes an HTTP redirect to a safe GET route (`/checkout`). Refreshing the checkout screen simply re-reads cached session data without re-triggering a purchase query.

### 🛡️ Lesson 2: Server-Side Price Verification vs. Front-End Trust

- **The Vulnerability**: Trusting price values sent from hidden inputs in HTML forms (`<input type="hidden" name="price" value="19.99">`) is highly insecure. Any user can use browser inspection tools to modify the price markup to `0.01` and purchase premium items for pennies.
- **The Defensive Fix**: The application form submits **only** a structural primary key link (`product_id`) and the desired quantity. The backend view queries the true, immutable price directly from the secure database, completely neutralizing client-side HTML tampering.

---

## 💾 Relational Database Schema Mapping (Models)

The application structures transactional metrics across two independent tracking tables inside `models.py`:

```python
from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

---

## 📊 Analytics & Aggregation Engine

When an item is securely purchased, the system calculates and preserves dynamic context variables for the checkout interface:

1. **Current Order Cost**: Multiplies the queried database product price by the verified quantity payload.
2. **Historical Items Count**: Loops through historical backend logs (`Order.objects.all()`) to sum up every single item ordered across all historical store transactions.
3. **Cumulative Gross Spend**: Aggregates total historical prices to print a collective financial summary of all purchases combined.

---

## 🗺️ Application Routes (URL Endpoints)

| HTTP Method | Route URL     | View Function    | Description                                                                                           |
| ----------- | ------------- | ---------------- | ----------------------------------------------------------------------------------------------------- |
| **GET**     | `/`           | `views.index`    | Renders the primary store shelf using an updated Bootstrap 5 item grid.                               |
| **POST**    | `/amadon/buy` | `views.buy`      | **Background Worker**. Resolves product details from database, commits the order, and updates totals. |
| **GET**     | `/checkout`   | `views.checkout` | **Safe Checkout Landing**. Displays real-time calculations from the current session cache.            |

---

## 📁 Workspace Configuration

Ensure your application folder structure matches the layout below:

```text
amadon_proj/
│
├── amadon_app/
│   ├── templates/
│   │   └── store/
│   │       ├── index.html     # Main Secure Shop Frontend (Bootstrap 5)
│   │       └── checkout.html  # Secure Invoice Confirmation Panel
│   ├── models.py              # Schema Blueprints for Products and Logs
│   ├── urls.py                # Decoupled PRG Route Registries
│   └── views.py               # Calculation Engine & Database Auditing

```

---

## 🏃‍♂️ Database Seeding & Local Execution

1. Navigate to your root project workspace folder and generate your database infrastructure:

```bash
python manage.py makemigrations amadon_app
python manage.py migrate

```

2. Seed the database with catalog items by accessing the interactive **Django Shell**:

```bash
python manage.py shell

```

3. Copy and run the following script inside the shell environment to register the inventory items:

```python
from amadon_app.models import Product

Product.objects.create(description="Dojo Tshirt", price=19.99)
Product.objects.create(description="Dojo Sweater", price=29.99)
Product.objects.create(description="Dojo Cup", price=4.99)
Product.objects.create(description="Algorithm Book", price=49.99)

exit()

```

4. Launch the local web server instance:

```bash
python manage.py runserver

```

5. Open your web browser and load: `http://127.0.0.1:8000/`

```

```
