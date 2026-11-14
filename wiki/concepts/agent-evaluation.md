---
type: concept
tags: [ai-agents, llm, evaluation, testing]
sources: [langchain-agent-development-lifecycle, atlan-adlc-vs-sdlc]
created: 2026-11-14
updated: 2026-11-14
---

# Agent evaluation (evals)

**In one line:** testing an agent by running it on a set of example tasks and scoring the results,
so you know if a change made it better or worse.

## How it works
```
 examples (dogfooding, tickets, traces, edge cases)
        │
        ▼
   dataset ──► run agent version A and B ──► metrics ──► compare (experiment)
        ▲                                                   │
        └──────── hardest production failures added ◄───────┘
```
- **Dataset:** a small set of representative tasks, from expected use, manual testing, dogfooding (using your own product), support tickets, past traces and edge cases. Datasets *preserve what you learned*, so old failures don't come back after a prompt or model change (src: [[langchain-agent-development-lifecycle]]).
- **Metrics:** when there is a ground truth (right value, right label, right field) score correctness directly; when there isn't (a summary, a reply), use **criteria-based** checks — was it grounded, did it follow policy, ask for clarification, avoid needless tool calls (src: [[langchain-agent-development-lifecycle]]).
- **Experiments:** compare prompts, models, retrieval strategies, tool schemas and orchestration against the *same* dataset to see improvement or regression (src: [[langchain-agent-development-lifecycle]]).
- **Simulations:** multi-turn agents (support, coding, voice) need simulated end-to-end conversations; single-turn evals are not enough (src: [[langchain-agent-development-lifecycle]]).
- **LLM-as-judge:** a second model scores outputs against criteria (used heavily in monitoring too, see [[agent-observability]]) (src: [[langchain-agent-development-lifecycle]]).

- **Distributions, not pass/fail:** because agents are non-deterministic, ADLC measures the *spread* of quality across many scenarios and checks it stays above a threshold — accurate, grounded and cost-viable (src: [[atlan-adlc-vs-sdlc]]).
- **Token economics:** measure cost per task at expected production volume during development; a prompt that works in testing can be unaffordable at scale (src: [[atlan-adlc-vs-sdlc]]).
- **Evaluate against the right truth:** the harness is only meaningful if the agent has governed business context, not raw schema (see [[context-engineering]]) (src: [[atlan-adlc-vs-sdlc]]).

## Why it matters / when to use it
Arthur.ai's CEO calls a well-curated eval suite the single most important predictor of an agent's success {A}. Before deploying, you need a way to tell if an agent is ready — not a perfect suite, but enough to
catch obvious failures, compare versions and avoid shipping blind. It replaces "vibes" with data (src: [[langchain-agent-development-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Catches regressions after prompt/model/tool changes (src: [[langchain-agent-development-lifecycle]]) | A dataset is only as good as the examples in it; it must keep growing (src: [[langchain-agent-development-lifecycle]]) |
| Lets you compare versions objectively (src: [[langchain-agent-development-lifecycle]]) | Criteria-based and LLM-judge scores are softer than exact-match (src: [[langchain-agent-development-lifecycle]]) |
| Simulations test real multi-turn behaviour (src: [[langchain-agent-development-lifecycle]]) | Simulations cost more to build and run (note: general knowledge, not from a source) |

## Real-world examples
- A support agent simulated against a frustrated customer: ask follow-ups, check order status, decide whether to escalate (src: [[langchain-agent-development-lifecycle]]).
- A coding agent: inspect a repo, change code, run tests, respond to feedback (src: [[langchain-agent-development-lifecycle]]).

## Related
[[adlc-vs-sdlc]] — why pass/fail tests aren't enough for agents
[[agent-development-lifecycle]] — evaluation is the Test stage
[[agent-observability]] — production traces feed new eval examples

## Sources
- [[langchain-agent-development-lifecycle]]
- [[atlan-adlc-vs-sdlc]]
