---
type: source
tags: [ai-agents, software-engineering, devops]
sources: []
created: 2026-11-14
updated: 2026-11-14
---

# Inside the software factory, and what it takes to build one (Factory, 2026)

- **Raw file:** `raw/articles/2026-11-14-software-factory.md`
- **Author / origin:** Factory (factory.com) company article, 2026-07-18 — https://factory.com/articles/what-is-a-software-factory
- **Ingested:** 2026-11-14 (received via Telegram)

## Summary
A **software factory** is a managed way of producing software: repeatable inputs, standard
tooling, measurable output, and enough saved context to rebuild how any change was made. The
idea is old (General Electric in the late 1960s, Hitachi's Software Works in 1969). Factory, a
company that sells coding agents called "Droids", describes an **agent-native** version where
delivery is a continuous loop: bug reports and feedback become planned changes, which are built,
tested, reviewed, secured and shipped, and production monitoring produces the next request.
Agents take over more of the investigation and coding, but the same tests, reviews and release
controls still decide what ships. Note: it is a vendor article, and its customer numbers are
self-reported.

## Key takeaways
- **The pattern is the same whether a human or an agent writes the patch.** What changes is how much the agent does, and whether the checks around it can catch a "plausible but wrong" change.
- **The bottleneck moves.** Faster patch writing exposes missing tests, slow environments and limited review capacity. More agent sessions won't fix weak validation.
- **Replayability:** keep the starting revision, environment, task constraints, model configuration, commands and resulting patch. Even then, a re-run of the model may not give the same patch.
- **Three stated requirements:** model independence, "sovereign intelligence" (you control the system and the knowledge it gathers), and continual learning (an incident improves a test or a review rule).
- **Start small:** pick a recurring task that already has a reproduction and a test command; turn repeated mistakes into tests or enforced checks; fix the environment before increasing volume.

## Concepts touched
[[software-factory]], [[agent-development-lifecycle]]

## Open questions
- Customer figures (Groq 3–5x faster, Empower −40% incident time, Nav 2x velocity) are vendor-published and workflow-specific; not benchmarks.
- How "measurable output" is actually measured (Factory's "Agent Effectiveness") is not explained.
