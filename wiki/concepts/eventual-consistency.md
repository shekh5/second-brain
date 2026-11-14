---
type: concept
tags: [system-design, distributed-systems, consistency]
sources: [tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# Eventual consistency

**In one line:** after a write, different copies of the data may disagree for a short time, but if no new writes come in they will all end up the same.

## How it works

```
t=0  Alice likes a post   → primary: likes=101
t=0  Bob in another region → copy:    likes=100  (stale)
t=1s replication arrives   → copy:    likes=101  (consistent again)
```

The opposite is **strong consistency**: every read sees the latest write, which needs
coordination between copies and is slower or less available. (note: general knowledge, not from a source)

## Why it matters / when to use it
In a distributed system, machine failures and network splits ("partitions") are near-certain.
The **CAP theorem** says that during a partition you must choose between consistency and
availability. Facebook's [[tao]] picks availability: briefly losing consistency is "a lesser evil
than losing availability". (src: [[tao-the-power-of-the-graph]])

TAO softens this with two rules (src: [[tao-the-power-of-the-graph]]):
- **Read-your-own-writes:** it tries hard to make sure users always see their own updates.
- **Opt-in strong consistency** for the few cases that need it, at a higher cost and possible loss of availability.

Good fit: like counts, feeds, comments, view counts. Bad fit: bank balances, stock levels, seat
booking. (note: general knowledge, not from a source)

## Trade-offs
| Pro | Con |
|---|---|
| Stays available during failures | Users can see stale or out-of-order data |
| Fast reads and writes (no waiting for other copies) | App code must tolerate inconsistency |
| Scales across regions | Hard bugs ("I posted but it disappeared") without read-your-own-writes |

## Real-world examples
- Facebook [[tao]]: eventual consistency by default. (src: [[tao-the-power-of-the-graph]])
- DNS, Amazon DynamoDB (default reads) and Cassandra are eventually consistent. (note: general knowledge, not from a source)

## Related
- [[replication]] — async replication is what causes the delay
- [[cache-invalidation]] — a stale cache is the same problem in a smaller form
- CAP theorem — the reason for the trade-off (no page yet)

## Sources
- [[tao-the-power-of-the-graph]]
