---
type: source
tags: [ai-agents, software-engineering, devops, coding-agents, governance]
sources: [ai-native-sdlc-playbook]
created: 2026-11-21
updated: 2026-11-21
---

# The AI-native SDLC playbook — Claude

- **Raw file:** `raw/articles/2026-11-21-ai-native-sdlc-playbook.md`
- **Author / origin:** Louis Claxton (Anthropic), 2026-08-21, ~40 min read; covers Claude Enterprise, Claude Code and Claude Tag. A vendor playbook built around its own products. The raw file is only a summary of the long article.
- **Ingested:** 2026-11-21

## Summary
The playbook argues that **"code is no longer the bottleneck"**: coding agents write code faster
than human-speed approvals, reviews and handoffs can absorb it, so the bottleneck has moved to
planning, review/testing and deployment. It rebuilds the software development lifecycle (SDLC) as
six stages — Plan, Design, Build, Test, Deploy, Maintain — where **each stage commits a file**
(`intent.md` → `spec.md` → `plan.md` → code + tests → reviewed PR) that the next stage reads.
Those files form the audit trail. Agents do the work up to the **production gate**, which only a
human can pass; rules are enforced by **deterministic hooks and managed settings**, not just
advisory instructions. Monitoring and scans can restart the loop on their own.

## Key takeaways
- The bottleneck moved from writing code to **deciding, reviewing and shipping** it.
- **Artifact per stage, committed to git:** intent → spec → plan → code → review. The chain is the audit trail.
- **Agents verify their own work** (tests, builds, screenshots); evals run continuously in CI; config changes are treated as code.
- **AI first-pass PR review** guided by a `REVIEW.md`, humans still approve; CI runs with sandboxed credentials.
- **Hooks enforce, skills advise:** must-follow policy goes into deterministic hooks and admin-managed settings.
- **Self-starting loop:** alerts, scheduled security scans and incident channels create new `intent.md` files.
- "The loop keeps running. Human judgement stays above it."

## Concepts touched
[[ai-native-sdlc]], [[software-factory]], [[agent-skill]], [[agent-governance]], [[agent-evaluation]], [[ephemeral-environment]]

## Open questions
- The raw capture is a summary — the per-stage metrics and the example managed-settings file are missing.
- How does review keep up if PR volume grows 10–40x? (Same question as [[cognition-40x-merged-prs]].) AI review helps, but humans still approve every PR.
- Running the loop "without a person initiating it" raises cost and noise questions the summary doesn't cover.
