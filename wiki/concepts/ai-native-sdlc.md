---
type: concept
tags: [ai-agents, software-engineering, devops, coding-agents, governance]
sources: [ai-native-sdlc-playbook]
created: 2026-11-21
updated: 2026-11-21
---

# AI-native SDLC

**In one line:** the software development lifecycle rebuilt for coding agents — every stage
produces a committed file the next stage reads, agents do the work, and humans own the gates.

## How it works
The **SDLC** (software development lifecycle) is the usual path from idea to running software.
Once agents write code faster than people can review it, the old gates become the bottleneck, so
the process is redesigned around agents (src: [[ai-native-sdlc-playbook]]).

```
  PLAN        DESIGN       BUILD          TEST            DEPLOY            MAINTAIN
 intent.md ─► spec.md ─► plan.md ─► code + tests ─► AI review + ─► [PROD GATE] ─► monitor, scans,
 (owner       (org        (plan mode,  (agent checks    human approval   human only     incidents
  reviews)     skills)     worktrees)   itself, evals)  (REVIEW.md)                        │
     ▲                                                                                    │
     └───────────────────────── new intent.md ◄───────────────────────────────────────────┘
```
(src: [[ai-native-sdlc-playbook]])

| Stage | Committed artifact | Key practice |
|---|---|---|
| Plan | `intent.md` | Drafted with the agent, reviewed by a product owner |
| Design | `spec.md` | Org [[agent-skill|skills]] (brand, security, compliance, UX) applied while writing |
| Build | `plan.md`, code | Plan before code; `CLAUDE.md`, skills and hooks as guardrails; parallel sessions in git worktrees |
| Test | tests, eval results | Agent verifies its own work (tests, builds, screenshots); continuous evals in CI; config treated as code |
| Deploy | reviewed PR | AI review per `REVIEW.md`, human approval; hooks as approval gates; CI with sandboxed credentials |
| Maintain | new `intent.md` | Alerts, recurring security scans, incident-channel bots restart the loop |
(src: [[ai-native-sdlc-playbook]])

**Hooks vs skills:** a *hook* is a script the tooling always runs at a fixed point (e.g. before a
command or commit) and that can block it — deterministic. A skill is guidance the model may or may
not follow — advisory (note: general knowledge, not from a source). The playbook puts must-follow
policy in hooks and admin-managed settings (src: [[ai-native-sdlc-playbook]]).

## Why it matters / when to use it
- "Code is no longer the bottleneck": planning, review and deployment are (src: [[ai-native-sdlc-playbook]]).
- The chain of committed files is the **audit trail** — you can see why every change was made (src: [[ai-native-sdlc-playbook]]).
- Human attention is concentrated at the gates instead of spread thin over every diff (src: [[ai-native-sdlc-playbook]]).

## Trade-offs
| Pro | Con |
|---|---|
| Built-in audit trail from intent to production (src: [[ai-native-sdlc-playbook]]) | More documents per change; overhead for tiny fixes (note: general knowledge, not from a source) |
| Agent can't pass the production gate — a hard safety line (src: [[ai-native-sdlc-playbook]]) | Human approval still caps throughput if agent output grows a lot (note: general knowledge, not from a source) |
| Hooks make policy deterministic, not "please follow" (src: [[ai-native-sdlc-playbook]]) | Hooks and managed settings must be built and maintained centrally (note: general knowledge, not from a source) |
| Self-starting loop catches issues early (src: [[ai-native-sdlc-playbook]]) | Automatic triggers can flood the queue with low-value work (note: general knowledge, not from a source) |

## Real-world examples
- Anthropic's playbook for Claude Code / Claude Enterprise, including an example enterprise managed-settings file (src: [[ai-native-sdlc-playbook]]).
- Cognition runs a similar agent-first process: self-driving PRs, pods, hourly-rebuilt VMs (src: [[cognition-40x-merged-prs]]) — see [[software-factory]].
- This wiki works the same way in miniature: `CLAUDE.md` rules, skills, scheduled runs, every change committed (note: general knowledge, not from a source).

## Related
[[software-factory]] — the same idea described as a repeatable, measured delivery loop
[[adlc-vs-sdlc]] — don't confuse: that's the lifecycle *for building agents*; this is the SDLC *run by agents*
[[agent-governance]] — hooks, managed settings and audit trails are governance tools
[[agent-evaluation]] — continuous evals in CI are the Test stage
[[ephemeral-environment]] — gives agents a full environment to verify their own work
[[formal-verification]] — another answer to "review can't keep up with agent code"

## Sources
- [[ai-native-sdlc-playbook]]
