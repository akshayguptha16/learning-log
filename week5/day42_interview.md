# Day 42 - Mock Technical Interview (Advanced)

## Q1: Global Interpreter Lock (GIL)

The GIL is a lock in CPython that ensures only one thread executes
Python bytecode at a time. It simplifies memory management and protects
Python's internal data structures.

Key points:
- GIL prevents true parallel thread execution in CPython
- CPU-bound tasks: multithreading does NOT improve performance
- I/O-bound tasks: multithreading DOES help - threads release GIL while waiting
- Solution for CPU-bound: use multiprocessing module
- Each process has its own interpreter and its own GIL
- multiprocessing enables true parallel execution on multiple CPU cores

## Q2: Django Middleware

Middleware sits between HTTP request and Django view, and between
view and HTTP response. Processes requests before views and responses
before sending to client.

Custom middleware use case - Request/Response Logger:
- Log every incoming request - method, URL, user, IP address
- Log every outgoing response - status code, time taken
- Implement once instead of adding logging to every view
- DRY principle applied at framework level
- Useful for debugging, monitoring, and auditing

## Q3: Notification System Design

### Flow
1. User action (like/comment/follow) → API saves primary action → returns success
2. API publishes event to message queue (async - don't block)
3. Notification Service consumes event
4. Creates notification record in database
5. If user online → send via WebSocket (real-time)
6. If user offline → store in DB, show on next login

### Components
- Message Queue - decouples notification creation from API
- Notification Service - dedicated service, scales independently
- WebSocket - real-time delivery to online users
- Database - persistent storage for all notifications
- Redis - cache unread notification counts

### Scaling Challenge - WebSocket + Load Balancer
Problem: Multiple WebSocket servers, user connected to only one server.
How does Notification Service know which server has the user's connection?

Solution 1 - Redis Pub/Sub (small/medium scale):
- All WebSocket servers subscribe to Redis
- Notification Service publishes to Redis
- Only server with active connection delivers message
- Simple, integrates well with Django Channels

Solution 2 - Connection Registry (large scale):
- Redis maps user_id → WebSocket server
- Notification Service looks up user's server directly
- Sends message to that specific server only
- More efficient - no broadcasting to all servers
- Better for millions of concurrent users

### Key Design Decisions
- Async processing via message queue keeps API responsive
- Notification Service scales independently from main API
- Database indexes on user_id and created_at for fast queries
- Archive old notifications to keep DB performant

## Interview Assessment
- GIL: Perfect - CPU vs I/O bound, multiprocessing solution
- Middleware: Correct concept, practical example
- Notification System: Exceptional - async queue, WebSockets,
  two scaling solutions with trade-offs
- Overall: Ready for second round interviews at Bengaluru startups
