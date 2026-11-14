---
type: topic
tags: [ai-agents]
sources: [inside-the-software-factory, langchain-agent-development-lifecycle]
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
- [[agent-harness]] — build: frameworks vs runtimes vs harnesses
- [[agent-evaluation]] — test: datasets, metrics, experiments, simulations
- [[agent-runtime]] — deploy: durable execution, human-in-the-loop, sandboxes, context hub
- [[agent-observability]] — monitor: traces, signals, feedback, dashboards

## 3. Running agents safely
- [[agent-governance]] — cost, tool access + audit trails, discoverability
- ⬜ Prompt injection
- ⬜ Context engineering

## Suggested learning order
1. [[agent-development-lifecycle]] — the big picture first
2. [[agent-harness]]
3. [[agent-evaluation]]
4. [[agent-runtime]]
5. [[agent-observability]]
6. [[agent-governance]]
7. [[software-factory]] — the same loop applied to producing software with agents
