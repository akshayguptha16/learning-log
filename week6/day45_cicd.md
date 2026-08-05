# Day 45 - Complete CI/CD Pipeline with Auto-Deployment

## What I built
- Added RENDER_DEPLOY_HOOK as GitHub Secret
- Updated GitHub Actions workflow with two jobs - test and deploy
- Deploy job only runs if test job passes
- Deploy job only runs on main branch
- Both jobs showing green checkmarks - pipeline fully working
- Every push to main now automatically tests AND deploys

## Updated Workflow File
```yaml
name: Django CI/CD

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python manage.py test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to Render
      run: curl "${{ secrets.RENDER_DEPLOY_HOOK }}"
```

## Complete Pipeline Flow
