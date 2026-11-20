---
type: topic
tags: [ai-agents]
sources: [inside-the-software-factory, langchain-agent-development-lifecycle, atlan-adlc-vs-sdlc, google-automate-agent-lifecycle, lean4-formal-verification-for-engineers, self-improvement-memory-crsi, lovable-set-intelligence-free]
created: 2026-11-14
updated: 2026-11-20
---

# AI Agents — map

An **AI agent** is a program where a language model decides which steps to take and which tools
to call to reach a goal, rather than following fixed code (note: general knowledge, not from a source).
This page maps how agents are built, tested, shipped and run. ⬜ = no page yet (add a source!).

## 1. Agents in software delivery
- [[software-factory]] — a repeatable delivery loop where coding agents write more of the patches
- [[formal-verification]] — prove agent-written code meets a human-owned spec (Lean, Verus, kernels)
- [[differential-testing]] — compare production code with a reference model on millions of random inputs

## 2. The agent development lifecycle
- [[agent-development-lifecycle]] — build → test → deploy → monitor, then iterate; governance around it
- [[adlc-vs-sdlc]] — why agents need a different lifecycle than normal code
- [[agent-harness]] — build: frameworks vs runtimes vs harnesses
- [[agent-evaluation]] — test: datasets, metrics, experiments, simulations
- [[agent-runtime]] — deploy: durable execution, human-in-the-loop, sandboxes, context hub
- [[long-running-agent]] — agents that work for hours/days: inboxes, forkable histories, checkpointed sandboxes
- [[copy-on-write]] — the trick that makes forking a whole agent sandbox cheap
- [[agent-observability]] — monitor: traces, signals, feedback, dashboards

## 3. Running agents safely
- [[agent-governance]] — cost, tool access + audit trails, discoverability
- [[prompt-injection]] — hidden instructions in text the agent reads; screen it, limit privileges
- [[grounding]] — facts come from tools/code, the model only narrates
- [[context-engineering]] — keep the agent's business context governed, versioned and fresh

## 4. Agents that improve themselves
- [[recursive-self-improvement]] — LLMs propose, test and keep edits to the harness, round after round
- [[self-improvement-memory]] — the optimizer's diary of problems, edits and outcomes; lets improvement continue after a model/benchmark change

## Suggested learning order
1. [[agent-development-lifecycle]] — the big picture first
2. [[adlc-vs-sdlc]]
3. [[agent-harness]]
4. [[agent-evaluation]]
5. [[grounding]]
6. [[context-engineering]]
7. [[agent-runtime]]
8. [[long-running-agent]]
9. [[agent-observability]]
10. [[agent-governance]]
11. [[prompt-injection]]
12. [[software-factory]] — the same loop applied to producing software with agents
13. [[formal-verification]] — how to trust what the factory produces
14. [[differential-testing]]
15. [[recursive-self-improvement]] — after harness + evaluation make sense
16. [[self-improvement-memory]]
