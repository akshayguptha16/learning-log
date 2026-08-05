# Day 47 - Advanced Mock Interview

## Q1: Python Garbage Collection
- Reference counting: every object tracks how many variables point to it
- When count hits 0 object is immediately destroyed
- Problem: circular references keep count above 0 even when unreachable
- Solution: cyclic garbage collector runs periodically, finds and destroys cycles
- CPython combines both: reference counting for speed + cyclic GC for cycles
- gc module: import gc; gc.collect() to manually trigger

## Q2: Django Startup Sequence
- manage.py sets DJANGO_SETTINGS_MODULE environment variable
- Django imports settings.py - loads apps, middleware, database config
- Initializes INSTALLED_APPS - creates AppConfig objects, imports models
- AppConfig.ready() runs - registers signals and startup logic
- Builds middleware chain, loads URL configuration
- Prepares ORM and database config (connections opened lazily)
- Development server starts listening for HTTP requests
- No view has run, no request through middleware yet

## Q3: Rate Limiter Design
- Redis for fast atomic counters with TTL
- Key pattern: rate_limit:user:42 with 60-second TTL
- On each request: increment counter
- If count <= 100: request proceeds
- If count > 100: return HTTP 429 immediately
- Django REST Framework has built-in throttling classes
- All API servers share same Redis instance for consistency
- Sliding window or token bucket for smoother rate limiting vs fixed window

## Q4: Merge Two Sorted Lists
- Two pointer technique - one pointer per list
- Compare current elements, append smaller to result
- Move that pointer forward
- When one list exhausted, extend with remaining elements
- Time complexity: O(n + m), Space complexity: O(n + m)
