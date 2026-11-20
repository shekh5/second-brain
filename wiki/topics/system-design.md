---
type: topic
tags: [system-design]
sources: [caching-basics, tao-the-power-of-the-graph, lovable-set-intelligence-free]
created: 2026-11-14
updated: 2026-11-20
---

# System Design — map

Building systems that stay fast, correct, and available as users grow.
This page is the map; each link is a concept page. ⬜ = no page yet (add a source!).

## 1. Fundamentals
- ⬜ Latency vs throughput
- ⬜ Scalability (vertical vs horizontal)
- ⬜ Availability and reliability

## 2. Caching ✅ started
- [[caching]] — what a cache is and where it lives
- [[cache-patterns]] — cache-aside, write-through, write-back
- [[cache-eviction-policy]] — LRU, LFU, TTL
- [[cache-invalidation]] — keeping data fresh, cache stampedes
- [[cdn]] — caching at the edge
- [[redis-vs-memcached]]
- [[tao]] — case study: Facebook's cache-first graph store

## 3. Scaling the web tier
- ⬜ Load balancer
- ⬜ Stateless services
- ⬜ API gateway / rate limiting

## 4. Data ✅ started
- ⬜ SQL vs NoSQL
- [[graph-data-model]] — nodes and edges instead of tables
- [[replication]] — copies of data for availability and read scaling
- [[sharding]] — split data across servers; watch for hot spots
- ⬜ Consistent hashing
- ⬜ CAP theorem
- [[eventual-consistency]] — copies agree… eventually
- [[copy-on-write]] — share data on copy; duplicate a block only when it is changed (cheap forks/snapshots)

## 5. Async processing
- ⬜ Message queues
- ⬜ Pub/sub, event-driven design
- ⬜ Idempotency

## 6. Classic designs (practice)
- ⬜ URL shortener
- ⬜ News feed
- ⬜ Chat system
- ⬜ Rate limiter

## Suggested learning order
Fundamentals → Caching → Load balancer → Replication → Sharding + consistent hashing
→ CAP → Message queues → practice designs.
