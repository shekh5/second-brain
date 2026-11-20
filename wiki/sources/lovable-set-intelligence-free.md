---
type: source
tags: [ai-agents, agent-runtime, sandboxes, software-engineering]
sources: [lovable-set-intelligence-free]
created: 2026-11-20
updated: 2026-11-20
---

# What it takes to set intelligence free — Fabian Hedin (Lovable)

- **Raw file:** `raw/articles/2026-11-20-lovable-set-intelligence-free.md`
- **Author / origin:** Fabian Hedin, CTO of Lovable (an AI app builder), talk at CODE Summit 2026 on the AI Engineer YouTube channel (~21 min). The YouTube transcript was blocked, so the raw file holds only the video description, the chapter list, and the README of Lovable's open-source `oj` build tool. Details below are therefore thin — treat them as an outline of the talk, not its full argument.
- **Ingested:** 2026-11-20

## Summary
Lovable says it nearly failed after building a sophisticated **multi-agent framework**. What
worked instead was infrastructure that lets a single coding agent run for a long time without
limits: a **durable agent runtime**, **inboxes** for messages to and from agents, **Git-inspired
histories** that let an agent's work be forked, prompts kept separate from task history,
**stateless workers** so deployments don't interrupt running agents, and **checkpointable,
forkable computers** (sandboxes) built on **copy-on-write** memory. They also rewrote their
frontend tooling (Vite) in Rust — the `oj` project — to cut memory and cold-start cost when
running many builds for agents. Finally, an inner verification loop and product/business
metrics close the loop between generated software and outcomes.

## Key takeaways
- A clever multi-agent framework was the wrong bet for Lovable; the gains came from runtime infrastructure (src: raw description).
- Long-running coding agents need: durable execution, agent inboxes, forkable Git-like history, stateless workers, and checkpoint/resume of the whole machine.
- **Forking a sandbox** cheaply relies on **copy-on-write** memory: a fork shares the parent's pages until one side writes.
- When thousands of agent builds run at once, build-tool memory and cold start become a real cost: `oj` reports a 2.5x–6.6x smaller memory footprint than Vite's default dev server on 1k–10k-module apps, and 1.4x–1.9x faster cold start (vendor's own benchmark).
- Verification and feedback loops should connect to product and business metrics, not stop at "the code compiles".

## Concepts touched
[[agent-runtime]], [[long-running-agent]], [[copy-on-write]], [[software-factory]], [[agent-evaluation]]

## Open questions
- What exactly made the first multi-agent framework fail (coordination cost? context loss?) — needs the transcript.
- How are "inboxes" and "Git-inspired histories" implemented? Is history forked at the message level or the filesystem level?
- `oj` benchmarks are self-reported on one machine (Apple M5 Max); Vite's experimental bundled dev mode still starts and reloads faster.
