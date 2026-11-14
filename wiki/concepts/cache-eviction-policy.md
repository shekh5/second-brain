---
type: concept
tags: [system-design, caching]
sources: [caching-basics]
created: 2026-11-14
updated: 2026-11-14
---

# Cache eviction policy

**In one line:** the rule for which item to throw out when the [[caching|cache]] is full.

## How it works
| Policy | Removes… | Good for |
|---|---|---|
| **LRU** (least recently used) | item untouched for the longest time | general default |
| **LFU** (least frequently used) | item used the fewest times | stable "popular" items |
| **FIFO** | oldest inserted item | simple cases |
| **TTL** (time to live) | anything past its expiry time | freshness, not just space |

(src: [[caching-basics]])

LRU in practice is usually built with a **hash map + doubly linked list**, so both
lookup and "move to front" are O(1). This is a classic interview question.
(note: general knowledge, not from a source)

## Trade-offs
| Policy | Pro | Con |
|---|---|---|
| LRU | adapts to changing access patterns | one big scan can flush useful items |
| LFU | keeps long-term favourites | slow to adapt; old favourites linger |
| TTL | bounds staleness | popular items expire too; can cause a stampede ([[cache-invalidation]]) |

## Real-world examples
- Redis supports `allkeys-lru`, `allkeys-lfu`, `volatile-ttl` and others via `maxmemory-policy`. (note: general knowledge, not from a source)

## Related
- [[cache-invalidation]] — TTL is both an eviction and an invalidation tool
- [[cache-patterns]]

## Sources
- [[caching-basics]]
