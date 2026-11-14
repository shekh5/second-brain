# Index

Catalogue of every wiki page. Claude reads this first when answering questions.

## Topics
- [[system-design]] — map of all system design concepts, with learning order

## Concepts
- [[caching]] — keep slow-to-get data in a fast store; hits, misses, hit ratio, cache layers
- [[cache-patterns]] — cache-aside, read-through, write-through, write-back
- [[cache-eviction-policy]] — LRU, LFU, FIFO, TTL: what to remove when full
- [[cache-invalidation]] — keeping cached data fresh; thundering herd / stampede
- [[cdn]] — servers near users that cache static files
- [[eventual-consistency]] — copies may briefly disagree but converge; chosen for availability
- [[graph-data-model]] — data as typed nodes (objects) and edges (associations)
- [[replication]] — copies of data across servers/regions; primary/secondary
- [[sharding]] — splitting data across many servers; hot spots, rebalancing
- [[tao]] — Facebook's sharded, cache-first graph store (case study)

## Comparisons
- [[redis-vs-memcached]] — rich data types + persistence vs simple multi-threaded KV

## Questions

## Sources
- [[caching-basics]] — starter notes on caching (2026-11-14)
- [[tao-the-power-of-the-graph]] — Facebook Engineering on TAO, its graph store (2013)
