This project is a Django-based backend for managing items with full CRUD (Create, Read, Update, Delete) functionality. It uses PostgreSQL as the database and Django Rest Framework (DRF) to expose the APIs.

Features

1. Full CRUD operations for managing items.
2. PostgreSQL integration for data storage.
3. Simple JWT authentication for secure API access.
4. Customizable API endpoints using Django Rest Framework.

Requirements

1. Python 3.8+
2. Django 4.x
3. Django Rest Framework
4. PostgreSQL
5. Simple JWT
6. django-cors-headers
7. psycopg2

Setup and Installation

1. Clone the Repository:
git clone https://github.com/chabikant/wtvision-asgmnt.git
cd wtvision-asgmnt

2. Setup a Virtual Environment:

python -m venv backend_project
source venv/bin/activate    # Linux/macOS
# OR
backend_project\Scripts\activate       # Windows

3. Install Dependencies:

pip install Django Django Rest Framework PostgreSQL Simple JWT django-cors-headers psycopg2

4. Configure PostgreSQL Database:
Before running the project, ensure you have a running PostgreSQL instance and a database created for the project.
Update the DATABASES configuration in settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply Migrations:

python manage.py makemigrations
python manage.py migrate

6. Create Superuser (for admin access):
python manage.py createsuperuser

7. Run the Development Server:
python manage.py runserver

The project will be accessible at http://127.0.0.1:8000/.

8. Accessing API Endpoints
To authenticate and obtain a token:

Endpoint: POST /auth/token/

Body:
{
  "username": "your_username",
  "password": "your_password"
}

You will receive access and refresh tokens in response. Use the access token in the Authorization header for all other requests

9. CRUD API Endpoints for Items:
GET /admin/ - Get admin access.
GET /api/items/ - Get the list of items.
POST /api/items/ - Create a new item.
GET /api/items/<id>/ - Get a specific item by ID.
PUT /api/items/<id>/ - Update an item by ID.
DELETE /api/items/<id>/ - Delete an item by ID.

10. Assumptions Made:
The key and value fields in the items model are essential to the item structure and must be provided for each item.
The PostgreSQL database should be pre-configured with appropriate privileges for the Django application user.
For development purposes, CORS is enabled to allow all origins (CORS_ALLOW_ALL_ORIGINS = True).


Conclusion:
This project provides a robust foundation for an item management system using Django, DRF, and PostgreSQL, with full API access and JWT authentication.