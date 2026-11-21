---
type: comparison
tags: [ai-agents, llm, software-engineering]
sources: [atlan-adlc-vs-sdlc, langchain-agent-development-lifecycle]
created: 2026-11-14
updated: 2026-11-21
---

# ADLC vs SDLC

The **SDLC** (software development lifecycle) is how teams plan, build, test and release normal
code. The [[agent-development-lifecycle|ADLC]] (agent development lifecycle) is how teams build,
evaluate and run AI agents. They share phase names (plan, build, test, deploy, monitor) but differ
in *what* they ship and *how they define done* (src: [[atlan-adlc-vs-sdlc]]).

The root difference: normal code is **deterministic** (same input → same output), agents are
**non-deterministic** (same input → possibly different output, depending on context, model state,
prompt wording and tool availability) (src: [[atlan-adlc-vs-sdlc]]).

| Dimension | SDLC | ADLC |
|---|---|---|
| What it engineers | deterministic code | probabilistic agent behaviour (src: [[atlan-adlc-vs-sdlc]]) |
| Primary artifact | source code + tests | code + context layer + evaluation suite (src: [[atlan-adlc-vs-sdlc]]) |
| Testing | binary pass/fail (unit, integration, regression) | evaluation *distributions* against quality thresholds (src: [[atlan-adlc-vs-sdlc]]) |
| Question asked | does the code do what the spec says? | is the output accurate, grounded and cost-viable? (src: [[atlan-adlc-vs-sdlc]]) |
| Deployment | version-gated releases | continuous deployment with context calibration (src: [[atlan-adlc-vs-sdlc]]) |
| Context at runtime | none — behaviour is in the code | first-class: governed, versioned business context (src: [[atlan-adlc-vs-sdlc]]) |
| Governance | code review, audit trail, access control | + context governance, drift monitoring, token economics (src: [[atlan-adlc-vs-sdlc]]) |
| Failure modes | bug, crash, regression, logic error | context drift, stale schema, hallucination, cost overrun (src: [[atlan-adlc-vs-sdlc]]) |
| Maturity measure | code coverage, regression pass rate | eval stability, context freshness, cost per task (src: [[atlan-adlc-vs-sdlc]]) |
| Ownership | software engineering team | cross-functional: engineering + data + AI ops (src: [[atlan-adlc-vs-sdlc]]) |
| Age | mature (Waterfall 1970s, Agile 1990s–2000s) | 2–3 years as a named practice (src: [[atlan-adlc-vs-sdlc]]) |

"Done" in SDLC = a passing test suite and a deployed version. "Done" in ADLC = an evaluation
distribution that *stays* above a threshold in production (src: [[atlan-adlc-vs-sdlc]]).

## When to pick SDLC
- Deterministic, rule-based automation: infrastructure tools, APIs, data pipelines where behaviour is fully specified (src: [[atlan-adlc-vs-sdlc]]).
- Don't apply heavy ADLC evaluation to code that behaves deterministically — that over-engineers it (src: [[atlan-adlc-vs-sdlc]]).

## When to pick ADLC
- Any agent that takes natural-language goals, uses an LLM, calls tools, or whose output quality depends on context quality (src: [[atlan-adlc-vs-sdlc]]).

## When you need both (almost always)
Most real programs run them in parallel: the pipelines, APIs and tools the agent uses follow SDLC;
the agent's behaviour follows ADLC. Example: an API is built and contract-tested under SDLC, then
tested *as an agent tool* (permission boundaries, cost per call) under ADLC (src: [[atlan-adlc-vs-sdlc]]).

## Example
A financial-services contract-analysis agent passed every SDLC gate (unit tests, security review,
staging). ADLC evaluation then showed (1) the prompt design was too expensive at production volume
and (2) the agent hallucinated contract terms when the context layer returned a stale schema.
Neither problem is visible to pass/fail tests (src: [[atlan-adlc-vs-sdlc]]).

## Don't confuse with
[[ai-native-sdlc]] — the normal SDLC *run by coding agents* (intent → spec → plan → code → gated deploy). This page is about the lifecycle *of an agent* as a product.

## Sources
- [[atlan-adlc-vs-sdlc]]
- [[langchain-agent-development-lifecycle]]
