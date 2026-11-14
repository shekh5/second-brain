---
type: concept
tags: [ai-agents, llm, security, governance]
sources: [langchain-agent-development-lifecycle, atlan-adlc-vs-sdlc, google-automate-agent-lifecycle]
created: 2026-11-14
updated: 2026-11-14
---

# Agent governance

**In one line:** the rules and controls around a fleet of agents — what they cost, what they are
allowed to do, and whether teams can find and reuse them.

## How it works
Governance sits around the whole [[agent-development-lifecycle]] (src: [[langchain-agent-development-lifecycle]]). Three main areas:

1. **Cost** — agents can be expensive (many model calls, long context, retries, long runs). Track spend with budgets, usage monitoring, alerts and a breakdown by agent, team, model and tool (src: [[langchain-agent-development-lifecycle]]).
2. **Tool access** — clear rules for which tools an agent may use, when, and on whose behalf. Keep **audit trails**: which agent called the tool, with what inputs and outputs, authorised by which user or policy. Use **human-in-the-loop** approval for actions touching customers, money, sensitive data or production systems — designed in from the start (src: [[langchain-agent-development-lifecycle]]).
3. **Discoverability and reuse** — prompts, skills, tools, retrieval sources, policies and whole agents should be findable so teams don't rebuild inconsistent copies (src: [[langchain-agent-development-lifecycle]]).

Google's tutorial shows concrete security controls (src: [[google-automate-agent-lifecycle]]):
- **Agent identity:** each agent gets its own principal with least-privilege roles (no write or admin), instead of borrowing broad permissions.
- **Egress allow-list:** route outbound traffic through a gateway that only allows named hosts (e.g. sec.gov, the news API).
- **Input/output screening** against [[prompt-injection]] and jailbreaks.

Atlan adds that agent governance covers more than code governance: context governance, drift
monitoring, token economics and agent accountability (src: [[atlan-adlc-vs-sdlc]]). "Agent sprawl" (many teams each with
their own ungoverned agents and context) is the organisational version of the problem (src: [[atlan-adlc-vs-sdlc]]).

## Why it matters / when to use it
One agent needs only light controls. Many agents without governance become hard to find, hard to
monitor, expensive and unclear in what they may do. Good governance is meant to make fast
iteration *possible*, not slow it down (src: [[langchain-agent-development-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Prevents runaway cost and unsafe actions (src: [[langchain-agent-development-lifecycle]]) | Approval steps slow down fully automated flows (src: [[langchain-agent-development-lifecycle]]) |
| Audit trails make tool calls reviewable (src: [[langchain-agent-development-lifecycle]]) | Needs central infrastructure and ownership (note: general knowledge, not from a source) |
| Reuse avoids inconsistent duplicate skills (src: [[langchain-agent-development-lifecycle]]) | A shared catalogue must be curated or it becomes clutter (note: general knowledge, not from a source) |

## Real-world examples
- Gartner (June 2025) predicts over 40% of agentic AI projects will be cancelled by end of 2027, mostly due to cost, unclear value and weak risk controls; and that by 2030 half of agent deployment failures will come from weak runtime governance (src: [[atlan-adlc-vs-sdlc]]).
- A skill encoding a domain procedure built by one team should be discoverable by another rather than rewritten (src: [[langchain-agent-development-lifecycle]]).

## Related
[[agent-observability]] — traces power the audit trail
[[agent-runtime]] — human-in-the-loop pauses happen in the runtime

## Sources
- [[langchain-agent-development-lifecycle]]
- [[atlan-adlc-vs-sdlc]]
- [[google-automate-agent-lifecycle]]
