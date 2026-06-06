# Day 21 - Django Forms

## What I built
- Created forms.py with ContactForm using ModelForm
- Updated view to handle both GET and POST requests
- Added form to home template using {{ form.as_p }}
- Used {% csrf_token %} for security
- Validated form data with form.is_valid()
- Saved new contacts to database with form.save()
- Redirected after successful save with redirect('home')
- Users can now add contacts directly from the web page

## Key concepts
- forms.ModelForm - creates form from model automatically
- class Meta - specifies model and fields for the form
- request.method == 'POST' - detects form submission
- ContactForm(request.POST) - binds submitted data to form
- form.is_valid() - validates all fields
- form.save() - saves to database
- redirect('home') - redirects after saving
- {% csrf_token %} - required security token in every form
- {{ form.as_p }} - renders all form fields automatically

## The complete request cycle
GET request → empty form shown → user fills form → 
POST request → validate data → save to database → 
redirect → show updated contact list
