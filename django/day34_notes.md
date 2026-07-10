# Day 34 - Docker and Docker Compose

## What I built
- Created Dockerfile for Django Contact Book
- Created docker-compose.yml with web and db services
- Ran Django + PostgreSQL together inside Docker containers
- Applied migrations inside running container
- Django Contact Book running fully in Docker

## Key commands
- docker-compose up --build
- docker-compose up -d
- docker-compose exec web python manage.py migrate
- docker-compose ps
- docker build -t image-name .
- docker run -p 8000:8000 image-name

## Key concepts
- Dockerfile - blueprint for building a Docker image
- Image - built from Dockerfile, like a class
- Container - running instance of an image, like an object
- docker-compose.yml - defines and runs multiple containers
- depends_on - ensures db starts before web container
- Service names as hostnames - containers talk to each other using service name not localhost
- Environment variables - pass config to containers securely
- Migrations inside container - docker-compose exec web python manage.py migrate

## Why Docker matters
- Eliminates "works on my machine" problem
- Same environment in development, testing, and production
- Easy to share and deploy applications
- Industry standard for backend and DevOps roles
