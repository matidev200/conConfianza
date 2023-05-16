# conConfianza - Live chat with django
Basic web app with Contacts, Profiles, Live Chat and Requests.

# Instalation

Clone Repository
```
$ git clone https://github.com/matidev200/conConfianza.git
$ cd conConfianza
```

Install pip packages
```
$ pip install -r requirements.txt
```

Configure database
```
$ python manage.py migrate
```

Create two users for testing or create them in http://localhost:8000/profile/register
```
$ python manage.py createsuperuser
```

Start server!, then you can access in http://localhost:8000/profile/login
```
python manage.py runserver
```
