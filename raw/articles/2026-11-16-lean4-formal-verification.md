# Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers

> Origin: https://www.youtube.com/watch?v=lRa9sPaMyy4
> Received via Telegram: 2026-11-15T15:27:01+00:00
> Author: Varun Pant (AWS), AI Engineer channel (YouTube talk, ~9.5 min)
> Transcript note: YouTube transcript was blocked (bot check). Saved instead: the video description (via r.jina.ai) and the official AI Engineer talk write-up, which is based on the corrected transcript: https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286

## Video description

An AI spent about a week rewriting zlib in Lean and emitted 32,000 lines of proof. Not tests, proof. It decomposed the job into lemmas, closed each one with tactics, assembled them into a single theorem, and a small independent kernel checked the result. Varun Pant opens on the gap that makes this worth caring about now. Coding agents are producing hundreds or thousands of pull requests a week, and none of the usual checks actually clear them. A model grading code is probabilistic, tests cover the inputs someone thought of, and human review does not scale to agent throughput. None of the three can say the code is correct for every input. His division of labor is the memorable part: humans own the specification, machines own the code and the proof. That puts all the weight on the spec being right, which is why he insists on validating it before anything downstream runs, whether a person reviews it or it gets tested against real inputs. The chess analogy carries the rest, with tactics as moves, a theorem as checkmate, and backtracking when a branch will not close. AWS runs this in production on Cedar, whose authorization semantics live in Lean while the shipping code is Rust, reconciled by roughly 100 million differential tests nightly. Nothing ships until they agree.

Timestamps: 0:00 Why none of the usual checks clear agent output · 1:06 Specifications humans own, proofs machines own · 2:00 Lean as one language for code and proof · 3:01 Tactics, theorems, and the chess analogy · 3:58 A small kernel you can independently rebuild · 4:52 Rewriting zlib into Lean, and 32,000 lines of proof · 6:44 Cedar: Lean semantics, Rust in production · 7:40 Solvers, preconditions, and code erased at runtime · 8:37 Bringing any language into the same core

## Official talk write-up (ai.engineer)


### Ideas worth remembering[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#essay-takeaways-heading)

*   A proof establishes that code satisfies its specification. Validate what the specification means before generating implementation and proof. 
*   Tactics construct proofs through search and backtracking; a small independent kernel checks the completed argument. 
*   Cedar compares production Rust with a Lean model using about 100 million differential random tests nightly. Verus and Aeneas provide different routes toward deductive verification of Rust. 
*   Start with critical code and a concrete property you can explain, then let the agent implement it and the verification tool prove it. 

### Define correctness before asking a machine to prove it[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#checks-and-specifications-heading)

Coding agents can produce hundreds or thousands of pull requests a week. Checking that output creates a different bottleneck: an LLM judge gives a probabilistic assessment, tests exercise selected inputs, and human review struggles to keep pace. Varun Pant, who builds AI products and leads formal-verification teams at AWS, introduces formal verification as a way to prove that an implementation satisfies a specified property across every input covered by that property. [0:12](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=12s)

The first engineering task is to write what “correct” means. In the spec-driven workflow Pant introduces with Kiro, a human can write a formal specification directly in **Lean** or write natural-language requirements that an AI formalizes. The specification then needs validation: someone reviews it, or tests whether it describes the expected behavior on concrete inputs. A proof establishes agreement with the specification; a mistaken specification can therefore produce a proved implementation of the wrong requirement.

That order matters because the specification sits upstream of both implementation and verification. It remains a “living, breathing artifact” that the builder works with as requirements develop. Once its meaning is settled, the coding agent implements it and the verification tool proves the implementation matches it. Pant’s division of labor is compact: “humans own the specification, and machines own the code and proof.”





### One language holds the function and its theorem[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#lean-list-reversal-heading)

Lean is both a programming language and a proof assistant. Definitions and proofs use the same language, so a Lean implementation does not need a separate translation into a proof language. Pant also emphasizes extensibility—Lean is implemented in Lean—and a small trusted kernel that checks proofs. Proofs can be exported for independent checking.

List reversal supplies the first concrete example. Reversing `[1, 2, 3]` produces `[3, 2, 1]`. The accompanying theorem describes how reversal interacts with concatenation: reversing `A` followed by `B` gives the reverse of `B` followed by the reverse of `A`. Here, the talk’s “plus” means joining lists, rather than adding their elements.

To see the change, split that same list into `A = [1, 2]` and `B = [3]`. Concatenation places the `A` block before the `B` block. Reversing the combined list moves the `B` block to the front and reverses the order inside `A`, yielding `[3, 2, 1]`. Reversing the blocks separately and joining them in the opposite order produces the same result: `[3] ++ [2, 1]`. This instance makes the property visible; the theorem expresses it for every pair of lists, rather than only these three elements.

Tactics construct the proof, and the kernel checks it. This separation provides a way to accept machine-generated proofs: the machine searches for an argument, while a much smaller component checks whether that argument establishes the theorem.





### Search like chess, then check the result independently[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#tactics-and-kernel-heading)

Pant’s analogy is chess. The theorem is the goal, like checkmate; tactics are the moves used to reach it. Proof construction is interactive and branches into a search tree. A tactic may advance the proof, but a branch can also leave a goal unresolved. The prover then backtracks and tries another route. A plausible sequence of moves alone does not finish the job: the resulting proof must pass the kernel.

The kernel rejects an incorrect proof in Pant’s example. Confidence in the generator therefore does not substitute for checking its output. Pant describes open-source kernel implementations in C++, Rust, and Lean, and the possibility of writing an independent checker yourself. The trusted component remains the checker, even when proof search becomes large or complicated. [4:03](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=243s)





### A compression round trip becomes 32,000 lines of proof[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#zlib-proof-heading)

The next example puts both specification and implementation in Lean. Pant describes an open-source project in which AI converted zlib, the C compression library, to Lean over about a week. Its natural-language requirement is easy to understand: decompressing compressed data should return the original data. Written as an intended property, the round trip is `decompress(compress(data)) = data`. The [Lean theorem in Leo de Moura’s separate May 6, 2026 NFM presentation](https://leodemoura.github.io/static/nfm2026/) proves that round trip across compression levels for inputs satisfying `data.size < 1024 * 1024 * 1024`: strictly below 1 GiB. The proved claim therefore includes an input-size precondition that the plain-language requirement leaves unstated. [4:41](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=281s)

The AI first turns that requirement into a formal specification. After the specification is checked, it writes the Lean code and breaks the proof into helper lemmas—smaller claims that serve as subgoals. Tactics prove those claims, the claims assemble into the final theorem, and the independent kernel checks the result. Pant reports 32,000 lines of proof for this example. That quantity describes the proof artifact, rather than a count of test cases.

How does one readable requirement lead to such a large proof? The flow below separates the initial decision about meaning from the generated implementation and proof. Specification validation comes first. The AI then expands the problem into code and lemmas, and the kernel checks the assembled argument. The checker’s position at the end explains why validating the requirement cannot be delegated to proof checking.

### From round-trip requirement to checked theorem[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#_R_18eajalm_)

**Round-trip requirement**Decompressing compressed data returns the original data.

**Formal specification**AI formalizes the requirement; a human reviews it or tests its meaning on inputs.

**Lean implementation**AI writes code after specification validation.

**Helper lemmas**AI decomposes the proof into subgoals and proves them with tactics.

**Final theorem**The proved lemmas assemble into the complete argument.

**Independent kernel**Checks the completed proof.

Validation precedes implementation. Helper lemmas divide the proof into manageable claims; the kernel checks their assembled result. The theorem in Leo de Moura’s separate NFM presentation, rather than one shown in Pant’s recording, covers inputs strictly below 1 GiB across compression levels.

Read the diagram as text
*   **Round-trip requirement.**Decompressing compressed data returns the original data.
*   **Formal specification.**AI formalizes the requirement; a human reviews it or tests its meaning on inputs.
*   **Lean implementation.**AI writes code after specification validation.
*   **Helper lemmas.**AI decomposes the proof into subgoals and proves them with tactics.
*   **Final theorem.**The proved lemmas assemble into the complete argument.
*   **Independent kernel.**Checks the completed proof.

*   Round-trip requirement → Formal specification: Formalize.
*   Formal specification → Lean implementation: Implement after validation.
*   Lean implementation → Helper lemmas: Generate proof subgoals.
*   Helper lemmas → Final theorem: Assemble.
*   Final theorem → Independent kernel: Check.





### Cedar connects Lean semantics to production Rust[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#cedar-rust-heading)

Production code can stay in Rust while Lean supplies its functional specification. Cedar, an open-source authorization policy language, illustrates this arrangement: its specification is written in Lean and its production implementation runs in Rust. The critical example is “forbid trumps permit.” Whenever a forbid policy is satisfied, the request must be denied, even when permission would otherwise be available. [5:58](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=358s)

The connection between the two implementations uses differential random testing. Each generated input goes to both the Rust production code and the Lean model, and their outputs are compared. Pant reports about 100 million such tests nightly and says no version ships until the agreement requirement is satisfied. This checks the Rust implementation against the formal model on sampled inputs; it does not establish a deductive proof that the Rust code agrees with the model for every input.

The practical choice is to keep a shipping implementation in Rust and use a Lean model as the reference for its behavior. For the forbid example, agreement means both paths return denial for the same request and policies. A difference exposes a disagreement that must be resolved before release. The model gives testing a precise expected result, rather than requiring each test author to invent one.





### Two routes from Rust to deductive verification[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#rust-deductive-verification-heading)

Deductive verification offers another way to work with Rust. Before introducing the tools, Pant distinguishes a solver from Lean’s interactive proof search. Lean resembles a chessboard on which tactics advance a goal. A solver resembles a powerful calculator: it receives a formula and answers whether that formula is satisfiable or unsatisfiable—whether its constraints can hold together. [6:59](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=419s)

*   **Verus: specifications alongside code.** Verus uses Z3 to verify Rust code with annotations expressing preconditions and postconditions. A precondition states what must hold before the operation; a postcondition states what must hold afterward. These specifications are checked statically by the verifier and erased at runtime, so they do not become runtime assertions.

*   **Aeneas: translate Rust into Lean.** Aeneas starts from Rust’s mid-level intermediate representation and translates it into a functional form in Lean. The translated program can then use the theorem-proving approach introduced earlier: goals, tactics, and checked proofs.

These paths place the specification in different working environments. Verus keeps it close to the Rust code and uses a solver; Aeneas brings a functional translation into Lean for theorem proving. Both differ from Cedar’s differential-testing arrangement, where the production program and model are run on matching inputs and their outputs compared.





### Lower different languages into a shared verification core[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#shared-core-and-starting-point-heading)

The final technical proposal extends the compiler idea beyond Rust. Pant describes [Strata](https://raw.githubusercontent.com/strata-org/Strata/main/README.md), an open-source AWS tool. A language-specific dialect represents a program at a high level, then lowers it into Strata Core, a common low-level representation written in Lean. The intended architecture lets that representation feed different verification engines: Lean proofs, SMT solvers, or model checkers. The [architecture documentation](https://raw.githubusercontent.com/strata-org/Strata/main/docs/Architecture.md) describes the implemented analysis as a verification-condition generator with an SMT interface; broader Lean reasoning and other engine integrations remain architectural goals. Support for arbitrary languages is likewise the intention of this work in progress, rather than a claim that every language is already supported. [8:26](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=506s)

What does a shared core buy? The diagram shows where language-specific work ends and analysis begins, distinguishing the implemented SMT route from proposed engine choices. Each language needs a dialect and lowering path, but the resulting program reaches the same core. That common representation allows an analysis to be reused across languages, with additional engines intended to extend the choice of verification method.

The closing recommendation starts smaller than that infrastructure: pick your most critical code and write what correct means. Pant points to using Lean in a browser, then having a coding agent implement the specification and a verification tool prove the result. A useful first target is a property whose meaning you can inspect and care about—a compression round trip or a denial rule—before asking a machine to expand it into a proof. That is the route toward the ending’s ambition of software that is “provably correct.” [9:17](https://www.youtube.com/watch?v=lRa9sPaMyy4&t=557s)

### A shared core supports reusable analysis[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#_R_18fqjalm_)

**Language-specific dialect**Represents a source program in a high-level intermediate form.

**Strata Core**Common low-level program representation written in Lean; implemented analysis generates verification conditions.

**Lean reasoning — goal**planned-engines — Broader theorem-proving support is a long-term architectural goal.

**SMT interface — implemented**implemented-engine — Verification conditions are encoded for SMT solvers.

**Model checkers — goal**planned-engines — An intended external-engine integration.

Language-specific translation precedes Strata Core. The documented implementation generates verification conditions and interfaces with SMT solvers; broader Lean reasoning and model-checker routes are architectural goals.

Read the diagram as text
*   **Language-specific dialect.**Represents a source program in a high-level intermediate form.
*   **Strata Core.**Common low-level program representation written in Lean; implemented analysis generates verification conditions.
*   **Lean reasoning — goal.**planned-engines — Broader theorem-proving support is a long-term architectural goal.
*   **SMT interface — implemented.**implemented-engine — Verification conditions are encoded for SMT solvers.
*   **Model checkers — goal.**planned-engines — An intended external-engine integration.

*   Language-specific dialect → Strata Core: Lower.
*   Strata Core → Lean reasoning — goal: Architectural goal.
*   Strata Core → SMT interface — implemented: Generate conditions and encode for SMT.
*   Strata Core → Model checkers — goal: Architectural goal.





### Resources[#](https://ai.engineer/talks/lRa9sPaMyy4-youtube-a4fdf8b98776965fc286#talk-resources-heading)

#### From the talk

*   The project README provides prerequisites, build commands, and an example verification invocation for experimenting with Strata. This is a practical next step for the shared-core proposal, separate from the talk’s invitation to try Lean in a browser.

*   Explains dialect definitions, composition, transformations, and Strata Core. It distinguishes the broader engine architecture from the implemented verification-condition generator and SMT interface.

*   [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro](https://ai.engineer/talks/HY_JyxAZsiE-spec-driven-development-agentic-coding-at-faang)
A companion on the specification-driven development workflow Pant introduces before adding formal proof.

*   [Fuzzing in the GenAI Era](https://ai.engineer/talks/OMGPvW8TBHc-fuzzing-in-genai-era)
A related testing topic to explore alongside Cedar’s randomized comparisons between implementation and model.
