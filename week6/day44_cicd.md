# Day 44 - CI/CD with GitHub Actions

## What I built
- Set up GitHub Actions workflow for Django Contact Book
- Automated tests run on every push to main branch
- Green checkmark = tests passed, Red X = tests failed
- Workflow file: .github/workflows/django.yml

## How It Works
1. Developer pushes code to GitHub
2. GitHub Actions detects the push
3. Spins up fresh Ubuntu container on GitHub servers
4. Installs Python and dependencies
5. Runs Django tests automatically
6. Shows green checkmark or red X on the commit

## Workflow File Structure
```yaml
name: Django CI

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
```

## Key Concepts
- CI - Continuous Integration - automatically test every code change
- CD - Continuous Deployment - automatically deploy after tests pass
- GitHub Actions - GitHub's built-in CI/CD platform
- Workflow - defined in .github/workflows/*.yml
- on: push - triggers workflow on code push
- jobs - what the workflow does
- runs-on: ubuntu-latest - fresh Ubuntu container per run
- steps - individual tasks in the job
- actions/checkout - clones repo into container
- actions/setup-python - installs Python version

## Why CI/CD Matters
- Catches bugs before they reach production
- Consistent deployments - no human error
- Every team member's code is automatically tested
- Clear deployment history
- Faster and safer releases
- Industry standard - expected at every tech company

## Resume Addition
"Configured GitHub Actions CI/CD pipeline that automatically
runs tests on every push to main branch."
