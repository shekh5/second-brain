---
type: concept
tags: [ai-agents, llm]
sources: [langchain-agent-development-lifecycle]
created: 2026-11-14
updated: 2026-11-14
---

# Agent development lifecycle (ADLC)

**In one line:** the repeatable loop for shipping AI agents — build, test, deploy, monitor, and
feed what you learn back into the next build.

## How it works
```
        ┌──────────── governance (cost · tool access · reuse) ────────────┐
        │                                                                  │
        │   Build ──► Test ──► Deploy ──► Monitor                          │
        │     ▲                              │                             │
        │     └──── iterate: failures become evals, fix, re-run ◄──┘        │
        └──────────────────────────────────────────────────────────────────┘
```
- **Build** — pick the level of abstraction: a framework, a runtime or a harness (see [[agent-harness]]), or a no-code tool so domain experts can take part (src: [[langchain-agent-development-lifecycle]]).
- **Test** — run the agent against a dataset of representative tasks with metrics, experiments and multi-turn simulations, *before* production (see [[agent-evaluation]]) (src: [[langchain-agent-development-lifecycle]]).
- **Deploy** — give it a runtime with durable execution, human-in-the-loop pauses, sandboxes and a context hub (see [[agent-runtime]]) (src: [[langchain-agent-development-lifecycle]]).
- **Monitor** — collect traces, signals and feedback, with dashboards and alerts (see [[agent-observability]]) (src: [[langchain-agent-development-lifecycle]]).
- **Iterate** — find the hard examples, understand why the agent failed, change the prompt / tools / retrieval / model, re-run the evals, redeploy. LangChain calls this "hill-climbing" (src: [[langchain-agent-development-lifecycle]]).
- **Govern** — around the whole loop: cost, tool access, discoverability (see [[agent-governance]]) (src: [[langchain-agent-development-lifecycle]]).

The order matters: testing starts before an agent reaches production (src: [[langchain-agent-development-lifecycle]]).

## Why it matters / when to use it
For one agent the process can stay light. Across many agents it becomes an infrastructure and
governance problem, so the best organisations build shared infrastructure for evals, deployment,
tracing and dashboards instead of each team rebuilding it (src: [[langchain-agent-development-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Turns one-off demos into a repeatable practice (src: [[langchain-agent-development-lifecycle]]) | Needs real infrastructure: datasets, tracing, runtime, dashboards (src: [[langchain-agent-development-lifecycle]]) |
| Ship early but not blindly — evals + monitoring catch regressions (src: [[langchain-agent-development-lifecycle]]) | Eval sets are never "done"; they must keep growing from production (src: [[langchain-agent-development-lifecycle]]) |
| Shared infrastructure lets many teams move fast (src: [[langchain-agent-development-lifecycle]]) | Heavy for a single small agent, where a lighter process is enough (src: [[langchain-agent-development-lifecycle]]) |

## Real-world examples
- LangChain's own stack maps onto it: LangChain/LangGraph/Deep Agents (build), LangSmith (test, monitor, deploy) (src: [[langchain-agent-development-lifecycle]]).
- Other tools named per stage: CrewAI and Claude Agent SDK (build); AWS AgentCore and Temporal (runtime); Daytona and E2B (sandboxes); n8n and Claude Cowork (no-code build) (src: [[langchain-agent-development-lifecycle]]).

## Related
[[software-factory]] — the same feedback loop, but for producing software with coding agents
[[agent-evaluation]] — the Test stage in detail
[[agent-observability]] — the Monitor stage in detail

## Sources
- [[langchain-agent-development-lifecycle]]
