---
type: source
tags: [ai-agents, llm, security, evaluation]
sources: []
created: 2026-11-14
updated: 2026-11-14
---

# Automate your agent development lifecycle using any coding agent (Google Cloud, 2026)

- **Raw file:** `raw/articles/2026-11-14-automate-agent-lifecycle-gemini.md`
- **Author / origin:** Shubham Saboo and Lavi Nigam, Google Cloud Blog, 2026-07-29 — https://cloud.google.com/blog/topics/developers-practitioners/automate-agent-development-lifecycles-with-gemini-enterprise
- **Ingested:** 2026-11-14 (received via Telegram)

## Summary
A hands-on tutorial: build "Industry Watch", an agent that compares what semiconductor companies
(NVDA, AMD, INTC, MU, AVGO) say in the news with what they file with the SEC — the *gap* is the
signal. The whole lifecycle is driven from a coding agent using Google's "Agents CLI" skills, in
six stages: **Setup, Build, Deploy, Govern, Evaluate, Publish**. The key design idea: two tools
fetch live data, a third tool joins them with plain code (no model inside), and the model only
*narrates* the result, so it cannot invent matches. Security comes from a per-agent identity with
least privilege, an outbound allow-list, and prompt-injection screening. It is a Google product
tutorial, so the tools named are Google's.

## Key takeaways
- **Grounding comes from architecture, not a bigger prompt:** deterministic tools do the fetching, joining and scoring; the model explains.
- **Untrusted text is an attack surface:** a press release could say "ignore prior instructions" — screen tool output, not just user input.
- **Least privilege for agents:** give each agent its own identity, minimal roles, and an egress allow-list of the hosts it may reach.
- **Make "don't hallucinate" a hard test:** every filing number the agent cites must appear word-for-word in tool output; run evals in CI.
- **Sessions vs memory:** sessions hold state within a conversation; a memory store carries preferences across conversations.
- **The coding agent as control plane:** skills + a docs MCP server let one assistant scaffold, deploy, secure, evaluate and publish.

## Concepts touched
[[grounding]], [[prompt-injection]], [[agent-development-lifecycle]], [[agent-runtime]],
[[agent-governance]], [[agent-evaluation]], [[agent-harness]]

## Open questions
- The tutorial puts Evaluate *after* Deploy and Govern, while LangChain stresses testing *before* production — the CI gate suggests evals still run before each release, but the article doesn't say so explicitly.
- No numbers on eval results, cost or latency.
