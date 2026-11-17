---
type: concept
tags: [ai-agents, llm, self-improvement]
sources: [self-improvement-memory-crsi]
created: 2026-11-17
updated: 2026-11-17
---

# Recursive self-improvement (of agent harnesses)

**In one line:** an automatic loop where LLMs repeatedly propose, test and keep edits to an agent's
[[agent-harness]] code, so the agent gets better without changing the model's weights.

## How it works
The *policy model* (the LLM that actually solves tasks) stays frozen. What changes is the harness:
the code that decides its context, tools and execution flow (src: [[self-improvement-memory-crsi]]).

```
        ┌──────────── round t ────────────┐
tasks → │ Evaluator: run model in harness │ → scores, traces, errors
        │ Proposer (LLM): suggest k edits │
        │ Selector (LLM): screen, run,    │
        │   keep best (or keep old one)   │
        └──────────────┬──────────────────┘
                       ▼
               harness for round t+1
```
Only an "evolve" set of tasks feeds the loop; a separate held-out set measures the final result,
so the loop can't simply memorise the test (src: [[self-improvement-memory-crsi]]). The selector
weighs score, complexity, how task-specific an edit is, and the risk of regressions
(src: [[self-improvement-memory-crsi]]). In the paper's experiments each run is 10 rounds with 5
candidates per round (src: [[self-improvement-memory-crsi]]).

**Continual RSI (CRSI)** keeps optimising after something changes: a new benchmark with the same
model (*cross-dataset*), or a new model on the same benchmark (*cross-model*), as long as the harness
still runs on the new setting (src: [[self-improvement-memory-crsi]]).

## Why it matters / when to use it
Hand-tuning a harness takes repeated engineering and evaluation; RSI automates it
(src: [[self-improvement-memory-crsi]]). It is useful when models are swapped or upgraded often, or
when one harness must serve several models (src: [[self-improvement-memory-crsi]]). But gains don't
transfer automatically: a harness evolved with Claude Opus scored *below* the plain seed harness
when run with Gemini in every domain tested (src: [[self-improvement-memory-crsi]]). Keeping a
[[self-improvement-memory]] helps the optimizer decide what to keep or revise.

## Trade-offs
| Pro | Con |
|---|---|
| Improves the agent without retraining the model (src: [[self-improvement-memory-crsi]]) | Needs a good evaluator and lots of compute: many rollouts per round (src: [[self-improvement-memory-crsi]]) |
| Searches more edits than a human would try (note: general knowledge, not from a source) | Edits tuned to one model/benchmark can hurt on another (src: [[self-improvement-memory-crsi]]) |
| Held-out split guards against overfitting (src: [[self-improvement-memory-crsi]]) | A self-modifying harness may game the evaluator instead of solving the task (src: [[self-improvement-memory-crsi]]) |

## Real-world examples
- Meta-Harness and AHE search over harness code using execution traces and scores (src: [[self-improvement-memory-crsi]]).
- Google's CRSI experiments: coding (Terminal-Bench 2.1 → 4), text classification, workspace tasks (JobBench, GDPval, APEX-Agents) and engineering design (src: [[self-improvement-memory-crsi]]).
- Carrying harness + memory across Gemini generations beat fresh RSI on 2 of 3 later generations (src: [[self-improvement-memory-crsi]]).

## Related
[[agent-harness]] — the thing being improved
[[self-improvement-memory]] — the record that lets RSI continue across changes
[[agent-evaluation]] — RSI is an automated eval → change → re-eval loop

## Sources
- [[self-improvement-memory-crsi]]
