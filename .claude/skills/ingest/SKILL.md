---
name: ingest
description: Ingest one raw source file into the second-brain wiki — write its source page, create or update concept pages, update topics, index.md and log.md. Use when the user says "ingest", "read this", "add this to my brain", or adds a file to raw/.
---

# Ingest a source

Argument: a path inside `raw/` (e.g. `raw/articles/2026-11-14-cap-theorem.md`).
If no path is given, list files in `raw/` that are not yet mentioned in `wiki/log.md` and ask which one.

If the user pasted text or a URL instead of a file: save it first as
`raw/notes/YYYY-MM-DD-slug.md` (or `raw/articles/…`), with the origin URL at the top, then ingest that file.

Follow the **Ingest** workflow in `CLAUDE.md` exactly:

1. Read the whole raw file. Never modify it.
2. Read `wiki/index.md` to learn which pages already exist.
3. Share 3–5 key takeaways with the user; ask if anything should be emphasised or skipped (skip asking if they said "just do it").
4. Write `wiki/sources/<slug>.md` using the source template.
5. Create or update concept pages. Merge into existing pages, never duplicate. Flag contradictions with a `> ⚠️ Conflict:` callout citing both sources.
6. Update the relevant `wiki/topics/` page(s).
7. Add every new page to `wiki/index.md`.
8. Append one `INGEST` line to `wiki/log.md`.
9. Commit and push: `git add -A && git commit -m "ingest: <slug>" && git push`.
10. Report: pages created, pages updated, conflicts, and 1–2 suggested next sources to read.
