---
type: source
tags: [ai-agents, software-engineering, devops, coding-agents]
sources: [cognition-40x-merged-prs]
created: 2026-11-20
updated: 2026-11-20
---

# 40x More Merged PRs With 2.7x the Engineers — Walden Yan (Cognition)

- **Raw file:** `raw/articles/2026-11-20-cognition-40x-merged-prs.md`
- **Author / origin:** Walden Yan, CPO of Cognition (maker of the Devin coding agent), AI Engineer talk on YouTube (~14 min). The YouTube transcript was blocked, so the raw file holds only the video description and the chapter list — an outline, not the full talk.
- **Ingested:** 2026-11-20

## Summary
In one year Cognition's number of merged pull requests (PRs) grew 40x while its engineering team
grew only 2.7x. Yan credits a reorganised way of working built around coding agents: PRs are
"self-driving" (agent-made) by default; small **pods** own a feature end to end, from bug report to
QA; most work happens from Slack. To let agents test properly, **every service runs locally** in the
agent's environment, and the **VMs are rebuilt every hour**; engineers work from iPads with
cloud-only access for security. Agents also improve the "factory" itself. The next step is
giving agents **jobs, not tasks** — ongoing ownership measured by metrics, such as tuning
inference on new GPUs or maintaining an Android app over 44 days.

## Key takeaways
- Output per engineer can jump when agents write PRs by default: 40x PRs vs 2.7x people (company's own figure; merged PRs is not the same as value delivered).
- Organise humans into **small pods with vertical ownership** (bug report → fix → QA).
- Agents need a full, realistic test setup: **run every service locally**, in **short-lived VMs rebuilt hourly**.
- Security by keeping code in the cloud only (engineers on iPads).
- **Give agents jobs, not tasks:** a goal + a metric over time ("keep inference fast on new GPUs"), not a single ticket. **Measure everything** so agents can optimise.
- Use agents to improve the factory itself (its tooling and processes).

## Concepts touched
[[software-factory]], [[ephemeral-environment]], [[long-running-agent]], [[agent-evaluation]]

## Open questions
- "40x merged PRs" — how big were the PRs, and did defects or reverts grow too? Needs the transcript.
- How do pods review the volume of agent PRs? What does "self-driving by default" leave for humans?
- How does an hourly VM rebuild interact with long-running agents that need to persist state?
