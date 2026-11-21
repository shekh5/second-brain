---
type: concept
tags: [ai-agents, llm, data, privacy]
sources: [anatomy-of-effective-commerce-agents]
created: 2026-11-21
updated: 2026-11-21
---

# Agent memory

**In one line:** facts an agent keeps about a user across conversations (sizes, preferences,
past orders), stored outside the model so later sessions can use them.

## How it works
The model itself forgets everything between conversations; memory is an app-side database the
agent reads from and writes to (note: general knowledge, not from a source). The commerce-agent guide
recommends (src: [[anatomy-of-effective-commerce-agents]]):

- **Typed records in your own database**, e.g. `{person: 42, kind: "shoe_size", value: "EU 43"}` — not a blob of free text.
- **Extract asynchronously:** a background job pulls facts out of finished conversations, so the live chat isn't slowed down.
- **Keyed per person**, so one user's facts never leak into another's session.
- **User control:** people can see and delete what is remembered.
- **Retention periods:** facts expire.

```
 conversation ──(after)──► extractor job ──► memory DB (typed, per person, TTL)
                                                  │
 next conversation ◄──── load relevant facts ─────┘
```

## Why it matters / when to use it
Memory makes an agent feel personal (no re-asking your size) but it is also personal data, so it
needs privacy controls from day one (src: [[anatomy-of-effective-commerce-agents]]).

## Trade-offs
| Pro | Con |
|---|---|
| Personalised help without re-asking (note: general knowledge, not from a source) | Stores personal data → privacy duty, deletion, retention (src: [[anatomy-of-effective-commerce-agents]]) |
| Typed records are queryable, testable and auditable (src: [[anatomy-of-effective-commerce-agents]]) | Extraction can save wrong or outdated facts (note: general knowledge, not from a source) |
| Async extraction keeps chat fast (src: [[anatomy-of-effective-commerce-agents]]) | Memories appear with a delay, not instantly (note: general knowledge, not from a source) |

## Real-world examples
- Commerce agents remembering preferences per shopper, with a page to view and delete them (src: [[anatomy-of-effective-commerce-agents]]).

## Related
[[self-improvement-memory]] — a different kind of memory: an optimizer's record of its own edits, not facts about users
[[context-engineering]] — memory is one input into the agent's context
[[long-running-agent]] — long-lived agents also need state outside the model

## Sources
- [[anatomy-of-effective-commerce-agents]]
