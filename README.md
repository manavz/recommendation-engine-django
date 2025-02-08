# Recommendation Engine - Django

![Project Banner](assets/banner.png)

A Django-based project that implements the core logic of a recommendation engine. This project demonstrates how to apply basic recommendation algorithms such as content-based and collaborative filtering using Django.

---

## Features

- **Content-Based Filtering**: Recommends items based on similarity of item attributes.
- **Collaborative Filtering**: Generates recommendations by analyzing user interactions.
- **Simple Architecture**: Built using Django with SQLite as the default database.

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/manavz/recommendation-engine-django.git
   cd recommendation-engine-django

## Create and Activate a Virtual Environment:
 ```sh
   python -m venv env
   source env/bin/activate   # For Windows: env\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

## Then, open your browser and visit http://127.0.0.1:8000/ to view the application.

\```
recommendation-engine-django/
├── assets/
│   └── banner.png
├── test_app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── test_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
\```


