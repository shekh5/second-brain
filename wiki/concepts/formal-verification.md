---
type: concept
tags: [ai-agents, formal-verification, testing, software-engineering]
sources: [lean4-formal-verification-for-engineers]
created: 2026-11-16
updated: 2026-11-16
---

# Formal verification

**In one line:** mathematically *proving* that code does what its specification says, for every
possible input, instead of checking a sample of inputs with tests.

## How it works
Three pieces (src: [[lean4-formal-verification-for-engineers]]):

- **Specification (spec):** a precise statement of what "correct" means, e.g. `decompress(compress(data)) = data`.
- **Implementation:** the code.
- **Proof:** an argument that the code satisfies the spec. A *theorem* is the claim; *lemmas* are smaller helper claims (sub-goals).

```
 requirement ─► formal spec ─► (validate spec!) ─► code ─► helper lemmas ─► theorem ─► kernel checks
   human          human or AI     human review/tests    AI      AI + tactics      AI       small, trusted
```

**Lean** is both a programming language and a *proof assistant* (a tool that helps build and check
proofs), so code and proof live in one language (src: [[lean4-formal-verification-for-engineers]]).
Proofs are built with **tactics**, like moves in chess: the theorem is checkmate, and when a branch
gets stuck the prover backtracks and tries another route. The finished proof must then pass a small
**kernel**, the only part you need to trust; kernels exist in C++, Rust and Lean and you can write
your own (src: [[lean4-formal-verification-for-engineers]]).

A second style uses a **solver** (e.g. Z3): like a powerful calculator, it takes a formula and says
whether its constraints can all hold. **Verus** checks Rust code annotated with *preconditions* (what
must be true before) and *postconditions* (what must be true after) this way; the annotations are
checked at build time and erased at runtime. **Aeneas** instead translates Rust into Lean so it can
be proved with tactics (src: [[lean4-formal-verification-for-engineers]]).

## Why it matters / when to use it
Coding agents create far more code than people can review. An LLM judge is probabilistic, tests
cover only the inputs someone thought of, and human review doesn't scale; none can say code is
correct for *every* input (src: [[lean4-formal-verification-for-engineers]]). Formal verification
splits the work: **humans own the spec, machines own the code and proof**
(src: [[lean4-formal-verification-for-engineers]]).

Start small: your most critical code, plus one property you understand and care about
(src: [[lean4-formal-verification-for-engineers]]).

## Trade-offs
| Pro | Con |
|---|---|
| Covers every input the spec covers, not a sample (src: [[lean4-formal-verification-for-engineers]]) | A wrong spec gives a "proved" wrong program; the spec must be validated by humans (src: [[lean4-formal-verification-for-engineers]]) |
| Untrusted AI can write the proof; only the small kernel needs trust (src: [[lean4-formal-verification-for-engineers]]) | Proofs are huge: 32,000 lines for zlib (src: [[lean4-formal-verification-for-engineers]]) |
| Scales review to agent-level output (src: [[lean4-formal-verification-for-engineers]]) | Proved claims may hide limits, e.g. zlib proof only for inputs < 1 GiB (src: [[lean4-formal-verification-for-engineers]]) |
| | Needs special languages/tools and skills; most teams don't have them yet (note: general knowledge, not from a source) |

## Real-world examples
- **zlib in Lean:** an AI converted the zlib compression library to Lean in about a week and proved the compress/decompress round trip, with 32,000 lines of proof (src: [[lean4-formal-verification-for-engineers]]).
- **AWS Cedar:** authorization policy language whose meaning is specified in Lean (e.g. "forbid beats permit") while production code is Rust, checked by [[differential-testing]] (src: [[lean4-formal-verification-for-engineers]]).
- **AWS Strata:** work-in-progress shared core in Lean that many languages can be lowered into, so one analysis serves all; today it generates verification conditions for SMT solvers (src: [[lean4-formal-verification-for-engineers]]).

## Related
[[differential-testing]] — cheaper cousin: compare code with a model on random inputs instead of proving
[[agent-evaluation]] — evals score agent behaviour probabilistically; proofs give certainty for code
[[software-factory]] — formal proofs could be a gate for agent-written patches
[[grounding]] — same idea of "trust the checker, not the model"

## Sources
- [[lean4-formal-verification-for-engineers]]
