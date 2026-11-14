---
type: concept
tags: [ai-agents, llm, observability, monitoring]
sources: [langchain-agent-development-lifecycle, atlan-adlc-vs-sdlc]
created: 2026-11-14
updated: 2026-11-14
---

# Agent observability (traces, signals, feedback)

**In one line:** recording everything an agent did in production — every model call and tool call —
so you can see whether it actually did the task, not just whether it responded.

## How it works
- **Trace:** the full trajectory of one run — inputs, model calls, tool calls and their outputs, and the final answer or action. "The improvement loop starts with a trace" (src: [[langchain-agent-development-lifecycle]]).
- **Signals:** scores harvested from traces, by an LLM judge (did it answer, follow policy, use the right tone) or a simple regex (was a forbidden tool called, did a required phrase appear). Signals double as product analytics: what users ask, where agents get stuck (src: [[langchain-agent-development-lifecycle]]).
- **Feedback:** user ratings, human reviews and judge scores stored *with* the trace, linking "the user was unhappy" to "it used the wrong tool three steps earlier" (src: [[langchain-agent-development-lifecycle]]).
- **Drift monitoring:** track output quality over time as data, schemas, business definitions or the model change; catch regressions before users do and trigger context recalibration. Normal software has no equivalent because it doesn't depend on runtime context (src: [[atlan-adlc-vs-sdlc]]).
- **Dashboards and alerts:** usage, feedback, latency, cost, tool calls, evaluator scores and recurring failures; alert on rising cost or latency, failing tools, falling feedback, policy-violation spikes (src: [[langchain-agent-development-lifecycle]]).

## Why it matters / when to use it
Classic metrics (latency, cost, error rate, uptime) still matter but are not enough: an agent can
return a "successful" response and still call the wrong tool, use the wrong context, skip an
approval or give a plausible but wrong answer (src: [[langchain-agent-development-lifecycle]]). Important traces become eval examples, so
monitoring feeds [[agent-evaluation]] (src: [[langchain-agent-development-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Shows *why* an agent failed, step by step (src: [[langchain-agent-development-lifecycle]]) | Full traces are large and may hold sensitive data (note: general knowledge, not from a source) |
| Turns production failures into future evals (src: [[langchain-agent-development-lifecycle]]) | Judge-based signals can themselves be wrong (note: general knowledge, not from a source) |
| Doubles as product analytics (src: [[langchain-agent-development-lifecycle]]) | Needs a pipeline: storage, feedback API, dashboards (src: [[langchain-agent-development-lifecycle]]) |

## Real-world examples
- LangSmith lets teams attach user feedback directly to the underlying run (src: [[langchain-agent-development-lifecycle]]).

## Related
[[agent-development-lifecycle]] — the Monitor stage
[[agent-governance]] — audit trails of tool calls rely on the same traces

## Sources
- [[langchain-agent-development-lifecycle]]
- [[atlan-adlc-vs-sdlc]]
