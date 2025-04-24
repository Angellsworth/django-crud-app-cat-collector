<p align="center">
  <img src="static/images/logotype.svg" alt="Cat Collector Logo" width="300"/>
</p>


Cat Collector 😼

A beginner-friendly Django CRUD application for managing your beloved feline friends.

This project was built as a lesson in General Assembly’s Software Engineering program to introduce Django fundamentals: models, views, templates, authentication, and CRUD operations.

⸻

🚀 Project Overview

Cat Collector is a simple full-stack web application built with Django that allows users to:
	•	Track cats they own or care for
	•	Log daily feedings
	•	Associate fun toys with each cat

This was my very first Django CRUD app. It’s designed as a guided project to solidify foundational concepts including model relationships, class-based views, route protection, and Django forms.

⸻

🧰 Tech Stack
	•	Python 3.11
	•	Django 5.2
	•	PostgreSQL
	•	HTML5 + CSS3 (modular styles)
	•	Django Templates
	•	Django Auth (Login, Logout, Signup)
	•	Local development environment

⸻

📸 Screenshots

Add screenshots of your homepage, cat detail page, or toy form here if desired!

⸻

📂 Features
	•	User authentication (sign up, log in, log out)
	•	Display only cats that belong to the logged-in user
	•	Full CRUD for Cat model: add, update, delete, view
	•	Feeding log (one-to-many relationship)
	•	Toy association (many-to-many relationship)
	•	Route protection using @login_required and LoginRequiredMixin
	•	Custom signup form

⸻

⚙️ Setup Instructions
	1.	Clone the Repository

git clone https://github.com/your-username/django-crud-app-cat-collector.git
cd django-crud-app-cat-collector


	2.	Install Django in a Virtual Environment

pipenv install django
pipenv shell


	3.	Create the Database

createdb catcollector


	4.	Apply Migrations

python manage.py makemigrations
python manage.py migrate


	5.	Start the Server

python manage.py runserver


	6.	Visit in Your Browser

http://127.0.0.1:8000



⸻

📁 File Structure

django-crud-app-cat-collector/
├── main_app/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
├── catcollector/
│   ├── settings.py
├── db.sqlite3 or PostgreSQL
└── manage.py



⸻

🧠 What I Learned
	•	The MVC-ish structure of Django (Models, Templates, Views)
	•	Class-based views for CRUD
	•	Handling one-to-many and many-to-many relationships
	•	Django’s built-in User model and authentication system
	•	Using decorators and mixins to protect routes
	•	Basic styling of Django-generated forms

⸻

🚀 Future Improvements
	•	Upload cat photos with Cloudinary
	•	Add cat birthdays & filter by age
	•	Generate daily care reminders

⸻

🌟 Acknowledgments

Big thanks to the instructors and lesson writers at General Assembly for building a strong foundation in Django with this starter project.

⸻

📧 Contact

Angela Ellsworth
GitHub: @Angellsworth