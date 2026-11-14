---
type: concept
tags: [system-design, databases, availability]
sources: [tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# Replication

**In one line:** keep copies of the same data on several servers (or regions), so you can read from many places and survive a failure.

## How it works — primary/secondary

```
  writes ──► PRIMARY (region A) ──replicate──► SECONDARY (region B)
                                 └─replicate──► SECONDARY (region C)
  reads  ──► any copy (secondaries may be slightly behind)
```

In [[tao]], each shard has **one primary region**. MySQL replication copies its updates to all
other (secondary) regions. A secondary region can't change the shard itself; it forwards writes
to the primary. If a MySQL server fails, an automated process can make another region the primary.
(src: [[tao-the-power-of-the-graph]])

Because copies update a little later than the primary, readers in other regions can briefly see
old data — this is [[eventual-consistency]]. TAO's write-through cache helps a user who wrote in
a secondary region still read their own write. (src: [[tao-the-power-of-the-graph]])

## Why it matters / when to use it
- **Availability:** if one copy dies, another takes over (failover).
- **Read scaling:** spread reads across many copies.
- **Low latency:** serve users from a nearby region.
(note: general knowledge, not from a source)

## Trade-offs
| Pro | Con |
|---|---|
| Survives server and region failures | Copies lag behind: stale reads |
| More read capacity | Writes still go to one primary (bottleneck, cross-region latency) |
| Users read from a nearby copy | Failover is tricky (risk of two primaries or lost writes) |
| | More storage cost |

## Real-world examples
- Facebook [[tao]]: one primary region per shard, MySQL replication to the rest. (src: [[tao-the-power-of-the-graph]])
- Most managed databases (Amazon RDS read replicas, PostgreSQL streaming replication) work the same way. (note: general knowledge, not from a source)

## Related
- [[sharding]] — splits data; replication copies each piece
- [[eventual-consistency]] — the consistency you get from async replication

## Sources
- [[tao-the-power-of-the-graph]]
