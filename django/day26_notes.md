# Day 26 - PostgreSQL Integration

## What I did
- Installed PostgreSQL 18 on Windows
- Installed psycopg2-binary Python adapter
- Created contactbook database in pgAdmin
- Updated Django settings.py to use PostgreSQL
- Ran migrations to create all tables in PostgreSQL
- Created superuser for new database
- Added Indian contact data through admin panel
- Verified API returning data from PostgreSQL

## Settings change
Changed DATABASES in settings.py from SQLite to PostgreSQL:
- ENGINE: django.db.backends.postgresql
- NAME: contactbook
- USER: postgres
- HOST: localhost
- PORT: 5432
- PASSWORD: stored as environment variable

## Key concepts
- PostgreSQL - production-grade relational database
- psycopg2-binary - Python adapter that connects Django to PostgreSQL
- Django ORM works identically with SQLite and PostgreSQL
- Only settings.py needs to change - no code changes needed
- Environment variables - store passwords securely, never commit to GitHub
- os.environ.get() - reads environment variable with fallback value
- pgAdmin - graphical interface for managing PostgreSQL databases
- Port 5432 - default PostgreSQL port

## Why PostgreSQL over SQLite
- SQLite - file based, good for development, not for production
- PostgreSQL - handles multiple users simultaneously
- PostgreSQL - faster for large datasets
- PostgreSQL - used in every real production Django application
- PostgreSQL - required for deployment on most cloud platforms

## Commands used
- pip install psycopg2-binary
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
