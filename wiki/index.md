# Index

Catalogue of every wiki page. Claude reads this first when answering questions.

## Topics
- [[ai-agents]] — map of AI agent concepts: building, testing, deploying, governing agents
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
- [[eventual-consistency]] — copies may briefly disagree but converge; chosen for availability
- [[graph-data-model]] — data as typed nodes (objects) and edges (associations)
- [[replication]] — copies of data across servers/regions; primary/secondary
- [[sharding]] — splitting data across many servers; hot spots, rebalancing
- [[software-factory]] — repeatable, measurable software delivery loop; agent-native version uses coding agents
- [[tao]] — Facebook's sharded, cache-first graph store (case study)

## Comparisons
- [[redis-vs-memcached]] — rich data types + persistence vs simple multi-threaded KV

## Questions

## Sources
- [[caching-basics]] — starter notes on caching (2026-11-14)
- [[tao-the-power-of-the-graph]] — Facebook Engineering on TAO, its graph store (2013)
- [[inside-the-software-factory]] — Factory on what a software factory is and its agent-native form (2026)
- [[langchain-agent-development-lifecycle]] — LangChain (Harrison Chase) on the agent development lifecycle (2026)
