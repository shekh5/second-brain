---
type: concept
tags: [ai-agents, llm, context]
sources: [anatomy-of-effective-commerce-agents, ai-native-sdlc-playbook]
created: 2026-11-21
updated: 2026-11-21
---

# Agent skill

**In one line:** a packaged set of instructions (and sometimes scripts) that an agent loads only
when a task needs it, instead of keeping everything in its always-on system prompt.

## How it works
The **system prompt** is the text an agent always sees. Putting every rule there makes it long,
slow and expensive (note: general knowledge, not from a source). A skill keeps rarely-needed know-how
outside it, and the agent pulls the skill in when relevant (src: [[anatomy-of-effective-commerce-agents]]).

```
 system prompt (always)          skills (loaded on demand)
 ┌──────────────────────┐        ┌──────────┐ ┌──────────┐ ┌──────────┐
 │ core rules, used on  │  ───►  │ returns  │ │ gift     │ │ bulk     │
 │ ≥ ~1/3 of requests   │        │ policy   │ │ wrapping │ │ orders   │
 └──────────────────────┘        └──────────┘ └──────────┘ └──────────┘
             one model, one agent loop, tools to business systems
```

**Rule of thumb:** if an instruction is needed on about a third or more of traffic, it belongs in
the system prompt; otherwise make it a skill (src: [[anatomy-of-effective-commerce-agents]]).

### Skills vs subagents
A **subagent** is a separate agent the main agent hands work to. For commerce agents the authors
prefer skills, because handoffs between agents lose state, cost more tokens and add latency.
Subagents still fit narrow jobs such as deep research, or a domain that already has its own
dedicated agent (src: [[anatomy-of-effective-commerce-agents]]).

### Skills advise, hooks enforce
Skills are *advisory*: the model is guided but not forced. For rules that must always hold, the
AI-native SDLC playbook uses deterministic hooks and managed settings instead (src: [[ai-native-sdlc-playbook]]).
Organisation-wide skills (brand, security, compliance, UX) are applied while specs are written (src: [[ai-native-sdlc-playbook]]).

## Why it matters / when to use it
- Keeps the base prompt short and stable — which also helps [[prompt-caching]] (note: general knowledge, not from a source).
- Lets different teams own different capabilities: give each skill and tool a **single owner team** (src: [[anatomy-of-effective-commerce-agents]]).
- Skills built by one team should be discoverable by others (see [[agent-governance]]).

## Trade-offs
| Pro | Con |
|---|---|
| One agent keeps full conversation state; no lossy handoffs (src: [[anatomy-of-effective-commerce-agents]]) | The model must recognise when to load a skill; a missed load means missing rules (note: general knowledge, not from a source) |
| Fewer tokens and less latency than subagents (src: [[anatomy-of-effective-commerce-agents]]) | Loading a skill mid-conversation adds tokens after the cached prefix (note: general knowledge, not from a source) |
| Clear ownership per skill (src: [[anatomy-of-effective-commerce-agents]]) | Many skills need a catalogue and curation (note: general knowledge, not from a source) |

## Real-world examples
- Anthropic's commerce-agent reference implementation (shopping and merchant agents) is built as one model + skills + tools (src: [[anatomy-of-effective-commerce-agents]]).
- This wiki itself runs on skills: `ingest`, `ask`, `lint`, `process-inbox` (note: general knowledge, not from a source).

## Related
[[agent-harness]] — skills are one of the pieces a harness provides
[[context-engineering]] — skills are a way to deliver the right context at the right time
[[agent-evaluation]] — every skill change should be checked against the eval suite

## Sources
- [[anatomy-of-effective-commerce-agents]]
- [[ai-native-sdlc-playbook]]
