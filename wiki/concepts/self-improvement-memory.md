---
type: concept
tags: [ai-agents, llm, self-improvement, memory]
sources: [self-improvement-memory-crsi]
created: 2026-11-17
updated: 2026-11-17
---

# Self-improvement memory (SIM)

**In one line:** a structured diary for the harness *optimizer* — which problems it found, what edits
it tried, why, what it expected and what actually happened — so improvement can continue after the
model or benchmark changes.

## How it works
It is memory for the optimizer, not for the task-solving agent (src: [[self-improvement-memory-crsi]]).
Entries are grouped by a recurring harness problem, i.e. a root-cause hypothesis such as
"premature completion" (src: [[self-improvement-memory-crsi]]):

```
Problem: premature completion
 ├─ attempt 1: add completion gate   | why: … | predicted fixes: tasks A,B | observed: A fixed, B not | Opus, TB2.1, round 3
 ├─ attempt 2: gate checks optimality | why: … | predicted: C          | observed: C fixed    | Gemini, TB4, round 5
 └─ …
```
- Predictions are written *before* evaluation and checked afterwards (src: [[self-improvement-memory-crsi]]).
- Only the selected edit each round is recorded — including when it regresses or misses its prediction (src: [[self-improvement-memory-crsi]]).
- Each new proposal cites an existing problem or names a new one; entries are appended, never dropped (src: [[self-improvement-memory-crsi]]).
- The proposer gets the whole memory in its system prompt and the selector reads the same record — no retrieval or truncation (src: [[self-improvement-memory-crsi]]).

## Why it matters / when to use it
An evolved harness is just code; it doesn't explain why an edit exists, so a new optimizer may
repeat old attempts or change parts without knowing their purpose (src: [[self-improvement-memory-crsi]]).
Example: with SIM the optimizer kept an inherited completion check and added new target checks; without SIM it
tightened the check, twice had to repair deadlocks it caused, and wrongly thought it had added the
check itself (src: [[self-improvement-memory-crsi]]).

## Trade-offs
| Pro | Con |
|---|---|
| Beat harness-only continuation in all 10 tested settings; +2.36 points on average in a 10-run coding study (src: [[self-improvement-memory-crsi]]) | Whole record goes in the prompt; may grow too large over long chains (note: general knowledge, not from a source) |
| Also helped keep source-task skills (fewer lost successes) (src: [[self-improvement-memory-crsi]]) | Diagnoses alone ("problem-only memory") gave mixed results — you need the full evidence (src: [[self-improvement-memory-crsi]]) |
| Keeps failures, so dead ends aren't retried (src: [[self-improvement-memory-crsi]]) | Tested mostly with single runs outside coding (src: [[self-improvement-memory-crsi]]) |

## Real-world examples
- Workspace tasks, Opus → Gemini: both started at 68.41; with SIM 84.75, harness-only 73.42 (src: [[self-improvement-memory-crsi]]).
- Similar ideas: edit histories, improvement graphs, playbooks, HarnessBank (groups harnesses by the problem they address) (src: [[self-improvement-memory-crsi]]).
- Same spirit as an engineering decision log / ADR — record *why*, not just *what* (note: general knowledge, not from a source).

## Related
[[recursive-self-improvement]] — the optimization loop SIM feeds
[[agent-harness]] — what the recorded edits change
[[context-engineering]] — SIM is context given to the optimizer agent

## Sources
- [[self-improvement-memory-crsi]]
