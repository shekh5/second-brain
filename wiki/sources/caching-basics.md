---
type: source
tags: [system-design, caching]
sources: []
created: 2026-11-14
updated: 2026-11-14
---

# Caching basics — starter study notes

- **Raw file:** `raw/notes/2026-11-14-caching-basics.md`
- **Author / origin:** starter notes written by Claude as the wiki's first demo source
- **Ingested:** 2026-11-14

## Summary
A cache is a small, fast store holding copies of expensive-to-fetch data. The notes
cover where caches live (browser, CDN, app cache, database), four patterns for how
an app reads and writes through a cache, the policies used to evict items when the
cache is full, and the hard problem of keeping cached data fresh (invalidation).
They end with a short Redis vs Memcached comparison and real-world examples.

## Key takeaways
- Caching trades memory and freshness for speed; RAM is ~10,000× faster than a networked DB query.
- Hit ratio is the main health metric of a cache.
- Cache-aside is the most common pattern; write-back is fastest but can lose data.
- LRU is the usual default eviction policy.
- Invalidation is the hard part; watch out for cache stampedes when hot keys expire.

## Concepts touched
[[caching]], [[cache-patterns]], [[cache-eviction-policy]], [[cache-invalidation]],
[[cdn]], [[redis-vs-memcached]]

## Open questions
- Exact latency numbers vary by hardware; verify with a "latency numbers every programmer should know" source.
- Facebook/Twitter/Netflix examples are summary-level; a real engineering blog post would add depth.
