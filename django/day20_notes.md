# Day 20 - Django Models and Database

## What I built
- Created a Contact model with name, phone, email, city fields
- Ran makemigrations and migrate to create the database table
- Registered Contact model with Django admin
- Added __str__ method to display contact names in admin
- Used Contact.objects.all() to fetch all contacts from database
- Displayed real database contacts on the home page

## Key commands
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

## Key concepts
- models.CharField, models.EmailField - field types
- makemigrations - creates migration files
- migrate - applies migrations to database
- Contact.objects.all() - fetches all records
- Django ORM - no SQL needed
