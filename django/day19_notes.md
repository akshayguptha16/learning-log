# Day 19 - Django Templates

## What I built
- Created templates folder structure — contacts/templates/contacts/home.html
- Updated view to render HTML template instead of plain text
- Passed data from view to template using context dictionary
- Used {{ variable }} to display variables in template
- Used {% for item in list %} to loop through data in template
- Displayed dynamic contact list from view in browser

## Key concepts
- render(request, 'template.html', context) - renders template with data
- context dictionary - passes data from view to template
- {{ }} - variable tags, display data
- {% %} - logic tags, loops and conditions
- {% for item in list %} {% endfor %} - template loop
- {{ list|length }} - Django filter, counts items
- Template folder must be app/templates/app/template.html
