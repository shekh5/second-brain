---
type: source
tags: [system-design, caching, databases, distributed-systems]
sources: []
created: 2026-11-14
updated: 2026-11-14
---

# TAO: The power of the graph (Facebook Engineering, 2013)

- **Raw file:** `raw/articles/2026-11-14-tao-the-power-of-the-graph.md`
- **Author / origin:** Mark Marchukov, Facebook Engineering blog, 2013-06-25 — https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/
- **Ingested:** 2026-11-14 (received via Telegram)

## Summary
Facebook must build every user's page on the fly from the social graph in a few hundred
milliseconds, at over a billion reads per second. Their first setup, MySQL with a separate
Memcache layer, was fast but hard for engineers to use correctly: two data models, manual cache
filling, and frequent consistency bugs. TAO ("The Associations and Objects") is a custom
distributed service that hides this behind a simple graph API: **objects** (nodes) and
**associations** (edges). Underneath, data is split into hundreds of thousands of shards stored in
MySQL, with two tiers of write-through cache (followers and leaders) in every region. Each shard
has one primary region; MySQL replication copies its data to the others, and TAO chooses
eventual consistency by default because it prefers availability.

## Key takeaways
- **Read-dominated, uncacheable-ahead workload:** feeds are too personalised to precompute, so data is fetched live; reads vastly outnumber writes (billion reads vs millions of writes per second).
- **A cache needs an owner:** Memcache doesn't fill itself or stay consistent, so every product engineer had to get caching right — and many didn't. TAO moved that responsibility into one service.
- **Graph model:** typed objects + typed, time-ordered associations; inverse edges ("likes" / "liked by") are created automatically.
- **Simple API on purpose:** only point, range and count queries — no complex graph traversals during a user request.
- **Sharding + two cache tiers:** hundreds of thousands of shards; followers serve clients, leaders sit in front of MySQL and keep the region consistent.
- **Eventual consistency by default** (because of the CAP theorem), with "see your own writes" guaranteed with high probability and strong consistency as an opt-in.

## Concepts touched
[[tao]], [[graph-data-model]], [[sharding]], [[replication]], [[eventual-consistency]],
[[caching]], [[cache-patterns]], [[cache-invalidation]], [[redis-vs-memcached]]

## Open questions
- The full Usenix ATC '13 paper has the numbers (hit rates, latency) — worth adding as a source.
- How exactly do leaders invalidate follower caches across regions? The post doesn't say.
- The CAP theorem is cited but not explained; add a dedicated source on it.
