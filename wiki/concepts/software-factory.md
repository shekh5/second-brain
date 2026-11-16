---
type: concept
tags: [ai-agents, software-engineering, devops]
sources: [inside-the-software-factory, lean4-formal-verification-for-engineers]
created: 2026-11-14
updated: 2026-11-16
---

# Software factory

**In one line:** a managed, repeatable system for producing software — standard inputs and tools,
measurable output, and saved context so you can rebuild how any change was made.

## How it works
Every change follows the same path, and production feeds the next change (src: [[inside-the-software-factory]]):

```
 bug report / feedback / requirement
            │
            ▼
   scope ─► plan ─► implement ─► test ─► review ─► secure ─► ship
                                                              │
            ▲                                                 ▼
            └──────────── new signals ◄──────── monitor in production
```

- **Repeatable inputs:** a request carries enough detail to reproduce or scope it (src: [[inside-the-software-factory]]).
- **Same gates for everyone:** an agent-written patch faces the same tests, security checks and release controls as a human one (src: [[inside-the-software-factory]]).
- **Measurable output:** CI and source-control records show which checks passed and which revision was approved; useful measures separate time *generating* a patch from time *correcting and reviewing* it (src: [[inside-the-software-factory]]).
- **Replayability:** keep the starting revision, environment, constraints, model configuration, commands and resulting patch. A re-run of the model may still produce a different patch (src: [[inside-the-software-factory]]).

The **agent-native** version (sold by the company Factory, with agents called "Droids") lets coding
agents do more of the investigation and implementation, not just build/test/deploy automation
(src: [[inside-the-software-factory]]). Factory names three requirements: *model independence* (swap models
per task), *sovereign intelligence* (you control the system and what it learns), and *continual
learning* (an incident improves a test or a review instruction) (src: [[inside-the-software-factory]]).

## Why it matters / when to use it
When requests, repositories and contributors multiply, delivery must stay dependable. The value
shows when the next incident improves the process instead of forcing the same investigation
again (src: [[inside-the-software-factory]]).

Getting started: choose a recurring task with an existing reproduction and test command, let the
agent prepare the patch, keep human review, and look at what had to be corrected. Turn repeated
mistakes into tests or checks; fix broken setup before adding volume (src: [[inside-the-software-factory]]).

## Trade-offs
| Pro | Con |
|---|---|
| Agents take on investigation + coding, so more patches flow | The bottleneck moves to tests, environments and review capacity (src: [[inside-the-software-factory]]) |
| One path for every change → auditable, replayable | Needs deliberate integration work to record all the context (src: [[inside-the-software-factory]]) |
| Production feedback continually improves the process | More sessions can't fix validation that can't tell "correct" from "plausible" (src: [[inside-the-software-factory]]) |
| Self-hosting keeps control of code and data | Self-hosting means you own updates and recovery (src: [[inside-the-software-factory]]) |

## Real-world examples
- **History:** Robert Bemer wrote about a software factory at General Electric in the late 1960s; Hitachi opened its Software Works in 1969; Michael Cusumano's 1991 book *Japan's Software Factories* studied the idea (src: [[inside-the-software-factory]]).
- **Chainguard:** one two-week agent session spanned six repositories and built 80 packages (src: [[inside-the-software-factory]]).
- **Groq, Empower, Nav:** report faster features and shorter incident response — self-reported by the vendor's customers, not universal benchmarks (src: [[inside-the-software-factory]]).

## Related
[[formal-verification]] — proving agent-written code correct, since tests and human review can't keep up with agent throughput (src: [[lean4-formal-verification-for-engineers]])
[[agent-development-lifecycle]] — the same build → test → ship → monitor loop, applied to building agents themselves

## Sources
- [[inside-the-software-factory]]
