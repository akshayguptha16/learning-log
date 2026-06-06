# Day 18 - Django Setup and First View

## What I built
- Created a Django project called contactbook
- Created a Django app called contacts
- Registered contacts app in settings.py INSTALLED_APPS
- Created first view function that returns HttpResponse
- Created urls.py in contacts app
- Connected contacts urls to main project urls using include()
- Saw "Hello from Django!" in the browser

## Key commands
- django-admin startproject contactbook .
- python manage.py startapp contacts
- python manage.py runserver

## Key concepts
- Project contains multiple apps
- urls.py maps URLs to view functions
- views.py handles requests and returns responses
- Every request goes through urls.py first
- HttpResponse returns plain text to browser
