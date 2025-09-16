# Full Stack Data Engineer Demo

## Overview
This is a Django project demonstrating:

- CRUD operations for products via REST APIs
- Integration with a third-party Weather API
- Dashboard with data visualization using Chart.js
- PostgreSQL database (local or Supabase)

This project is designed as a demo task for a Full Stack Data Engineer selection process.

---

## Features

### CRUD API for Products
- **GET** `/api/products/` – List all products
- **POST** `/api/products/` – Create a new product
- **PUT** `/api/products/<id>/` – Update a product
- **PATCH** `/api/products/<id>/` – Partial update
- **DELETE** `/api/products/<id>/` – Delete a product

### Weather API Integration
- **GET** `/api/weather/?city=CityName` – Fetch weather for a given city (uses free public API `wttr.in`).

### Product Summary Report
- **GET** `/api/product_report/` – Returns aggregated product data:
  - Total products
  - Average price
  - Max price
  - Min price

### Dashboard
- **GET** `/dashboard/` – Displays a bar chart summarizing product stats using Chart.js.

---

## Tech Stack
- Python 3.x
- Django 5.x
- Django REST Framework
- PostgreSQL (or Supabase)
- Chart.js
- Requests (for external API)

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/AmolDoiphode21/Full-Stack-Data-Engineer-Demo.git
cd your-repo


Create and activate virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Configure database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Or Supabase host
        'PORT': '5432',
    }
}


Apply migrations:

python manage.py migrate


Create superuser (optional, for admin access):

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Access the application:

CRUD API Browser: http://127.0.0.1:8000/api/products/

Weather API: http://127.0.0.1:8000/api/weather/?city=Delhi

Product report: http://127.0.0.1:8000/api/product_report/

Dashboard: http://127.0.0.1:8000/dashboard/

Testing

You can test APIs using:

Browser (DRF browsable API)

Postman

PowerShell / curl scripts (test_apis.ps1 included)

The test_apis.ps1 script demonstrates:

GET all products

POST new product

PUT / PATCH updates

DELETE product

GET weather

GET product summary report

Notes

Weather API uses wttr.in (free, no API key required)

Dashboard uses Chart.js for bar chart visualization

PostgreSQL is required for CRUD operations; Supabase can be used as an alternative

All CRUD operations return JSON responses via DRF
