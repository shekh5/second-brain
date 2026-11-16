---
type: source
tags: [ai-agents, formal-verification, testing, software-engineering]
sources: [lean4-formal-verification-for-engineers]
created: 2026-11-16
updated: 2026-11-16
---

# Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers

- **Raw file:** `raw/articles/2026-11-16-lean4-formal-verification.md`
- **Author / origin:** Varun Pant (AWS, leads formal-verification teams), AI Engineer conference talk on YouTube. The YouTube transcript was blocked, so the raw file holds the video description plus the official ai.engineer write-up of the talk.
- **Ingested:** 2026-11-16

## Summary
Coding agents now produce hundreds or thousands of pull requests a week, and the usual checks can't
keep up: an LLM judge is probabilistic, tests only cover inputs someone thought of, and human review
doesn't scale. Pant proposes **formal verification**: mathematically *proving* code meets a
specification for every input. The split is "humans own the specification, machines own the code
and proof", so the most important step is checking the spec is right. Lean is both a programming
language and a proof assistant; tactics search for a proof like moves in chess, and a small
independent kernel checks it. Examples: an AI rewrote zlib in Lean with 32,000 lines of proof, and
AWS's Cedar keeps its rules in Lean but ships Rust, compared by ~100 million random tests a night.

## Key takeaways
- A proof only says code matches its spec. A wrong spec gives a proved implementation of the wrong thing, so **validate the spec first** (review it, or test it on concrete inputs).
- **Humans own the spec; machines own the code and the proof.**
- Proof search (tactics) can be large and messy; trust comes from the **small kernel** that checks the finished proof, which you can rebuild yourself.
- Production code can stay in Rust: Cedar uses a Lean model as the reference and **differential random testing** (~100M tests nightly) before shipping. That is testing, not proof.
- Rust can also be verified deductively: **Verus** (pre/postconditions checked by the Z3 solver) or **Aeneas** (translate Rust into Lean and prove there).
- Getting started: pick your most critical code, write a concrete property you understand (a round trip, a "deny" rule), let an agent implement it and a tool prove it.

## Concepts touched
[[formal-verification]], [[differential-testing]], [[agent-evaluation]], [[software-factory]]

## Open questions
- The zlib proof (per Leo de Moura's separate NFM 2026 talk) only covers inputs under 1 GiB, a precondition the plain-English requirement doesn't mention. How often do proved theorems quietly carry such limits?
- How much engineer effort does validating a spec take compared with reviewing the code directly?
- Strata (AWS's shared verification core for many languages) is work in progress; only the SMT route is implemented today.
