# django-react-semantic
My web development starter kit.

This kit is not intended to be used in production environments.

* Back-end: Django (with REST Framework)
* Front-end: ReactJS
* Styles: Semantic UI

**Installation**
1) Create a project directory and cd into it.
2) Clone the repository (note the dot as the last argument - clones the repository into the current directory without the project folder).
```
git clone https://github.com/ru13r/django-react-semantic.git .
```
3) Create and activate virtual environment (Windows PowerShell commands, please visit *virtualenv* documentation for other operating systems)
```
mkvirtualenv venv-myproject
cd ~/Envs/venv-myproject
.\Scripts\activate
```
4) Cd back to project directory
```
cd C:\Path-to-project-directory
```
5) Install python packages
``` 
pip install -r requirements.txt
```
6) Make migrations, populate database with sample data, create super user.
```
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db
python manage.py createsuperuser
```
7) Init NPM and install NPM packages
``` 
npm install --save-dev
```
**Running**
1) Start webpack development server
```
node server.js
```
2) Start django server (in a different console)
``` 
python manage.py runserver 
```

Use the following links:
* http://127.0.0.1:8000/ - to visit landing page
* http://127.0.0.1:8000/content/ - to visit open content page
* http://127.0.0.1:8000/react-content/ - to visit page powered by ReactJS

A login will be required to view protected content.
You will also be asked to verify your email - look in the console for the verification link.