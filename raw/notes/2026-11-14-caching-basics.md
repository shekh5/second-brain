# Caching basics — starter study notes

> Origin: starter notes written by Claude on 2026-11-14 as the first demo source
> for this wiki. Replace or supplement with real articles over time.

## What is a cache?
A cache is a small, fast store that keeps copies of data that is expensive to
fetch or compute, so later requests can be served quickly. Reading from memory
(RAM) takes around 100 nanoseconds; a database query over the network often takes
1–10 milliseconds, roughly 10,000–100,000 times slower. Caching trades memory and
some freshness for speed.

A **cache hit** means the data was found in the cache. A **cache miss** means it
wasn't, so the system goes to the slower source. The **hit ratio** (hits / total
requests) is the main health metric of a cache.

## Where caches live
- Browser cache (on the user's device)
- CDN (servers near users that store static files like images and video)
- Application cache (Redis or Memcached next to your servers)
- Database's own internal cache (buffer pool)

## Caching patterns (how the app talks to the cache)
1. **Cache-aside (lazy loading)** — the app checks the cache; on a miss it reads
   the database, then writes the result into the cache. Most common pattern.
   Only requested data gets cached. First request is always slow.
2. **Read-through** — like cache-aside, but the cache itself loads from the
   database on a miss. The app only talks to the cache.
3. **Write-through** — every write goes to the cache and the database at the same
   time. Cache is always fresh, but writes are slower.
4. **Write-back (write-behind)** — writes go to the cache only, and are flushed to
   the database later in batches. Very fast writes, but data can be lost if the
   cache crashes before flushing.

## Eviction policies (what to throw out when the cache is full)
- **LRU (least recently used)** — remove the item not used for the longest time.
  The most common default.
- **LFU (least frequently used)** — remove the item used the fewest times.
- **FIFO** — remove the oldest item.
- **TTL (time to live)** — each item expires after a fixed time, regardless of use.

## Cache invalidation (keeping the cache correct)
"There are only two hard things in computer science: cache invalidation and naming
things." — Phil Karlton.

When the database changes, the cached copy becomes **stale**. Approaches:
- Set a TTL so stale data eventually expires.
- Delete the cache key when the data is written (most common with cache-aside).
- Update the cache on write (write-through).

Danger: **thundering herd / cache stampede** — a popular key expires, and
thousands of requests miss at the same moment and all hit the database together.
Fixes: a lock so only one request rebuilds the value, or slightly randomised TTLs.

## Redis vs Memcached (short)
- Memcached: simple key-value, multi-threaded, strings only, no persistence.
- Redis: rich data types (lists, sets, sorted sets, hashes), persistence options,
  replication, pub/sub. Most teams pick Redis today.

## Real-world examples
- Facebook ran one of the largest Memcached deployments to serve its social graph.
- Twitter/X caches timelines in Redis so the home feed loads instantly.
- Netflix uses CDNs (Open Connect) to cache video close to viewers.
