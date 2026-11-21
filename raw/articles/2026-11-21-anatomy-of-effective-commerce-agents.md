# The anatomy of effective commerce agents — Claude Platform

> Origin: https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents
> Received via Telegram: 2026-11-21T18:20:33+00:00
> Author: Ali Shazal and Matthew Koen (Claude Platform, Anthropic), published 2026-09-02, ~36 min read
> Capture note: the fetch tool would only return a summary of this long article, not its full text. This file holds that summary.

## Architecture
- Commerce agents use one Claude model in a standard agent loop, equipped with skills, tools that call existing business systems, and a strong eval suite.
- The authors recommend skills over per-domain subagents. Subagent handoffs lose state, cost more tokens, and add latency. Subagents still make sense for narrow tasks like deep research, or when a domain has its own dedicated agent.
- Put instructions in the system prompt if they're needed on about a third or more of traffic. Otherwise, put them in skills.
- Tools should return already-ranked, trimmed results. UI components such as product carousels are best modeled as typed tool calls rather than custom markup parsed on the client.

## Latency and cost
- Task latency depends on the number of model turns, tool speed, and token speed. Reduce turns by preloading likely context and running independent tool calls in parallel.
- Dispatch tools eagerly as their arguments finish streaming, and stream UI components to cut perceived latency.
- Prompt caching is the main cost lever. The authors target 90–99% cache hit rates by keeping the global prompt byte-identical, placing session context next, and putting volatile values such as timestamps at the end.
- Choose models and effort levels by sweeping the eval suite, and measure cost per completed task rather than per call.

## Production
- **Memory:** Store facts as typed records in your own database. Extract memories asynchronously, key them per person, let users view and delete them, and set retention periods.
- **Safety:** Enforce rules in code rather than the prompt. Models propose changes, and humans or policy engines approve them. Writes accept only server-issued IDs, caps apply to the resulting state, and third-party content is sanitized and fenced.
- **Evals:** Test snapshots of state rather than full conversations. Include messy starting states, negative cases, safety cases, and cases that span multiple capabilities. Source cases from subject-matter experts and real incidents.
- **Organization:** Give each skill and tool a single owner team. Run targeted CI sets per change, the full suite nightly, and roll out changes to a canary cohort first.

## Looking ahead
The architecture should adopt better models through configuration changes plus an eval sweep. The authors also expect voice interfaces, proactive actions such as fare-drop alerts, and external agents shopping on users' behalf.

A reference implementation with shopping and merchant agents is available at github.com/anthropics/commerce-agents.
