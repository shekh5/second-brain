---
type: concept
tags: [system-design, caching, consistency]
sources: [caching-basics, tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# Cache invalidation

**In one line:** making sure the [[caching|cache]] doesn't keep serving old data after the real data changed.

> "There are only two hard things in computer science: cache invalidation and naming things." — Phil Karlton (src: [[caching-basics]])

## How it works
When the database changes, the cached copy becomes **stale**. Three main approaches:

| Approach | How | Trade-off |
|---|---|---|
| **TTL expiry** | each key expires after N seconds | simple; stale for up to N seconds |
| **Delete on write** | app deletes the key after updating the DB | fresh; next read is a miss |
| **Update on write** | write-through: update cache with DB | fresh; slower writes |

(src: [[caching-basics]]; patterns in [[cache-patterns]])

## Danger: thundering herd / cache stampede
A popular key expires → thousands of requests miss at the same moment → all hit the database at once → DB overloads.

```
key expires ──► 10,000 misses ──► 10,000 DB queries 💥
```

Fixes (src: [[caching-basics]]):
- **Lock / single-flight**: only one request rebuilds the value; the others wait or get the old value.
- **Jittered TTLs**: add randomness so keys don't all expire together.

## Real-world example: Facebook
With Memcache in front of MySQL, appending one edge to a cached list forced the **whole list** to be invalidated, lowering the hit rate. Avoiding thundering herds also needed coordination that client-side code couldn't provide. Facebook's answer was [[tao]], a service that owns both the cache and its consistency. (src: [[tao-the-power-of-the-graph]])

## Why it matters
Stale data bugs are subtle: wrong price, old profile photo, a deleted post still visible.
How stale you can tolerate is a **product decision**, not just a technical one.

## Related
- [[cache-eviction-policy]] — TTL overlaps with eviction
- [[cache-patterns]]
- [[eventual-consistency]] — staleness across database copies

## Sources
- [[caching-basics]]
- [[tao-the-power-of-the-graph]]
