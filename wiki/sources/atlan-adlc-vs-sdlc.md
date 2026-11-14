---
type: source
tags: [ai-agents, llm, software-engineering, governance]
sources: []
created: 2026-11-14
updated: 2026-11-14
---

# ADLC vs SDLC: How the Agent Development Lifecycle Differs (Atlan, 2026)

- **Raw file:** `raw/articles/2026-11-14-adlc-vs-sdlc.md`
- **Author / origin:** Emily Winks, Atlan, published 2026-06-16 (updated 2026-09-21) — https://atlan.com/know/ai-agent/adlc-vs-sdlc/
- **Ingested:** 2026-11-14 (received via Telegram)

## Summary
The classic **software development lifecycle (SDLC)** assumes code is *deterministic*: same input,
same output, so tests can be pass/fail. AI agents are *probabilistic*: their output changes with
context quality, model state and tool availability. The **agent development lifecycle (ADLC)**
therefore ships three things — code, a governed **context layer**, and an **evaluation suite** —
measures quality as a *distribution* against thresholds, and keeps calibrating context after
launch. Most enterprise programs need both: SDLC for the infrastructure, ADLC for the agent
behaviour. The article argues most ADLC efforts fail because agents are evaluated against raw
database schema rather than governed business context. Atlan sells a "context layer" product,
so this framing is promotional, and several statistics come from Atlan's own research.

## Key takeaways
- **Three structural differences:** artifact (code vs code + context + evals), testing (pass/fail vs evaluation distributions), production (versioned releases vs continuous context calibration).
- **New failure modes:** context drift, stale schema, hallucination and cost overruns — none caught by binary tests.
- **Token economics:** a prompt design can pass every SDLC gate yet be too expensive at production volume; ADLC checks cost per task in the inner loop.
- **Context is a lifecycle, not a setup step:** build, test, version, deploy and observe it like code.
- **Origins:** term used by Sierra (2024) and Arthur.ai (2024–25); formalised by Glean (7 stages), Salesforce (5 phases), IBM and others. Vocabulary is still settling. Not the same as "AI-SDLC" (using AI to help write normal software).

## Concepts touched
[[adlc-vs-sdlc]], [[agent-development-lifecycle]], [[context-engineering]], [[agent-evaluation]],
[[agent-observability]], [[agent-governance]], [[agent-harness]]

## Open questions
- Statistics to double-check: Gartner (>40% of agentic AI projects cancelled by end of 2027), McKinsey (62% experimenting vs ~23% scaling), "88% never reach production" and the "38% SQL accuracy gain" (both from Atlan's own research).
- Original ADLC posts by Sierra, Arthur.ai and Glean are cited — worth adding as sources.
