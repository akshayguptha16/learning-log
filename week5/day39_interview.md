# Day 39 - Behavioral Interview Prep and System Design

## Behavioral Questions

### Q1: Technical Challenge
Used FAISS vector database in WhatsApp Knowledge Organizer project.
Problem: FAISS index failing to load correctly, runtime errors on search.
Approach: Isolated each pipeline stage - parsing, embedding, index creation, loading.
Added logging at each step to identify exact failure point.
Root cause: File path inconsistencies on Windows affecting index save/load.
Result: Fixed paths, tested with multiple chat exports, search worked reliably.
Lesson: Systematic debugging, break complex systems into smaller components,
validate each stage instead of guessing.

### Q2: Weakness
Tendency to over-research before implementing - seeking perfect solution.
Fix: Break into smaller tasks, build working solution first, iterate based on testing.
Set time limits for research, focus on incremental progress not perfection.

### Q3: Why Startup over Large Company
- Direct impact and ownership from day one
- Work across multiple areas - backend, deployment, debugging
- Already demonstrated this with live deployed project at django-contact-book.onrender.com
- Rapid learning over structured but slow career path
- Acknowledged large companies positively - shows maturity

## System Design - URL Shortener

### Core Components
- API service - receives long URL, returns short URL
- Database - stores URL mappings (short code → long URL)
- Cache (Redis) - fast lookups for popular URLs
- Load balancer - distributes traffic at scale

### How It Works
1. User submits long URL to API
2. Service generates unique short code
3. Stores mapping in database
4. Returns shortened URL
5. When short URL visited - lookup original URL and redirect

### Short Code Generation - Base62
- Base62 uses 0-9, A-Z, a-z = 62 unique characters
- Converts auto-increment numeric ID to short string
- Why Base62 over Base64: avoids +, /, = characters that complicate URLs
- Why Base62 over random strings: auto-increment IDs guarantee uniqueness
  without collision checks - simpler and more efficient

### Scaling
- Load balancers for multiple API instances
- Redis caching for frequent lookups
- Database read replicas
- CDN for static assets

## Key Interview Lessons
- Always use specific examples not generic statements
- Structure answers: situation → task → action → result
- Acknowledge trade-offs in system design
- Mention your live project as proof of ownership mindset
- Time-box your answers - don't ramble
