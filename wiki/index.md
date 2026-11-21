# Index

Catalogue of every wiki page. Claude reads this first when answering questions.

## Topics
- [[ai-agents]] — map of AI agent concepts: building, testing, deploying, governing agents
- [[devops]] — map of DevOps & infrastructure: IaC, Terraform, environments, delivery
- [[system-design]] — map of all system design concepts, with learning order

## Concepts
- [[agent-development-lifecycle]] — ADLC: build → test → deploy → monitor loop for AI agents, plus iterate and govern
- [[agent-evaluation]] — evals: datasets, metrics, experiments and simulations to test agents
- [[agent-governance]] — cost control, tool access + audit trails, reuse across many agents
- [[agent-harness]] — agent tool layers: framework (abstractions) vs runtime (execution) vs harness (doing)
- [[agent-observability]] — traces, signals, feedback and dashboards for agents in production
- [[agent-runtime]] — production home for agents: durable execution, human-in-the-loop, sandboxes, context hub
- [[caching]] — keep slow-to-get data in a fast store; hits, misses, hit ratio, cache layers
- [[cache-patterns]] — cache-aside, read-through, write-through, write-back
- [[cache-eviction-policy]] — LRU, LFU, FIFO, TTL: what to remove when full
- [[cache-invalidation]] — keeping cached data fresh; thundering herd / stampede
- [[cdn]] — servers near users that cache static files
- [[context-engineering]] — build, version and monitor the business context agents reason with
- [[copy-on-write]] — share data on copy, duplicate a block only when written; cheap forks and snapshots
- [[differential-testing]] — run random inputs through production code and a reference model; flag disagreements
- [[ephemeral-environment]] — short-lived VM with every service, rebuilt from scratch often; lets agents test end to end
- [[eventual-consistency]] — copies may briefly disagree but converge; chosen for availability
- [[formal-verification]] — mathematically prove code meets its spec for all inputs; humans own spec, machines own proof
- [[graph-data-model]] — data as typed nodes (objects) and edges (associations)
- [[infrastructure-as-code]] — infra defined in versioned text files; declarative, reviewable, less drift
- [[grounding]] — tie every agent claim to fetched data; deterministic tools, model only narrates
- [[long-running-agent]] — agent working for hours/days: durable runtime, inboxes, forkable history, checkpointed sandboxes
- [[opentofu]] — open-source Linux Foundation fork of Terraform; drop-in, adds state encryption
- [[prompt-injection]] — attack via instructions hidden in text an agent reads; defences
- [[recursive-self-improvement]] — LLM loop that proposes, tests and keeps agent-harness edits; continual RSI across model/benchmark changes
- [[replication]] — copies of data across servers/regions; primary/secondary
- [[self-improvement-memory]] — SIM: optimizer's record of problems, edits, rationale, predicted vs observed outcomes
- [[sharding]] — splitting data across many servers; hot spots, rebalancing
- [[software-factory]] — repeatable, measurable software delivery loop; agent-native version uses coding agents
- [[terraform]] — HashiCorp's multi-cloud IaC tool: core, providers, state file, modules, plan/apply
- [[tao]] — Facebook's sharded, cache-first graph store (case study)

## Comparisons
- [[adlc-vs-sdlc]] — agent lifecycle (probabilistic, context + evals) vs classic software lifecycle (deterministic code)
- [[terraform-vs-cloudformation]] — multi-cloud HCL + self-managed state vs AWS-only with AWS-managed state
- [[opentofu-vs-terraform]] — same HCL workflow; open-source community governance vs HashiCorp BUSL
- [[redis-vs-memcached]] — rich data types + persistence vs simple multi-threaded KV

## Questions

## Sources
- [[caching-basics]] — starter notes on caching (2026-11-14)
- [[tao-the-power-of-the-graph]] — Facebook Engineering on TAO, its graph store (2013)
- [[inside-the-software-factory]] — Factory on what a software factory is and its agent-native form (2026)
- [[langchain-agent-development-lifecycle]] — LangChain (Harrison Chase) on the agent development lifecycle (2026)
- [[atlan-adlc-vs-sdlc]] — Atlan on how the agent lifecycle differs from the SDLC; context as a lifecycle (2026)
- [[google-automate-agent-lifecycle]] — Google Cloud tutorial: six-stage agent lifecycle driven from a coding agent (2026)
- [[lean4-formal-verification-for-engineers]] — Varun Pant (AWS) talk: Lean proofs for agent-written code, zlib, Cedar (2026)
- [[self-improvement-memory-crsi]] — Google paper: Self-Improvement Memory for continual recursive self-improvement of harnesses (2026)
- [[lovable-set-intelligence-free]] — Fabian Hedin (Lovable CTO) talk: durable runtimes, forkable sandboxes, Rust Vite rewrite (2026)
- [[cognition-40x-merged-prs]] — Walden Yan (Cognition CPO) talk: 40x merged PRs, pods, hourly VMs, agents given jobs (2026)
- [[what-is-terraform]] — GeeksforGeeks intro to Terraform: IaC, architecture, state, commands (2026)
- [[opentofu-homepage]] — OpenTofu project homepage: why the fork exists, unique features (2026)
