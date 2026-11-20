---
type: concept
tags: [devops, software-engineering, ai-agents, security]
sources: [cognition-40x-merged-prs]
created: 2026-11-20
updated: 2026-11-20
---

# Ephemeral environment

**In one line:** a short-lived, throw-away copy of the whole system (machine + services) that is
built from scratch, used for a while, and then destroyed — instead of a long-lived shared dev or
test server.

## How it works
(note: general knowledge, not from a source, unless cited)

1. A script or image describes everything needed: OS, tools, databases, and every service.
2. A fresh VM or container is created from that description for each developer, agent or PR.
3. Work happens there; when it's done (or after a fixed time) it is deleted and rebuilt clean.

```
 image / script ──build──► [ VM: app + db + all services ] ──use──► destroy
        ▲                                                             │
        └─────────────────── rebuild (e.g. every hour) ◄──────────────┘
```

At Cognition, every service runs locally inside the agent's environment so agents can test their
own changes end to end, and the VMs are rebuilt every hour (src: [[cognition-40x-merged-prs]]).

## Why it matters / when to use it
- **Coding agents need to test their work.** If the whole system runs inside the agent's machine, the agent can run it, see failures and fix them before asking a human (src: [[cognition-40x-merged-prs]]).
- **No drift:** a frequent rebuild stops "works on my machine" problems and leftover junk from earlier runs (note: general knowledge, not from a source).
- **Security:** Cognition pairs this with cloud-only work — engineers use iPads, so code doesn't live on laptops (src: [[cognition-40x-merged-prs]]).

## Trade-offs
| Pro | Con |
|---|---|
| Clean, reproducible environment every time (note: general knowledge, not from a source) | Build time: a rebuild that is slow wastes agent and human time (note: general knowledge, not from a source) |
| Agents can test against the real services (src: [[cognition-40x-merged-prs]]) | Running every service per environment costs compute; big systems may not fit on one VM (note: general knowledge, not from a source) |
| Less data left on devices → smaller security risk (src: [[cognition-40x-merged-prs]]) | Anything not saved outside the VM is lost at rebuild; long tasks need checkpoints (note: general knowledge, not from a source) |

## Real-world examples
- **Cognition** — every service runs locally for agents; VMs rebuilt hourly; cloud-only access from iPads (src: [[cognition-40x-merged-prs]]).
- Per-pull-request "preview environments" on platforms like Vercel or Heroku Review Apps (note: general knowledge, not from a source).

## Related
[[software-factory]] — ephemeral environments are part of the factory floor for agents
[[agent-runtime]] — sandboxes are the agent-side version of the same idea
[[long-running-agent]] — needs [[copy-on-write]] checkpoints to survive a rebuild

## Sources
- [[cognition-40x-merged-prs]]
