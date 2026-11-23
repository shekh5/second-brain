---
type: concept
tags: [ai-agents, mcp, tools]
sources: [mcpcurl-readme, langchain-agent-development-lifecycle, google-automate-agent-lifecycle, atlan-adlc-vs-sdlc]
created: 2026-11-23
updated: 2026-11-23
---

# Model Context Protocol (MCP)

**In one line:** an open standard "plug" that lets any AI agent discover and call tools offered by
a separate program (an *MCP server*), without custom glue code for each tool.

## How it works
An *MCP server* is a program that wraps some system (GitHub, a database, docs) and offers *tools*.
An *MCP client* (an agent harness, or a CLI like mcpcurl) connects to it and talks
*JSON-RPC* — a simple format of JSON request/response messages naming a method and its parameters
(src: [[mcpcurl-readme]]).

```
client                         MCP server (e.g. GitHub)
  │ ── tools/list ───────────────▶ │
  │ ◀── schema: every tool,  ───── │   name, description,
  │     its params + types         │   input parameters
  │ ── call get_issue(owner,…) ──▶ │
  │ ◀── JSON result ────────────── │
```

1. The client asks `tools/list`; the server replies with a schema describing every tool (src: [[mcpcurl-readme]]).
2. The client builds its interface from that schema — an agent shows the tools to the model; mcpcurl turns each into a CLI subcommand with flags and validation (src: [[mcpcurl-readme]]).
3. A tool call is sent as a JSON-RPC request; the reply is returned to the caller (src: [[mcpcurl-readme]]).

**Transport:** with *stdio*, the client launches the server as a child process and exchanges
messages over its standard input/output (src: [[mcpcurl-readme]]). Remote servers over HTTP also
exist (note: general knowledge, not from a source).

## Why it matters / when to use it
- **Write a tool once, use it in every agent.** Because tools describe themselves, any MCP-aware harness can use a server without bespoke integration code (note: general knowledge, not from a source).
- It is one of the standard parts of an [[agent-harness]], next to prompts, skills and hooks (src: [[langchain-agent-development-lifecycle]]).
- Use it to give agents fresh information instead of stale training data — e.g. a docs MCP server (src: [[google-automate-agent-lifecycle]]).
- **Debug it without a model:** tools like mcpcurl let you list and call a server's tools from the shell, so you can check what an agent will actually see (src: [[mcpcurl-readme]]).

## Trade-offs
| Pro | Con |
|---|---|
| One standard interface; tools are discoverable from their schema (src: [[mcpcurl-readme]]) | Every tool's description lands in the model's context, costing tokens (note: general knowledge, not from a source) |
| Built-in validation of required params, types and enums (src: [[mcpcurl-readme]]) | Tool results are untrusted text — a route for [[prompt-injection]] (note: general knowledge, not from a source) |
| Same server serves many agents and plain CLIs | Servers often need powerful credentials (e.g. a GitHub token), so access must be governed — see [[agent-governance]] (note: general knowledge, not from a source) |

## Real-world examples
- **GitHub MCP Server** — repo, issue, PR and search tools (`get_issue`, `create_pull_request`, `search_code`…), run via Docker with a personal access token (src: [[mcpcurl-readme]]).
- **mcpcurl** — a curl-like CLI client generated on the fly from a server's tool schema (src: [[mcpcurl-readme]]).
- **Google's docs MCP server** given to a coding agent to build other agents (src: [[google-automate-agent-lifecycle]]).
- **Atlan** exposes a company "context layer" to AI tools through an MCP server (src: [[atlan-adlc-vs-sdlc]]).

## Related
[[agent-harness]] — MCP servers are one of the harness's parts
[[agent-skill]] — skills are instructions; MCP tools are actions; often used together
[[context-engineering]] — MCP is a common way to serve governed context to agents
[[prompt-injection]] — tool output is a main injection path

## Sources
- [[mcpcurl-readme]]
- [[langchain-agent-development-lifecycle]]
- [[google-automate-agent-lifecycle]]
- [[atlan-adlc-vs-sdlc]]
