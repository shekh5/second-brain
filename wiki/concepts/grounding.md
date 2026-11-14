---
type: concept
tags: [ai-agents, llm, reliability]
sources: [google-automate-agent-lifecycle]
created: 2026-11-14
updated: 2026-11-14
---

# Grounding

**In one line:** making sure every fact an agent states comes from real, fetched data (a tool
result or document) rather than from the model's memory or imagination.

## How it works
A *hallucination* is when a model states something false with confidence (note: general knowledge,
not from a source). Grounding fights this. The strongest form is **architectural**: split the work
so code does the facts and the model does the words (src: [[google-automate-agent-lifecycle]]).

```
  fetch_disclosures (SEC filings) ─┐
                                   ├─► reconcile (plain code, no model) ─► model narrates ─► answer
  fetch_claims (news, IR feeds) ───┘    matched / filing-only / claim-only      with citations
```

- **Deterministic tools:** fetching, joining and scoring are normal functions; "the join is the product" — the model never decides which press release matches which filing (src: [[google-automate-agent-lifecycle]]).
- **Model only narrates:** it explains the tool output, so it can't report a match the data doesn't support (src: [[google-automate-agent-lifecycle]]).
- **Grounding check as a test:** every ID the agent cites (SEC accession number, 8-K item code) must appear verbatim in tool output — a pass/fail gate, not a hope (src: [[google-automate-agent-lifecycle]]).

## Why it matters / when to use it
A plain chatbot can't answer "what changed last week?": that is past its training cutoff, so it
invents dates and filing numbers (src: [[google-automate-agent-lifecycle]]). Use grounding whenever answers must be auditable and depend
on live data. "The fix is an architecture, not a bigger prompt" (src: [[google-automate-agent-lifecycle]]).

## Trade-offs
| Pro | Con |
|---|---|
| Answers are traceable to real sources (src: [[google-automate-agent-lifecycle]]) | More engineering: you write and maintain the tools (src: [[google-automate-agent-lifecycle]]) |
| Hallucinated facts become testable failures (src: [[google-automate-agent-lifecycle]]) | Only covers what the tools fetch; gaps stay gaps (note: general knowledge, not from a source) |
| Logic in code is deterministic and testable the SDLC way (see [[adlc-vs-sdlc]]) | Less flexible than letting the model reason freely (note: general knowledge, not from a source) |

## Real-world examples
- Google's "Industry Watch" agent: SEC EDGAR 8-K filings vs GDELT news, joined by ticker and date, scored by 8-K item importance (Items 4.02 and 5.02 outrank 7.01) (src: [[google-automate-agent-lifecycle]]).

## Related
[[context-engineering]] — grounding in governed business context rather than raw data
[[agent-evaluation]] — grounding checks are a key eval metric
[[prompt-injection]] — fetched text can be trusted for facts but not as instructions

## Sources
- [[google-automate-agent-lifecycle]]
