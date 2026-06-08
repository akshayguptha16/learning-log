# Day 25 - Django REST Framework

## What I built
- Installed Django REST Framework
- Created serializers.py with ContactSerializer
- Built REST API endpoints for Contact model
- Full CRUD API working at /api/contacts/

## API Endpoints
- GET /api/contacts/ - list all contacts
- POST /api/contacts/ - create new contact
- GET /api/contacts/<id>/ - get single contact
- PUT /api/contacts/<id>/ - update contact
- DELETE /api/contacts/<id>/ - delete contact

## Files created/changed
- contacts/serializers.py - new file with ContactSerializer
- contacts/views.py - added api_contacts and api_contact_detail views
- contacts/urls.py - added API URL patterns

## Key concepts
- serializers.py - converts Django models to JSON and back
- ModelSerializer - automatically creates serializer from model
- class Meta - specifies model and fields for serializer
- @api_view decorator - marks function as API view
- Response() - returns JSON response from DRF
- request.data - data from POST/PUT requests
- many=True - serializes a list of objects not just one
- HTTP status codes:
  - 200 OK - successful GET
  - 201 Created - successful POST
  - 204 No Content - successful DELETE
  - 404 Not Found - resource doesn't exist
  - 400 Bad Request - invalid data submitted

## REST conventions
- GET list endpoint - returns all records
- POST list endpoint - creates new record
- GET detail endpoint - returns single record
- PUT detail endpoint - updates single record
- DELETE detail endpoint - deletes single record

## DRF Browsable API
- Django REST Framework provides a web interface
- Can test all endpoints directly in browser
- Shows allowed methods, status codes, response data
