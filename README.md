### INF601 - Advanced Programming in Python
### Austin Rivera
### Mini Project 4

Simple Book Catalog Web App

This is basically a small website where you can add and look at books, like a mini library.

## Description

For this mini project, I built a web app using Django. It's got a homepage, a list of books with a search bar I added extra, details for each book, a form to add new ones, an about page, plus login and register section. I used Bootstrap to make it look decent, and there's a modal on the home page as required. The admin side is set up so you can manage books easily there too. I tried to keep it simple but added the search to make it a little better.

## Getting Started

### Dependencies

* You need Python 3 
* Works on Windows, Mac, or Linux – I tested on Windows 11
* No fancy OS stuff needed
* Install packages with: pip install -r requirements.txt (mainly Django)

### Installing

* Grab the code by cloning the repo: git clone https://github.com/AustinMRivera/miniproject4AustinRivera.git
* Go into the folder: cd miniproject4AustinRivera

### Executing program

* Set up a virtual environment: python -m venv venv
* Activate it: source venv/bin/activate (or venv\Scripts\activate on Windows)
* Install deps: pip install -r requirements.txt
* Make the database ready: python manage.py makemigrations
* Apply them: python manage.py migrate
* Create an admin user: python manage.py createsuperuser (pick a username/password)
* Start the server: python manage.py runserver
* Go to http://127.0.0.1:8000/ in your browser
