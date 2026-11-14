---
type: concept
tags: [system-design, databases, data-modeling]
sources: [tao-the-power-of-the-graph]
created: 2026-11-14
updated: 2026-11-14
---

# Graph data model

**In one line:** store data as **nodes** (things) and **edges** (relationships between things) instead of rows in tables.

## How it works

```
 (Alice) ──checked in at──► (Golden Gate check-in) ◄──commented── (Cathy)
    │                              ▲
    └──tagged──► (Bob)             └──liked── (David)
```

In [[tao]], every node is a typed **object** with named fields (a user, a check-in, a comment),
and every edge is a typed **association** (likes, friend-of, tagged). Two objects can be linked by
several edges as long as each edge has a different type. (src: [[tao-the-power-of-the-graph]])

- **Inverse edges:** define "likes" with inverse "liked by", and creating one edge automatically creates the other, so you can walk the graph both ways. (src: [[tao-the-power-of-the-graph]])
- **Time on every edge:** associations carry a time (usually creation time), so lists like "newest comments" are cheap. (src: [[tao-the-power-of-the-graph]])
- **Flexible schema:** new fields can be added to an object type at any time without database migrations. (src: [[tao-the-power-of-the-graph]])

## Why it matters / when to use it
Use it when **relationships are the main data**: social networks, recommendations, fraud rings,
knowledge graphs. Questions like "friends of friends who like X" are natural on a graph and
painful with many SQL joins. (note: general knowledge, not from a source)

## Trade-offs
| Pro | Con |
|---|---|
| Relationships are first-class and fast to follow | Hard to shard: social graphs don't split cleanly (src: [[tao-the-power-of-the-graph]]) |
| Flexible schema, easy to add new types | Deep traversals are expensive at scale — TAO bans them in user requests (src: [[tao-the-power-of-the-graph]]) |
| Maps directly to how product teams think | Fewer mature tools than relational databases |

## Real-world examples
- Facebook's [[tao]]: objects and associations over sharded MySQL. (src: [[tao-the-power-of-the-graph]])
- Neo4j and Amazon Neptune are dedicated graph databases. (note: general knowledge, not from a source)

## Related
- [[tao]] — a large-scale implementation
- [[sharding]] — why graphs are hard to split

## Sources
- [[tao-the-power-of-the-graph]]
