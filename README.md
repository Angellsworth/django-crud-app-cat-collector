
# 🐱 Cat Collector  
**Track, feed, and spoil your digital fur babies.**  
A full-stack Django CRUD app built with love (and whiskers) as a first dive into Django.

---

## 🐾 About the Project

Welcome to **Cat Collector** — your cozy little corner of the internet to keep tabs on your beloved kitties.  
Whether you're managing a mansion full of majestic floofs or a single spicy tabby, this app helps you log meals, assign toys, and feel like the ultimate cat parent.  
Built during General Assembly’s Software Engineering course, this was my very first paws-on experience with Django!

---

## 🛠️ Tech Stack

- 🐍 Python 3.11  
- 🧱 Django 5.2  
- 🐘 PostgreSQL  
- 🎨 HTML, CSS (modular styles)  
- 🧵 Django Templating Engine  
- 🧑‍💻 Auth via Django’s built-in User model  

---

## 📸 Screenshots

_(Include some playful screenshots of your cat list page, toy associations, and the detail view if you have 'em!)_

---

## ✨ Features

- 🔐 Secure sign up and login/logout flow  
- 🐾 Only see and manage your own cats  
- 📋 Full CRUD for your fluffy little companions  
- 🦴 Add and manage toys for each cat  
- 🕒 Log mealtimes with `Feeding` records  
- 🎨 Custom forms styled with modular CSS  
- 🚪 Route protection using `@login_required` & `LoginRequiredMixin`  

---

## 🧪 Setup Instructions

```bash
# 1. Clone this repository
git clone https://github.com/your-username/cat-collector.git
cd cat-collector

# 2. Spin up your virtual environment
pipenv install django
pipenv shell

# 3. Create your local database
createdb catcollector

# 4. Make and run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the dev server
python manage.py runserver

# 6. Visit the app at:
http://localhost:8000



⸻

📁 Project Structure

catcollector/
├── main_app/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── catcollector/
│   └── settings.py
├── db (PostgreSQL)
└── manage.py



⸻

🧠 What I Learned
	•	How Django manages models, views, and templates
	•	How to create and link models using relationships (ForeignKey, ManyToManyField)
	•	How to secure views using decorators and mixins
	•	How to make Django forms a little less… plain 😅
	•	That everything is better with cats 🐈

⸻

🧹 Future Upgrades
	•	📸 Upload cat profile pics
	•	📍 Track feeding locations via Google Maps
	•	⏰ Schedule notifications for feedings or vet visits

⸻

👏 Special Thanks

To the wonderful felines in my life (real and digital),
and to the team at General Assembly for making Django feel less scary.
You taught me that CRUD can actually be cute.

⸻

📬 Contact

Angela Ellsworth
GitHub | LinkedIn

⸻

“Time spent with cats is never wasted.” – Sigmund Freud

