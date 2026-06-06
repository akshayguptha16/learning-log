# Day 23 - Bootstrap Styling and Template Inheritance

## What I built
- Created base.html template with Bootstrap CDN and navbar
- Updated home.html to extend base template
- Updated update.html to extend base template
- Replaced plain list with Bootstrap table for contacts
- Added colored buttons - yellow for Edit, red for Delete, blue for Add
- App now looks like a real web application

## Files changed
- contacts/templates/contacts/base.html - new base template with Bootstrap
- contacts/templates/contacts/home.html - extends base, Bootstrap table
- contacts/templates/contacts/update.html - extends base, styled form

## Key concepts
- base.html - master template with common layout
- {% extends 'contacts/base.html' %} - inherit from base template
- {% block content %}{% endblock %} - replaceable section in base
- Template inheritance - write layout once, reuse everywhere
- Bootstrap CDN - add CSS framework via link tag in head
- Bootstrap classes used:
  - navbar, navbar-dark, bg-dark - navigation bar
  - container - centers content with padding
  - row, col-md-4, col-md-8 - grid layout
  - table, table-striped - styled table
  - btn btn-primary, btn-warning, btn-danger - colored buttons

## What the app looks like now
- Dark navbar at top with Contact Book title
- Add contact form on the left
- Contacts table on the right with Edit/Delete buttons
- Clean professional layout using Bootstrap grid
