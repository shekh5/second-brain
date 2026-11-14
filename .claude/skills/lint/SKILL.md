---
name: lint
description: Health-check the second-brain wiki — broken links, orphans, missing index entries, missing concept pages, unresolved conflicts, stale pages. Use when the user says "lint", "check my wiki", or "clean up".
---

# Lint the wiki

Follow the **Lint** workflow in `CLAUDE.md`.

Start with the mechanical checks using the helper script:

```bash
python3 scripts/lint.py
```

It reports broken links, orphan pages, pages missing from the index, index entries pointing nowhere, and pages missing frontmatter.

Then do the checks that need judgement by reading pages:
- concepts mentioned often in text but with no page of their own
- unresolved `⚠️ Conflict` callouts
- stale pages (older `updated` date than newer sources on the same topic)
- weak pages (no trade-offs, no examples, no sources)

Fix safe things (index entries, obvious broken links). Ask before merging, deleting, or rewriting pages.
Append a `LINT` line to `wiki/log.md` and commit `lint: <date>`.
Finish with a short report: fixed / needs your decision / suggested sources to fill gaps.
