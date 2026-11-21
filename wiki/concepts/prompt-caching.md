---
type: concept
tags: [ai-agents, llm, caching, cost]
sources: [anatomy-of-effective-commerce-agents]
created: 2026-11-21
updated: 2026-11-21
---

# Prompt caching

**In one line:** the model provider reuses the work it already did on the unchanged start of your
prompt, so repeated requests are cheaper and faster — as long as that start stays byte-for-byte identical.

## How it works
It's [[caching]] applied to LLM prompts. The provider caches the processed **prefix** of a prompt.
The next request that begins with exactly the same bytes is a cache hit for that part; everything
after the first changed byte is processed again (note: general knowledge, not from a source).

So order the prompt from most stable to least stable (src: [[anatomy-of-effective-commerce-agents]]):

```
 ┌──────────────────────────────┬────────────────────┬──────────────────┐
 │ global prompt + tools        │ session context    │ volatile values  │
 │ (byte-identical for everyone)│ (same all session) │ (timestamp, etc.)│
 └──────────────────────────────┴────────────────────┴──────────────────┘
   cached across all users         cached per session    never cached
```

A timestamp at the *top* of the prompt would change every request and make the whole cache miss
(note: general knowledge, not from a source).

## Why it matters / when to use it
For agents it is **the main cost lever**; the commerce-agent guide targets **90–99% cache hit
rates** (src: [[anatomy-of-effective-commerce-agents]]). Agents re-send the same long system prompt
and tool list on every turn, so most input tokens can be cache hits (note: general knowledge, not from a source).
Judge the result by **cost per completed task**, not per call (src: [[anatomy-of-effective-commerce-agents]]).

## Trade-offs
| Pro | Con |
|---|---|
| Large cost and latency savings on repeated prefixes (src: [[anatomy-of-effective-commerce-agents]]) | Any tiny change early in the prompt (reordered tools, a date) breaks the cache (note: general knowledge, not from a source) |
| Free to use: just order the prompt well (note: general knowledge, not from a source) | Cache entries expire after a short time, so rarely-used prompts gain little (note: general knowledge, not from a source) |
| Rewards a small, stable system prompt (see [[agent-skill]]) | Personalising the top of the prompt per user lowers the hit rate (note: general knowledge, not from a source) |

## Real-world examples
- Commerce agents: global prompt first, then session context, timestamps last → 90–99% hit-rate target (src: [[anatomy-of-effective-commerce-agents]]).

## Related
[[caching]] — the general idea: hit ratio, keep hot data in a fast store
[[agent-governance]] — caching is a big part of controlling agent cost

## Sources
- [[anatomy-of-effective-commerce-agents]]
