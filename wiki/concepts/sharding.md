---
type: concept
tags: [system-design, databases, scalability]
sources: [tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# Sharding (partitioning)

**In one line:** split one big dataset into many smaller pieces (**shards**), each stored on a different server, so no single machine holds or serves everything.

## How it works

```
             all data
    ┌──────────┼──────────┐
 shard 1    shard 2    shard 3   …  (hundreds of thousands in TAO)
  DB A       DB B       DB C
```

A **shard key** (e.g. user ID) decides which shard a row lives in. Reads and writes for that
key go only to that shard's server. (note: general knowledge, not from a source)

In [[tao]], data is split into hundreds of thousands of shards. Everything in one shard lives in
the same MySQL database and is cached on the same set of servers. Objects can be placed in a
chosen shard when created, so related data sits together and fewer servers are contacted per
request. (src: [[tao-the-power-of-the-graph]])

## Why it matters / when to use it
When one database server can't keep up — too much data, too many writes, or too many reads
even with a [[caching|cache]] — you scale **horizontally** by adding servers and sharding.
(note: general knowledge, not from a source)

**Hot spots:** one shard can get far more traffic than others (a celebrity photo in tens of
millions of feeds). TAO handles this by migrating or cloning shards between servers to even out
the load. (src: [[tao-the-power-of-the-graph]])

## Trade-offs
| Pro | Con |
|---|---|
| Scale storage and throughput almost without limit | Queries across shards (joins, global counts) are slow and complex |
| A failure hits one shard, not everything | Hot shards need rebalancing (src: [[tao-the-power-of-the-graph]]) |
| Many small shards are easy to move around | Choosing a bad shard key is very costly to fix later |
| | Some data (like social graphs) doesn't split cleanly (src: [[tao-the-power-of-the-graph]]) |

## Real-world examples
- Facebook [[tao]]: hundreds of thousands of MySQL shards. (src: [[tao-the-power-of-the-graph]])
- Instagram shards PostgreSQL by user ID; MongoDB and Cassandra shard automatically. (note: general knowledge, not from a source)

## Related
- [[replication]] — copies a shard; sharding splits data. Real systems use both.
- Consistent hashing — a common way to map keys to shards (no page yet)

## Sources
- [[tao-the-power-of-the-graph]]
