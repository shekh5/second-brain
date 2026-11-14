---
type: concept
tags: [system-design, caching, performance]
sources: [caching-basics, tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# Caching

**In one line:** keep a copy of slow-to-get data in a fast place so the next request is quick.

## How it works

```
request ──► cache ──hit──► return fast ⚡
              │
             miss
              ▼
           database ──► return slow 🐢 (and usually store in cache)
```

- **Cache hit** — data found in the cache.
- **Cache miss** — not found; go to the slower source.
- **Hit ratio** = hits ÷ total requests. The main health metric of a cache. (src: [[caching-basics]])

Reading from RAM takes ~100 ns, while a networked database query takes ~1–10 ms,
roughly 10,000–100,000× slower. (src: [[caching-basics]])

## Where caches live
| Layer | Example | What it stores |
|---|---|---|
| Browser | HTTP cache | pages, images on the user's device |
| Edge | [[cdn]] | static files near users |
| Application | Redis, Memcached ([[redis-vs-memcached]]) | query results, sessions, computed data |
| Database | buffer pool | hot table/index pages |

(src: [[caching-basics]])

## Why it matters / when to use it
> **Lesson from Facebook:** a plain cache like Memcache won't fill itself on a miss or keep itself consistent. When every engineer has to handle that, bugs and stale data follow. (src: [[tao-the-power-of-the-graph]])

- Data is **read much more often than written** (profiles, product pages, feeds).
- The source is **slow or expensive** (DB joins, external APIs, ML inference).
- A slightly **stale answer is acceptable** for a short time.

## Trade-offs
| Pro | Con |
|---|---|
| Much lower latency | Data can be stale ([[cache-invalidation]]) |
| Less load on the database | Extra component to run and monitor |
| Cheaper at scale | Memory is limited, so you need an [[cache-eviction-policy]] |
| | More complex code paths ([[cache-patterns]]) |

## Real-world examples
- Facebook: huge Memcached fleet in front of its databases. (src: [[caching-basics]]) Later it built [[tao]], which puts two tiers of cache (followers, leaders) inside one graph service, so product engineers no longer manage the cache by hand. (src: [[tao-the-power-of-the-graph]])
- Twitter/X: timelines cached in Redis. (src: [[caching-basics]])
- Netflix: video cached on CDN boxes close to viewers. (src: [[caching-basics]])

## Related
- Part of the [[system-design]] map
- [[cache-patterns]] — how the app reads and writes through a cache
- [[cache-eviction-policy]] — what to remove when full
- [[cache-invalidation]] — keeping cached data correct
- [[cdn]] — caching at the network edge

## Sources
- [[caching-basics]]
- [[tao-the-power-of-the-graph]]
