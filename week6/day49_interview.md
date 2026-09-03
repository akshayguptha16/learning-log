# Day 49 - Final Interview Questions (10/10 Correct)

## Q1: Shallow Copy vs Deep Copy
- Shallow copy: new outer object, same references to nested objects
- Deep copy: recursively copies everything, completely independent
- copy.copy() for shallow, copy.deepcopy() for deep
- Deep copy uses more memory and is slower

## Q2: Django Signals
- Allow different parts of Django app to communicate when events occur
- Execute code automatically when event happens (model saved, deleted)
- Example: post_save signal to create user profile when new user created
- Use when you need side effects after events without cluttering views/models

## Q3: null=True vs blank=True
- null=True: database level, allows NULL in database column
- blank=True: validation level, allows empty value in forms
- null is for database, blank is for forms/validation

## Q4: __str__ vs __repr__
- __str__: human-readable representation, used by print()
- __repr__: developer-oriented, unambiguous, used for debugging
- __repr__ appears when objects are inside collections like lists

## Q5: @staticmethod vs @classmethod
- @classmethod: receives class as first argument (cls), can access class attributes
- @staticmethod: receives nothing automatically, behaves like normal function in class
- Both called on class without creating instance

## Q6: Database Indexing
- Additional data structure that speeds up database queries
- Add indexes to fields used in filter(), get(), order_by() on large tables
- Trade-off: indexes slow down INSERT, UPDATE, DELETE operations
- Don't index every field - only frequently queried ones

## Q7: Synchronous vs Asynchronous
- Sync: tasks execute one after another, program waits
- Async: start task, continue working while waiting for I/O
- Use async in Django for: multiple external API calls, WebSockets, network services
- Don't use async for simple views or CPU-intensive operations

## Q8: REST Principles
- Client-server separation
- Stateless communication
- Resource-based URLs
- Proper HTTP methods and status codes
- Consistent data representation (JSON)
- Example: GET /api/products/10/ retrieves, DELETE /api/products/10/ deletes

## Q9: SQL Injection Prevention in Django ORM
- Parameterized queries - user input passed separately from SQL
- Input treated as data not executable SQL
- Raw SQL still requires care - must use parameterized queries
- Never concatenate user input directly into SQL

## Q10: Django Performance Debugging
1. Reproduce issue, measure response time with Postman/DevTools
2. Django Debug Toolbar - inspect query count and timing
3. EXPLAIN ANALYZE - understand query plan, find missing indexes
4. Fix N+1 queries with select_related() or prefetch_related()
5. cProfile or py-spy for slow Python code
6. Redis caching for repeated expensive operations
7. Locust or k6 for load testing
8. Monitor CPU, memory, database performance
9. Measure after every optimization to confirm improvement

## Score: 10/10 - All questions answered correctly without AI or notes
