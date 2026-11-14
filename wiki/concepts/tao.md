---
type: concept
tags: [system-design, caching, databases, case-study]
sources: [tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# TAO (Facebook's graph store)

**In one line:** Facebook's distributed data service that stores the social graph as objects and edges, with a big built-in cache in front of MySQL.

## How it works

```
                 web servers (clients)
                        │
       ┌────────────────▼────────────────┐
       │  follower cache tier (many)     │  ← serves reads; miss → ask leader
       └────────────────┬────────────────┘
       ┌────────────────▼────────────────┐
       │  leader cache tier              │  ← keeps region consistent, RAM + Flash
       └────────────────┬────────────────┘
       ┌────────────────▼────────────────┐
       │  MySQL (sharded)                │  ← persistent storage
       └─────────────────────────────────┘
   one set of these per region; writes go follower → leader → MySQL
```

- **Data model:** a [[graph-data-model]] of objects (users, posts, check-ins) and associations (likes, friend-of, comments). (src: [[tao-the-power-of-the-graph]])
- **API:** only three read types — point ("does Alice like this post?"), range ("50 newest comments") and count. No complex graph walks during a page load. (src: [[tao-the-power-of-the-graph]])
- **Storage:** data split into hundreds of thousands of shards ([[sharding]]); each shard lives in one MySQL database and on one set of cache servers per cluster. (src: [[tao-the-power-of-the-graph]])
- **Caching:** two tiers of write-through cache ([[cache-patterns]]). A follower miss fills from a leader; a leader talks to MySQL. Writes travel up the chain, and caches are updated as the reply comes back down. (src: [[tao-the-power-of-the-graph]])
- **Multi-region:** each shard has one primary region that accepts writes; [[replication]] copies them to secondary regions. Secondary regions forward writes to the primary. (src: [[tao-the-power-of-the-graph]])
- **Consistency:** [[eventual-consistency]] by default; strong consistency available per request at higher cost. (src: [[tao-the-power-of-the-graph]])

## Why it matters / when to use it
TAO is a textbook answer to "design a social network's data layer". Its lesson: when every
team has to hand-manage a cache next to a database, bugs follow. Putting the cache **inside one
service with one simple API** gave speed *and* correctness. (src: [[tao-the-power-of-the-graph]])

Key workload facts that drove the design (src: [[tao-the-power-of-the-graph]]):
- Read-heavy: over a billion reads vs millions of writes per second.
- **Creation-time locality:** new items are the most read, so data is ordered by time.
- Many queries ask about edges that **don't exist** ("does this user like that story?" — usually no), which wastes a normal database's block cache.
- **Hot spots:** a celebrity photo can spike to millions of reads; shards are moved or cloned to spread load.

## Trade-offs
| Pro | Con |
|---|---|
| One simple API; engineers don't manage caching | Custom system to build and operate |
| Huge read throughput from RAM/Flash caches | Only simple queries (no joins or traversals) |
| Schema changes need no DBA work | Eventual consistency: users may briefly see old data |
| Shards can move to fix hot spots | All writes for a shard go to one primary region (cross-region write latency) |

## Real-world examples
- Facebook likes, pages, events, comments and check-ins all run on objects and associations. (src: [[tao-the-power-of-the-graph]])
- Similar ideas: LinkedIn's graph services and Twitter's FlockDB store social edges separately from content. (note: general knowledge, not from a source)

## Related
- [[caching]] — TAO is a cache-first data store
- [[redis-vs-memcached]] — TAO replaced raw Memcache usage
- [[sharding]], [[replication]], [[eventual-consistency]] — its three distributed-systems building blocks

## Sources
- [[tao-the-power-of-the-graph]]
