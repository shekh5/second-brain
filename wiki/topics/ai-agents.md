---
type: topic
tags: [ai-agents]
sources: [inside-the-software-factory, langchain-agent-development-lifecycle, atlan-adlc-vs-sdlc]
created: 2026-11-14
updated: 2026-11-14
---

# AI Agents — map

An **AI agent** is a program where a language model decides which steps to take and which tools
to call to reach a goal, rather than following fixed code (note: general knowledge, not from a source).
This page maps how agents are built, tested, shipped and run. ⬜ = no page yet (add a source!).

## 1. Agents in software delivery
- [[software-factory]] — a repeatable delivery loop where coding agents write more of the patches

## 2. The agent development lifecycle
- [[agent-development-lifecycle]] — build → test → deploy → monitor, then iterate; governance around it
- [[adlc-vs-sdlc]] — why agents need a different lifecycle than normal code
- [[agent-harness]] — build: frameworks vs runtimes vs harnesses
- [[agent-evaluation]] — test: datasets, metrics, experiments, simulations
- [[agent-runtime]] — deploy: durable execution, human-in-the-loop, sandboxes, context hub
- [[agent-observability]] — monitor: traces, signals, feedback, dashboards

## 3. Running agents safely
- [[agent-governance]] — cost, tool access + audit trails, discoverability
- ⬜ Prompt injection
- [[context-engineering]] — keep the agent's business context governed, versioned and fresh

## Suggested learning order
1. [[agent-development-lifecycle]] — the big picture first
2. [[adlc-vs-sdlc]]
3. [[agent-harness]]
4. [[agent-evaluation]]
5. [[context-engineering]]
6. [[agent-runtime]]
7. [[agent-observability]]
8. [[agent-governance]]
9. [[software-factory]] — the same loop applied to producing software with agents
