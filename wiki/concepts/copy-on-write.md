---
type: concept
tags: [system-design, operating-systems, sandboxes, ai-agents]
sources: [lovable-set-intelligence-free]
created: 2026-11-20
updated: 2026-11-20
---

# Copy-on-write (CoW)

**In one line:** when you copy something, don't really copy it yet — share the original and only
make a private copy of a piece at the moment someone changes it.

## How it works
(note: general knowledge, not from a source — the source only names the technique)

Memory (or disk) is split into **pages** (blocks). A "fork" just points to the parent's pages
and marks them read-only. The first write to a page triggers a fault; the system copies just that
page and lets the writer change its own copy.

```
 before write:   parent ─┐
                         ├──► [A][B][C]   (shared, read-only)
 fork ───────────────────┘

 fork writes B:  parent ───► [A][B][C]
                 fork   ───► [A][B'][C]   (only B copied)
```

## Why it matters / when to use it
- Makes a **fork** almost instant and nearly free, no matter how big the original is (note: general knowledge, not from a source).
- Lovable uses copy-on-write memory to fork agent sandboxes — so an agent's whole computer can be branched to explore another path (src: [[lovable-set-intelligence-free]]).
- Use it when you make many copies that mostly stay the same: process forks, VM/sandbox snapshots, database snapshots, immutable data structures (note: general knowledge, not from a source).

## Trade-offs
| Pro | Con |
|---|---|
| Fork in milliseconds, little extra memory (note: general knowledge, not from a source) | The first write to each page is slower (a fault + copy) (note: general knowledge, not from a source) |
| Many forks share most data → big savings at scale (note: general knowledge, not from a source) | Memory use grows unpredictably as forks diverge (note: general knowledge, not from a source) |
| Snapshots are cheap, so checkpoint/restore becomes practical (note: general knowledge, not from a source) | Long chains of snapshots get fragmented and need compaction (note: general knowledge, not from a source) |

## Real-world examples
- Unix `fork()` shares the parent's memory pages copy-on-write (note: general knowledge, not from a source).
- File systems ZFS and Btrfs, and VM disk snapshots, are copy-on-write (note: general knowledge, not from a source).
- **Lovable** forks agent sandboxes using copy-on-write memory (src: [[lovable-set-intelligence-free]]).

## Related
[[long-running-agent]] — forking agents' machines is one use
[[agent-runtime]] — sandboxes are part of the runtime
[[replication]] — the opposite choice: copy everything up front

## Sources
- [[lovable-set-intelligence-free]]
