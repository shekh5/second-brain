---
type: concept
tags: [system-design, caching]
sources: [caching-basics]
created: 2026-11-14
updated: 2026-11-14
---

# Cache patterns (cache-aside, read-through, write-through, write-back)

**In one line:** the rules for who reads and writes the [[caching|cache]] versus the database, and in what order.

## How it works

| Pattern | Read path | Write path | Note |
|---|---|---|---|
| **Cache-aside** (lazy loading) | App checks cache → on miss, app reads DB and fills cache | App writes DB, deletes cache key | Most common. First request always slow. |
| **Read-through** | App asks cache → cache loads DB on miss | (usually combined with another write pattern) | App only talks to the cache. |
| **Write-through** | from cache | App writes cache **and** DB together | Cache always fresh, writes slower. |
| **Write-back** (write-behind) | from cache | App writes cache only; flushed to DB later in batches | Fastest writes, **risk of data loss** if cache dies. |

(src: [[caching-basics]])

Cache-aside, step by step:
```
1. app → cache.get(key)          # miss
2. app → db.query(...)
3. app → cache.set(key, value, ttl)
4. next request → cache.get(key) # hit ⚡
```

## When to use which
- **Cache-aside**: default choice for read-heavy apps. Only data that is actually requested gets cached.
- **Write-through**: when reads right after writes must be fresh (e.g. user settings).
- **Write-back**: very write-heavy workloads where losing a few seconds of data is acceptable (e.g. view counters, analytics). (note: general knowledge, not from a source)

## Trade-offs
| Pattern | Pro | Con |
|---|---|---|
| Cache-aside | simple, resilient (cache down → still works via DB) | stale data possible, cold start |
| Write-through | fresh cache | slower writes, caches data nobody reads |
| Write-back | very fast writes | data loss risk, complex |

## Related
- [[cache-invalidation]] — the write path is where staleness comes from
- [[cache-eviction-policy]]

## Sources
- [[caching-basics]]
