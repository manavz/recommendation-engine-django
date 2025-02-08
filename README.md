# 🚀 Recommendation Engine - Django

![Project Banner](assets/banner.png)

A powerful **Recommendation Engine** built using **Django** that provides personalized recommendations based on user preferences and behavior.

## 📌 Features
✅ Content-based filtering  
✅ Collaborative filtering  
✅ Scalable architecture with Django & PostgreSQL  
✅ REST API support with Django Rest Framework (DRF)  
✅ Background tasks with Celery & Redis  

## 🛠️ Installation

Clone the repository:
```sh
git clone https://github.com/manavz/recommendation-engine-django.git
cd recommendation-engine-django

python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
pip install -r requirements.txt

Run database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

📦 recommendation-engine-django
 ┣ 📂 assets
 ┃ ┗ 🖼️ banner.png
 ┣ 📂 recommendation
 ┃ ┣ 📂 models
 ┃ ┣ 📂 views
 ┃ ┗ 📜 urls.py
 ┣ 📜 manage.py
 ┣ 📜 README.md
 ┗ 📜 requirements.txt

📷 Screenshot


