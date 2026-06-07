# Day 24 - Deploying Django to Production

## What I built
- Deployed Django Contact Book live on Render
- Live URL: https://django-contact-book.onrender.com
- Configured Django for production deployment

## Steps taken
- pip install gunicorn whitenoise
- pip freeze > requirements.txt
- Created Procfile: web: gunicorn contactbook.wsgi
- Updated settings.py - ALLOWED_HOSTS, Whitenoise middleware, STATIC_ROOT
- Initialized Git and pushed to GitHub
- Created .gitignore to exclude unnecessary files
- Deployed to Render and fixed start command

## Key concepts
- gunicorn - production Python web server replaces Django dev server
- whitenoise - serves static files without separate web server
- Procfile - deployment start command
- requirements.txt - dependency list for deployment platform
- ALLOWED_HOSTS = ['*'] - allows all domains in production
- Git workflow - init, add, commit, push

## Commands used
- pip freeze > requirements.txt
- git init
- git add .
- git commit -m "message"
- git push -u origin main

## Live project
- URL: https://django-contact-book.onrender.com
- GitHub: https://github.com/akshayguptha16/django-contact-book
