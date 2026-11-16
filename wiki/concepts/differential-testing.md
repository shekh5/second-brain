---
type: concept
tags: [testing, formal-verification, software-engineering]
sources: [lean4-formal-verification-for-engineers]
created: 2026-11-16
updated: 2026-11-16
---

# Differential testing

**In one line:** run the same random inputs through two implementations that should agree (e.g.
fast production code and a simple reference model) and flag any input where their outputs differ.

## How it works
```
              ┌─► production code (Rust) ─┐
 random input ┤                           ├─► compare ─► same? ok : bug to fix before release
              └─► reference model (Lean) ─┘
```
The reference model gives every test a precise expected answer, so test authors don't have to invent
one for each case (src: [[lean4-formal-verification-for-engineers]]).

## Why it matters / when to use it
Use it when you want production code in a fast, practical language but have a trusted spec/model
elsewhere, e.g. in a [[formal-verification]] tool (src: [[lean4-formal-verification-for-engineers]]).
It also catches bugs when rewriting or optimising code, by comparing old and new versions
(note: general knowledge, not from a source).

## Trade-offs
| Pro | Con |
|---|---|
| Keeps production code in its normal language (src: [[lean4-formal-verification-for-engineers]]) | Only checks sampled inputs; not a proof for every input (src: [[lean4-formal-verification-for-engineers]]) |
| Expected answers come for free from the model (src: [[lean4-formal-verification-for-engineers]]) | You must maintain two implementations (note: general knowledge, not from a source) |
| Easy to run at huge volume automatically (src: [[lean4-formal-verification-for-engineers]]) | If both share the same misunderstanding, the bug is missed (note: general knowledge, not from a source) |

## Real-world examples
- **AWS Cedar:** about 100 million differential random tests every night between the Rust implementation and the Lean model; no version ships until they agree (src: [[lean4-formal-verification-for-engineers]]).

## Related
[[formal-verification]] — provides the trusted model; proof is the stronger guarantee
[[agent-evaluation]] — another way of checking behaviour against expected results

## Sources
- [[lean4-formal-verification-for-engineers]]
