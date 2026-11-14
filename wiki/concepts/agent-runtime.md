---
type: concept
tags: [ai-agents, llm, deployment]
sources: [langchain-agent-development-lifecycle, google-automate-agent-lifecycle]
created: 2026-11-14
updated: 2026-11-14
---

# Agent runtime (deploying agents)

**In one line:** the production home for an agent — it keeps state, survives crashes, pauses for
humans, and gives the agent a safe place to run code and store files.

## How it works
Many agents run for a long time, call tools, wait for people, write files and must survive
interruptions — so a stateless web server is not enough (src: [[langchain-agent-development-lifecycle]]). A production runtime usually provides:

| Piece | What it means |
|---|---|
| **Durable execution** | the agent checkpoints its progress and resumes after a failure instead of losing work (src: [[langchain-agent-development-lifecycle]]) |
| **Human-in-the-loop (HITL)** | the agent pauses for approval, clarification or review, then continues (src: [[langchain-agent-development-lifecycle]]) |
| **Sandbox** | an isolated machine with a filesystem where the agent can run code; limits the "blast radius" of mistakes (src: [[langchain-agent-development-lifecycle]]) |
| **Virtual filesystem** | lighter option: files as working memory without running arbitrary code; can be backed by Postgres or S3 (src: [[langchain-agent-development-lifecycle]]) |
| **Context hub** | a place to store, version, review and update prompts, skills and instructions, so behaviour changes without a full redeploy and non-engineers can own them (src: [[langchain-agent-development-lifecycle]]) |

- **Sessions vs memory:** *sessions* hold state within one multi-turn conversation; a *memory bank* carries facts (watch-list, preferred format) across sessions (src: [[google-automate-agent-lifecycle]]).
- **Autoscaling / scale-to-zero:** a managed runtime can shut down between uses and start again on demand (src: [[google-automate-agent-lifecycle]]).
- **Deterministic code in the sandbox:** run joins and scoring in a code-execution sandbox, isolated from the model (src: [[google-automate-agent-lifecycle]]).

## Why it matters / when to use it
Deployment is not just "put it on a server": the agent needs a runtime, an execution environment
and context management to do real work (src: [[langchain-agent-development-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Durable execution means long tasks survive failures (src: [[langchain-agent-development-lifecycle]]) | More infrastructure than a stateless app (note: general knowledge, not from a source) |
| HITL keeps humans in control of risky steps (src: [[langchain-agent-development-lifecycle]]) | Every pause adds waiting time for a person (note: general knowledge, not from a source) |
| Sandboxes contain unsafe code (src: [[langchain-agent-development-lifecycle]]) | Not every agent needs one; a virtual filesystem may be enough (src: [[langchain-agent-development-lifecycle]]) |
| Context hub = fast prompt changes by domain experts (src: [[langchain-agent-development-lifecycle]]) | Prompt changes skip the code deploy pipeline, so they need their own review and versioning (src: [[langchain-agent-development-lifecycle]]) |

## Real-world examples
- Managed runtimes: LangSmith Deployment, AWS AgentCore; some teams build on Temporal (src: [[langchain-agent-development-lifecycle]]).
- Google Agent Runtime with Sessions and Memory Bank, plus a managed code-execution sandbox (src: [[google-automate-agent-lifecycle]]).
- Sandboxes: LangSmith Sandboxes, Daytona, E2B (src: [[langchain-agent-development-lifecycle]]).

## Related
[[agent-development-lifecycle]] — the Deploy stage
[[agent-harness]] — what you build before deploying it here
[[agent-governance]] — human approval is also a governance control

## Sources
- [[langchain-agent-development-lifecycle]]
- [[google-automate-agent-lifecycle]]
