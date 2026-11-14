---
type: comparison
tags: [system-design, caching]
sources: [caching-basics]
created: 2026-11-14
updated: 2026-11-14
---

# Redis vs Memcached

| Dimension | Redis | Memcached |
|---|---|---|
| Data types | strings, lists, sets, sorted sets, hashes, … | strings only |
| Persistence | optional (snapshots, append log) | none |
| Replication | yes | no (built in) |
| Pub/sub | yes | no |
| Threading | mostly single-threaded core | multi-threaded |

(src: [[caching-basics]])

## When to pick Redis
Almost always today: you get rich data structures (leaderboards with sorted sets,
queues with lists), persistence, and replication. (src: [[caching-basics]])

## When to pick Memcached
A pure, simple key-value [[caching|cache]] where multi-threaded throughput on big
machines matters and you need nothing else. (note: general knowledge, not from a source)

## Sources
- [[caching-basics]]
