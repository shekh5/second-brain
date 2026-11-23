---
type: source
tags: [ai-agents, mcp, tools]
sources: [mcpcurl-readme]
created: 2026-11-23
updated: 2026-11-23
---

# mcpcurl — README (GitHub MCP Server repo)

- **Raw file:** `raw/articles/2026-11-23-mcpcurl.md`
- **Author / origin:** GitHub, `github/github-mcp-server` repository, `cmd/mcpcurl` folder README. Project documentation, not an independent review.
- **Ingested:** 2026-11-23

## Summary
`mcpcurl` is a small command-line tool, written in Go, for talking to an MCP server by hand — like
`curl` is for web servers. You give it the shell command that starts an MCP server; it starts that
server, asks it which tools it offers, and turns each tool into a CLI subcommand with matching
flags. Running a subcommand sends the call to the server and prints the JSON reply. The README
shows it against GitHub's own MCP server (tools like `get_issue`, `create_pull_request`,
`search_code`). It is a handy way to see what an MCP server really exposes and to test tools
without an AI model in the loop.

## Key takeaways
- **Self-describing tools:** an MCP server answers a `tools/list` request with a schema of every tool (name, description, input parameters); clients can build their interface from that alone.
- **Transport here is stdio:** mcpcurl launches the server as a child process and speaks JSON-RPC over its stdin/stdout (`--stdio-server-cmd`, required).
- **Schema → CLI:** each tool becomes `mcpcurl tools <name>`, with flags, required-parameter checks, type checks and enum checks generated from the schema; help text comes from the tool's description.
- **`schema` command** dumps the raw tool schema — useful for inspecting a server.
- **Example server:** GitHub's MCP server, run via Docker with a `GITHUB_PERSONAL_ACCESS_TOKEN`, exposes ~18 repo/issue/PR/search tools in the README's listing.

## Concepts touched
[[model-context-protocol]], [[agent-harness]]

## Open questions
- The README only covers the stdio transport; whether mcpcurl supports remote (HTTP) MCP servers isn't stated.
- The tool list shown is an example snapshot; the live GitHub MCP server's toolset is likely larger now.
- Numeric parameters show as `float` (e.g. `--issue_number float`) — a side effect of JSON Schema "number" types.
