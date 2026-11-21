---
type: source
tags: [ai-agents, llm, commerce, evaluation, caching]
sources: [anatomy-of-effective-commerce-agents]
created: 2026-11-21
updated: 2026-11-21
---

# The anatomy of effective commerce agents — Claude Platform

- **Raw file:** `raw/articles/2026-11-21-anatomy-of-effective-commerce-agents.md`
- **Author / origin:** Ali Shazal and Matthew Koen, Claude Platform (Anthropic), 2026-09-02 (~36 min read). A vendor's guide for building on its own model. The raw file is only a summary of the long article, so details are thin.
- **Ingested:** 2026-11-21

## Summary
A practical guide to building shopping/commerce agents. The recommended architecture is simple:
**one model in a normal agent loop**, given **skills** (instructions loaded only when needed),
tools that call the business's existing systems, and a strong eval suite — rather than many
per-domain subagents. Most of the guide is about running this well in production: cutting latency
(fewer model turns, parallel tool calls, streaming), cutting cost with **prompt caching** (target
90–99% hit rate), storing user **memory** as typed records the user can see and delete, and
enforcing safety **in code, not in the prompt**. Evals test snapshots of state and include messy,
negative and safety cases.

## Key takeaways
- **Skills over subagents:** handing work between subagents loses state, costs tokens and adds latency. Use subagents only for narrow jobs (e.g. deep research).
- **The one-third rule:** if an instruction is needed on ~⅓+ of traffic, put it in the system prompt; otherwise put it in a skill.
- **Tools do the heavy lifting:** return ranked, trimmed results; model UI widgets (product carousels) as typed tool calls.
- **Prompt caching is the main cost lever:** stable prompt first (byte-identical), session context next, volatile bits (timestamps) last. Measure **cost per completed task**, not per call.
- **Safety in code:** model proposes, human/policy engine approves; writes accept only server-issued IDs; caps on resulting state; third-party text sanitised and fenced.
- **Evals on state snapshots**, sourced from experts and real incidents; targeted CI per change, full suite nightly, canary rollout.

## Concepts touched
[[agent-skill]], [[prompt-caching]], [[agent-memory]], [[agent-evaluation]], [[prompt-injection]], [[agent-governance]]

## Open questions
- The raw capture is a summary — the article's concrete numbers (latency budgets, cache hit results) and code are missing. Worth saving the full text or the reference repo (github.com/anthropics/commerce-agents).
- "Skills over subagents" is a vendor recommendation for this domain; other sources (multi-agent frameworks) argue the opposite for some tasks.
