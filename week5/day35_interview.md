# Day 35 - Mock Technical Interview

## Questions and Answers

### Q1: List vs Tuple
- List is mutable - elements can be added, removed, modified
- Tuple is immutable - cannot be changed after creation
- Use list for dynamic data - user inputs, shopping carts, task lists
- Use tuple for fixed data - coordinates, RGB values, config settings
- Tuples are more memory efficient
- Tuples can be used as dictionary keys (if hashable)

### Q2: == vs is
- == compares values of two objects
- is compares identity - whether both variables point to same object in memory
- a = [1,2,3]; b = [1,2,3]; a == b is True but a is b is False
- Always use is None, never == None

### Q3: Django Request Cycle
WSGI → middleware → urls.py → views.py → models.py → template → response
- Request enters through wsgi.py
- Passes through middleware
- contactbook/urls.py matches URL pattern
- Follows include() to contacts/urls.py
- Calls view function
- View queries database via ORM
- render() loads template with context
- Response passes back through middleware
- HTML sent to browser

### Q4: N+1 Query Problem
- One query for main data + N queries for each related object
- Fix with select_related() for ForeignKey/OneToOne - uses SQL JOIN
- Fix with prefetch_related() for ManyToMany/reverse FK - separate queries combined in Python

### Q5: PUT vs PATCH
- PUT replaces entire resource - full update
- PATCH updates only specified fields - partial update
- In DRF: PUT maps to update(), PATCH uses partial=True

### Q6: System Design - Scaling Contact Book
- Move to PostgreSQL
- Optimize queries with select_related/prefetch_related
- Redis caching for frequent reads - key pattern: contacts:user:101
- Invalidate cache on write operations
- Multiple Django instances behind load balancer
- Background workers for async tasks
- Monitoring and logging

## Interview Assessment
- Strong: Python fundamentals, Django concepts, REST APIs, caching
- Needs work: System design depth, staying focused on exact question asked
- Overall: Would pass screening round at most Bengaluru startups
