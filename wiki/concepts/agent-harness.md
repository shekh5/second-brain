---
type: concept
tags: [ai-agents, llm]
sources: [langchain-agent-development-lifecycle, google-automate-agent-lifecycle]
created: 2026-11-14
updated: 2026-11-14
---

# Agent harness (and frameworks vs runtimes)

**In one line:** the working environment wrapped around a model — prompts, skills, tools, hooks and
files — that lets an agent do long tasks; one of three layers of agent-building tools.

## How it works
LangChain splits code-first agent tools into three layers (src: [[langchain-agent-development-lifecycle]]):

| Layer | Focus | What it gives you | Examples |
|---|---|---|---|
| **Framework** | abstractions | compose model calls, tools, prompts, retrieval, structured output, the agent loop | LangChain, CrewAI |
| **Runtime** | execution | state, control flow, durability, pause/resume, human intervention | LangGraph |
| **Harness** | doing | prompts, skills, MCP servers, hooks, middleware, sometimes a filesystem | Deep Agents, Claude Agent SDK |

A *skill* is a packaged set of instructions (a workflow, a writing style, how to use a tool) (src: [[langchain-agent-development-lifecycle]]).
*MCP* (Model Context Protocol) is an open standard for plugging tools and data sources into an
agent (note: general knowledge, not from a source). *Hooks* and *middleware* are places to run your
own code around tool calls, approvals, auth or business rules (src: [[langchain-agent-development-lifecycle]]).

**Coding agent as control plane:** Google gives a general coding agent platform *skills* (via its
Agents CLI) and a docs MCP server so it looks up current documentation instead of relying on stale
training data; the coding agent then scaffolds, deploys, secures, evaluates and publishes the new
agent (src: [[google-automate-agent-lifecycle]]).

## Why it matters / when to use it
"Building an agent" can mean very different things: a simple app may only need a tool-calling loop
(a framework), while a long-running agent needs prompts, skills, MCP servers, middleware and
retrievable context (a harness) (src: [[langchain-agent-development-lifecycle]]). No-code builders let domain experts take part, but teams still
need hooks and middleware to extend behaviour in code (src: [[langchain-agent-development-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Harnesses handle long, open-ended tasks out of the box (src: [[langchain-agent-development-lifecycle]]) | More moving parts to configure and govern (note: general knowledge, not from a source) |
| Frameworks are light and flexible for simple loops (src: [[langchain-agent-development-lifecycle]]) | You build durability, state and approvals yourself |
| No-code tools let non-engineers build (src: [[langchain-agent-development-lifecycle]]) | Complex systems still need code-level control via hooks/middleware (src: [[langchain-agent-development-lifecycle]]) |

## Real-world examples
- Claude Agent SDK and LangChain Deep Agents (harnesses); LangGraph (runtime); LangChain and CrewAI (frameworks) (src: [[langchain-agent-development-lifecycle]]).
- Google Agents CLI skills + ADK (Agent Development Kit, open source), driven from any coding agent (src: [[google-automate-agent-lifecycle]]).
- No-code: LangSmith Fleet, Claude Cowork, n8n (src: [[langchain-agent-development-lifecycle]]).

## Related
[[agent-development-lifecycle]] — choosing a layer is the Build stage
[[agent-runtime]] — where the built agent runs in production

## Sources
- [[langchain-agent-development-lifecycle]]
- [[google-automate-agent-lifecycle]]
