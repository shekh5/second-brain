# Second Brain — Rules for Claude

This repo is a personal knowledge wiki maintained by Claude, following Karpathy's
"LLM Wiki" pattern. The owner adds sources and asks questions. Claude writes,
links, and maintains the wiki.

First topic: **system design**. Other topics may be added later under `wiki/topics/`.

## The three layers

| Folder | Owner | Rule |
|---|---|---|
| `raw/` | Human | **Never edit or delete anything here.** Read only. It is the source of truth. |
| `wiki/` | Claude | Claude creates and updates these pages. The human reads them. |
| `CLAUDE.md` | Both | These rules. Change them only when the human agrees. |

Inside `raw/`:
- `raw/articles/` — saved web articles (markdown, e.g. from Obsidian Web Clipper)
- `raw/notes/` — the owner's own notes, transcripts, or pasted text
- `raw/pdfs/` — papers and PDFs
- `raw/assets/` — images referenced by sources

Raw file naming: `YYYY-MM-DD-short-slug.md` (e.g. `2026-11-14-caching-basics.md`).

## Wiki page types

| Folder | Page type | One page per… | Example |
|---|---|---|---|
| `wiki/sources/` | source | raw file ingested | `sources/caching-basics.md` |
| `wiki/concepts/` | concept | idea, technique, or technology | `concepts/consistent-hashing.md` |
| `wiki/comparisons/` | comparison | "X vs Y" question | `comparisons/redis-vs-memcached.md` |
| `wiki/topics/` | topic | big area, as a map of its concepts | `topics/system-design.md` |
| `wiki/questions/` | question | good answer worth keeping | `questions/how-to-design-url-shortener.md` |

Special files:
- `wiki/index.md` — catalogue of **every** page: link + one-line summary, grouped by type. Always keep it complete.
- `wiki/log.md` — append-only history. Never rewrite old lines.

### File names
- lowercase, words joined by hyphens: `cache-invalidation.md`
- concept names are singular nouns: `load-balancer.md`, not `load-balancers.md`
- before creating a page, check `index.md` for an existing page with the same meaning (avoid duplicates such as `lb.md` next to `load-balancer.md`)

### Frontmatter (every wiki page)

```yaml
---
type: concept            # source | concept | comparison | topic | question
tags: [system-design, caching]
sources: [caching-basics] # source pages this page draws on (slugs)
created: 2026-11-14
updated: 2026-11-14
---
```

### Links
- Use Obsidian wiki links: `[[cache-invalidation]]` or `[[cache-invalidation|invalidation]]`.
- Link a concept the **first time** it is mentioned on a page. Don't link it again on that page.
- Every factual claim on concept, comparison, and question pages should trace to a source: end the sentence or paragraph with `(src: [[caching-basics]])`.
- If something is Claude's own reasoning or general knowledge rather than from a source, mark it: `(note: general knowledge, not from a source)`.

## Page templates

### Source page (`wiki/sources/<slug>.md`)
```markdown
# <Title of the source>

- **Raw file:** `raw/articles/2026-11-14-slug.md`
- **Author / origin:** …
- **Ingested:** 2026-11-14

## Summary
3–6 sentences in plain English.

## Key takeaways
- …

## Concepts touched
[[concept-a]], [[concept-b]]

## Open questions
Things the source left unclear, or claims to double-check.
```

### Concept page (`wiki/concepts/<slug>.md`)
```markdown
# <Concept name>

**In one line:** plain-English definition.

## How it works
Short explanation. Use a small ASCII diagram if it helps.

## Why it matters / when to use it

## Trade-offs
| Pro | Con |
|---|---|

## Real-world examples

## Related
[[other-concept]] — how it relates, in a few words

## Sources
- [[source-slug]]
```

### Comparison page
Title "X vs Y"; a table of dimensions; "When to pick X" / "When to pick Y"; sources.

### Question page
The question as title; the answer; sources; date asked.

### Topic page
A map: short intro, then concepts grouped into sections, each with a one-line hint, and a suggested learning order.

## Workflows

### Ingest (`/ingest <path>`)
1. Read the raw file fully. If it references images in `raw/assets/`, view them.
2. Tell the owner the 3–5 key takeaways and ask if anything should be emphasised or skipped. (Skip this if the owner said "just do it".)
3. Write the source page.
4. For each concept: update the existing page (merge, don't duplicate) or create a new page.
   - If the new source **contradicts** an existing page, don't silently overwrite it. Keep both claims, cite both, and add a `> ⚠️ Conflict:` callout.
5. Update the relevant topic page(s).
6. Update `index.md` with every new page.
7. Append to `log.md`.
8. Report: pages created, pages updated, conflicts found.

Ingest **one source at a time**.

### Ask (`/ask <question>`)
1. Read `index.md` first. Pick the relevant pages from it.
2. Read those pages (and follow links one hop if needed).
3. Answer with citations to wiki pages: `[[concept]]`.
4. If the wiki doesn't cover it, say so clearly, then answer from general knowledge marked as such, and suggest sources to add.
5. If the answer is useful and reusable, offer to save it as a question or comparison page (then update index and log).

### Lint (`/lint`)
Check and report (fix only what's safe, ask about the rest):
- pages missing from `index.md`, or index entries pointing to missing pages
- broken `[[links]]`
- orphan pages (no other page links to them)
- concepts mentioned in text without their own page
- unresolved `⚠️ Conflict` callouts
- pages missing frontmatter or sources
- stale pages (`updated` older than newer sources on the same tags)
Append a lint entry to `log.md`.

## log.md format
One line per event, newest at the bottom, fixed prefixes so it can be grepped:

```
2026-11-14 INGEST raw/notes/2026-11-14-caching-basics.md → +5 pages, ~1 updated
2026-11-14 ASK "redis vs memcached?" → saved comparisons/redis-vs-memcached.md
2026-11-14 LINT 2 broken links fixed, 1 orphan reported
2026-11-14 SCHEMA added question page type
```

## Writing style
- Plain, simple English. The owner is learning, so explain jargon the first time it's used.
- Short paragraphs, tables for trade-offs, small diagrams where useful.
- On system-design pages, always include a **trade-offs** section and **real-world examples**.

## Git
After each ingest, ask, or lint that changes files, commit with a message like
`ingest: caching-basics` / `ask: redis vs memcached` / `lint: weekly`.
