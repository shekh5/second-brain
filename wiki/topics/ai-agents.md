---
type: topic
tags: [ai-agents]
sources: [inside-the-software-factory, langchain-agent-development-lifecycle, atlan-adlc-vs-sdlc, google-automate-agent-lifecycle, lean4-formal-verification-for-engineers, self-improvement-memory-crsi, lovable-set-intelligence-free, cognition-40x-merged-prs, anatomy-of-effective-commerce-agents]
created: 2026-11-14
updated: 2026-11-21
---

# AI Agents — map

An **AI agent** is a program where a language model decides which steps to take and which tools
to call to reach a goal, rather than following fixed code (note: general knowledge, not from a source).
This page maps how agents are built, tested, shipped and run. ⬜ = no page yet (add a source!).

## 1. Agents in software delivery
- [[software-factory]] — a repeatable delivery loop where coding agents write more of the patches
- [[ephemeral-environment]] — throw-away VMs with every service, rebuilt often, so agents can test their own work
- [[formal-verification]] — prove agent-written code meets a human-owned spec (Lean, Verus, kernels)
- [[differential-testing]] — compare production code with a reference model on millions of random inputs

## 2. The agent development lifecycle
- [[agent-development-lifecycle]] — build → test → deploy → monitor, then iterate; governance around it
- [[adlc-vs-sdlc]] — why agents need a different lifecycle than normal code
- [[agent-harness]] — build: frameworks vs runtimes vs harnesses
- [[agent-skill]] — build: instructions loaded on demand; one agent + skills beats many subagents for commerce
- [[agent-memory]] — build: typed per-user facts in your own DB, user can view/delete
- [[agent-evaluation]] — test: datasets, metrics, experiments, simulations
- [[agent-runtime]] — deploy: durable execution, human-in-the-loop, sandboxes, context hub
- [[long-running-agent]] — agents that work for hours/days: inboxes, forkable histories, checkpointed sandboxes
- [[copy-on-write]] — the trick that makes forking a whole agent sandbox cheap
- [[agent-observability]] — monitor: traces, signals, feedback, dashboards

## 3. Running agents safely
- [[agent-governance]] — cost, tool access + audit trails, discoverability
- [[prompt-caching]] — the main cost lever: stable prompt prefix, 90–99% cache hits
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
4. [[agent-skill]]
5. [[agent-memory]]
6. [[agent-evaluation]]
7. [[grounding]]
8. [[context-engineering]]
9. [[agent-runtime]]
10. [[long-running-agent]]
11. [[agent-observability]]
12. [[agent-governance]]
13. [[prompt-caching]]
14. [[prompt-injection]]
15. [[software-factory]] — the same loop applied to producing software with agents
16. [[ephemeral-environment]]
17. [[formal-verification]] — how to trust what the factory produces
18. [[differential-testing]]
19. [[recursive-self-improvement]] — after harness + evaluation make sense
20. [[self-improvement-memory]]
