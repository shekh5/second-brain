---
type: source
tags: [ai-agents, llm, evaluation, observability]
sources: []
created: 2026-11-14
updated: 2026-11-14
---

# The Agent Development Lifecycle (ADLC) (LangChain, 2026)

- **Raw file:** `raw/articles/2026-11-14-agent-development-lifecycle.md`
- **Author / origin:** Harrison Chase, LangChain blog, 2026-05-09 — https://www.langchain.com/blog/the-agent-development-lifecycle
- **Ingested:** 2026-11-14 (received via Telegram)

## Summary
Teams that ship agents well don't treat each agent as a one-off demo; they run a repeatable
**agent development lifecycle**: **Build → Test → Deploy → Monitor**, with production learnings
fed back into the next build. *Build* means choosing a level of abstraction (framework, runtime or
harness, or a no-code tool). *Test* means a small dataset of real tasks, metrics, experiments and
multi-turn simulations — before production. *Deploy* needs durable execution, human-in-the-loop
pauses, sandboxes and a "context hub" for prompts. *Monitor* needs full traces, not just latency
and uptime. Around it all sits **governance**: cost, tool access and discoverability. It is written
by LangChain, so its examples favour LangChain products.

## Key takeaways
- **Test before production, not after.** Start with a small, useful eval set and grow it from the hardest cases (dogfooding, then production traces).
- **Three layers of build tools:** *frameworks* (abstractions: compose model calls, tools, prompts), *runtimes* (execution: state, durability, pause/resume), *harnesses* (doing: prompts, skills, MCP servers, hooks, filesystem).
- **Agents need more than a stateless server:** checkpoint-and-resume, human approval pauses, isolated sandboxes for running code, and versioned prompts editable without a redeploy.
- **An agent can "succeed" technically and still fail the task.** Only a trace (inputs, model calls, tool calls, outputs) shows what it really did; attach feedback to traces.
- **Governance grows with the number of agents:** budgets, tool permissions + audit trails + human approval, and a catalogue so teams reuse skills instead of rebuilding them.

## Concepts touched
[[agent-development-lifecycle]], [[agent-harness]], [[agent-evaluation]], [[agent-runtime]],
[[agent-observability]], [[agent-governance]], [[software-factory]]

## Open questions
- "Harness" vs "framework" vs "runtime" are LangChain's own categories; other vendors draw the lines differently.
- No numbers are given on how big an eval set should be before a first deploy.
