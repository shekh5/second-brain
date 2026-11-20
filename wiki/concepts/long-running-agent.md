---
type: concept
tags: [ai-agents, agent-runtime, durable-execution]
sources: [lovable-set-intelligence-free, cognition-40x-merged-prs]
created: 2026-11-20
updated: 2026-11-20
---

# Long-running agent

**In one line:** an AI agent that keeps working on one goal for hours or days — across crashes,
deploys and waiting time — instead of answering in a single short request.

## How it works
A short chat-style agent lives inside one request. A long-running agent outlives any single
process, so its state must live *outside* the worker that happens to be running it
(note: general knowledge, not from a source).

Lovable lists the pieces it needed to "remove the limits on agent runtime" (src: [[lovable-set-intelligence-free]]):

| Piece | What it does |
|---|---|
| **Durable runtime** | progress is saved, so the agent resumes after a failure |
| **Inbox** | a queue of messages to the agent (from users or other agents), so it can be talked to while it works |
| **Git-inspired history** | the agent's steps are stored like commits, so you can **fork** an agent from any point and try another path |
| **Prompts separate from task history** | the instructions can change without rewriting what already happened |
| **Stateless workers** | any worker can pick the agent up, so deploying new code doesn't kill running agents |
| **Checkpointed computers** | the agent's whole sandbox machine can be saved and resumed fast |
| **Forkable sandboxes** | a copy of the machine is made cheaply with [[copy-on-write]] memory |

```
   inbox ──► [ stateless worker ] ──► step ──► history (commit) ──► checkpoint
                   ▲                                │
                   └──── any worker resumes ◄───────┘      fork ──► new branch of work
```
(Diagram: Claude's sketch of the pieces above, not from the source.)

## Why it matters / when to use it
Lovable's first attempt was a sophisticated multi-agent framework, which nearly sank the
company; their later direction was to make the runtime for one agent durable and limitless
(src: [[lovable-set-intelligence-free]]). Use this design when tasks are too big for one request:
building whole apps, migrations, or ongoing maintenance (note: general knowledge, not from a source).

### Jobs, not tasks
Cognition argues for giving agents **jobs instead of tasks**: an ongoing responsibility with a
metric to optimise, rather than one ticket. Examples: tuning inference performance on new GPUs, and
an Android app maintained by Devin over 44 days (src: [[cognition-40x-merged-prs]]). A job is
only possible if the agent can run for a long time — which is what the pieces above provide
(note: Claude's link between the two sources, not stated in either).

## Trade-offs
| Pro | Con |
|---|---|
| Work survives crashes and deploys (src: [[lovable-set-intelligence-free]]) | Much more infrastructure: storage for histories, checkpoints and inboxes (note: general knowledge, not from a source) |
| Forking lets you explore alternatives from the same starting point (src: [[lovable-set-intelligence-free]]) | Many forks × whole machines = big memory and storage bills unless forks share data (note: general knowledge, not from a source) |
| Humans and other agents can message it mid-task (src: [[lovable-set-intelligence-free]]) | Longer runs make mistakes compound; needs verification loops along the way (note: general knowledge, not from a source) |

## Real-world examples
- **Lovable** — durable runtime, inboxes, Git-like histories, checkpointed and forkable sandboxes for its app-building agent (src: [[lovable-set-intelligence-free]]).
- **Cognition** — Devin kept an Android app going for 44 days as a "job" (src: [[cognition-40x-merged-prs]]).
- Durable-execution engines such as Temporal are used to build agent runtimes (src: [[langchain-agent-development-lifecycle]]).

## Related
[[agent-runtime]] — the general production home; this page is the "runs for a long time" case
[[copy-on-write]] — what makes forking a sandbox cheap
[[agent-evaluation]] — long runs need checks along the way

## Sources
- [[lovable-set-intelligence-free]]
- [[langchain-agent-development-lifecycle]]
- [[cognition-40x-merged-prs]]
