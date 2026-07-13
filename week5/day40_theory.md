# Day 40 - ORM Optimization and Docker Networking Theory

## Django ORM - select_related vs prefetch_related

### The N+1 Problem
When Django fetches a list of objects and accesses related objects in a loop,
it executes one query for the main objects and N additional queries for each
related object. For 100 posts this means 101 queries.

### select_related()
- Used for ForeignKey and OneToOneField relationships
- Performs a SQL JOIN - fetches everything in one query
- Best for forward relationships (Post → Author)

Example:
```python
# Bad - N+1 queries
posts = Post.objects.all()
for post in posts:
    print(post.author.name)  # separate query each time

# Good - 1 query with JOIN
posts = Post.objects.select_related("author")
for post in posts:
    print(post.author.name)  # no extra query
```

### prefetch_related()
- Used for ManyToManyField and reverse ForeignKey relationships
- Executes separate queries then combines in Python memory
- Best for reverse relationships and many-to-many

Example:
```python
# Bad - N+1 queries
posts = Post.objects.all()
for post in posts:
    tags = post.tags.all()  # separate query each time

# Good - 2 queries total, combined in Python
posts = Post.objects.prefetch_related("tags")
for post in posts:
    tags = post.tags.all()  # no extra query
```

### Key Difference
- select_related: SQL JOIN, one query, forward FK/OneToOne
- prefetch_related: separate queries + Python merge, ManyToMany/reverse FK

---

## Docker Networking

### Bridge Network
When docker-compose up runs, Docker creates a private bridge network.
All containers in the same compose file join this network automatically.
Containers are isolated from outside world but can talk to each other.

### Container DNS
Docker provides built-in DNS inside the bridge network.
Containers find each other by service name not IP address.
Service name db automatically resolves to PostgreSQL container IP.
This is why settings.py uses HOST: db not HOST: localhost.

### localhost vs service name
localhost inside Django container = Django container itself
db inside Django container = PostgreSQL container
Never use localhost to connect between containers.

### Port Mapping
Format: "host_port:container_port"
"8000:8000" = expose container port 8000 to host machine port 8000
"5433:5432" = map host port 5433 to container port 5432

### Critical insight
ports section exposes container to HOST MACHINE only.
Removing ports from db service does NOT affect Django→PostgreSQL connection.
Containers on same bridge network communicate internally regardless of ports.
ports only needed when you want to connect from your laptop directly.

## Summary
- select_related = JOIN = one query = ForeignKey/OneToOne
- prefetch_related = separate queries + Python merge = ManyToMany/reverse FK
- Docker bridge network = private network for containers in same compose file
- Service names = container DNS = how containers find each other
- ports = host machine access only, not inter-container communication
