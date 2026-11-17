---
type: source
tags: [ai-agents, llm, self-improvement, research-paper]
sources: [self-improvement-memory-crsi]
created: 2026-11-17
updated: 2026-11-17
---

# Self-Improvement Memory Enables Continual Recursive Self-Improvement

- **Raw file:** `raw/articles/2026-11-17-self-improvement-memory-crsi.md`
- **Author / origin:** Xin Yu, Fei Xia, Ting Yu and others (Google Cloud AI, Google DeepMind, Penn State). arXiv:2611.18856, 13 Nov 2026. Sent via Telegram.
- **Ingested:** 2026-11-17

## Summary
An LLM agent's performance depends on the model *and* on its [[agent-harness]] — the code that manages
context, tools and execution. **Recursive self-improvement (RSI)** automates harness tuning: an
LLM "proposer" suggests code edits to the harness, they are run on tasks, and an LLM "selector"
keeps the best one, round after round. Usually this is done for one fixed model and benchmark.
The paper asks what happens when the model or benchmark *changes* — they call continuing the
optimization **Continual RSI (CRSI)**. Their answer is **Self-Improvement Memory (SIM)**: a log,
grouped by recurring problem, of every accepted edit with its rationale, predicted vs. observed
outcome, and the context it was tested in. Carrying SIM along with the harness beats carrying the
harness alone in all ten settings they test.

## Key takeaways
- A harness tuned for one model can be **worse than the plain starting harness** on another model: an Opus-evolved harness scored 68.41 on Gemini vs. 73.89 for the seed harness.
- The evolved code alone doesn't say *why* each edit was made or how it performed, so a new optimizer may undo good fixes or repeat failed ones.
- SIM keeps, per root cause (e.g. "premature completion"): each attempt's change + rationale, predicted and actual results, and provenance (model, benchmark, round). Failures and regressions are recorded too. The whole memory goes into the proposer's prompt — no retrieval.
- Keeping only the diagnoses ("problem-only memory") gives mixed results; the full record of edits and evidence is what helps.
- Results: full SIM finished highest in 6/6 cross-dataset and 4/4 cross-model settings; in a 10-run coding study it beat harness-only continuation in 9/10 runs, by +2.36 points on average (p = 0.003). Largest gap: workspace tasks, 84.75 vs 73.42.
- Limits: only one run per condition outside coding; requires the harness interface to stay compatible.

## Concepts touched
[[recursive-self-improvement]], [[self-improvement-memory]], [[agent-harness]], [[agent-evaluation]]

## Open questions
- How big does SIM get over many transitions? It is put in the prompt in full, without truncation — this may not scale.
- The ethics section warns a self-modifying harness could satisfy the evaluator without solving the real task (reward hacking); how is that detected in practice?
- Results outside coding are single runs, so the size of the gains there is uncertain.
