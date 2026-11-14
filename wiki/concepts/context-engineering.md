---
type: concept
tags: [ai-agents, llm, data, governance]
sources: [atlan-adlc-vs-sdlc, langchain-agent-development-lifecycle]
created: 2026-11-14
updated: 2026-11-14
---

# Context engineering

**In one line:** building, versioning and maintaining the information an agent reasons with —
business definitions, data descriptions, policies, prompts — so its answers stay correct.

## How it works
An agent's output depends on the context it is given at runtime, not only on its code (src: [[atlan-adlc-vs-sdlc]]).
Context engineering treats that context (the **context layer**) as an engineered artifact with its
own lifecycle, just like code (src: [[atlan-adlc-vs-sdlc]]):

```
 build ──► test ──► version ──► deploy ──► observe ──► improve
   ▲                                                      │
   └──────────── business/data changes trigger ◄──────────┘
```

- **Governed context vs raw schema:** an agent asked a business question should reason over curated definitions ("what counts as an active customer"), not just database column names (src: [[atlan-adlc-vs-sdlc]]).
- **Context drift:** when the business or data changes but the context does not, the agent's answers slowly degrade. Drift monitoring catches this (see [[agent-observability]]) (src: [[atlan-adlc-vs-sdlc]]).
- **Context hub:** LangChain describes a related idea at deploy time — a versioned store for prompts, skills and instructions that domain experts can edit without a redeploy (src: [[langchain-agent-development-lifecycle]]).

## Why it matters / when to use it
Atlan argues the main cause of failed agent projects is missing or stale context, not weak models
or prompts, and that most ADLC frameworks prescribe evaluation harnesses but skip *what* the
harness evaluates against (src: [[atlan-adlc-vs-sdlc]]). A common saying in data teams: "the agent is easy to build now;
getting business context into it is the hard part" (src: [[atlan-adlc-vs-sdlc]]).

## Trade-offs
| Pro | Con |
|---|---|
| Grounded answers that match business reality (src: [[atlan-adlc-vs-sdlc]]) | A continuous discipline with real ongoing cost, not a one-time setup (src: [[atlan-adlc-vs-sdlc]]) |
| Atlan reports 38% better SQL accuracy with governance metadata vs raw schema (src: [[atlan-adlc-vs-sdlc]]) | That figure is from the vendor's own research — not independently verified |
| Makes evaluation meaningful (testing against the right truth) (src: [[atlan-adlc-vs-sdlc]]) | Needs cross-functional ownership (engineering + data + AI ops) (src: [[atlan-adlc-vs-sdlc]]) |

## Real-world examples
- Workday and DigiKey are quoted as using Atlan as a shared "context layer" exposed to AI tools via an MCP server (src: [[atlan-adlc-vs-sdlc]]).
- Stale schema causing a contract-analysis agent to hallucinate contract terms (src: [[atlan-adlc-vs-sdlc]]).

## Related
[[adlc-vs-sdlc]] — the context layer is the artifact SDLC never had
[[agent-evaluation]] — evals are only as good as the context they test against
[[agent-development-lifecycle]] — context runs through every stage

## Sources
- [[atlan-adlc-vs-sdlc]]
- [[langchain-agent-development-lifecycle]]
