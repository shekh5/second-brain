---
name: ask
description: Answer a question from the second-brain wiki with citations, and optionally save the answer as a new wiki page. Use when the user asks a question about anything they have studied or saved.
---

# Ask the wiki

Follow the **Ask** workflow in `CLAUDE.md`:

1. Read `wiki/index.md` first and choose the relevant pages from it. Don't scan the whole folder.
2. Read those pages; follow `[[links]]` one hop if needed.
3. Answer in plain English, citing pages as `[[page]]`.
4. Clearly separate what comes from the wiki and what is general knowledge (`note: general knowledge`).
5. If the wiki has gaps, say what's missing and suggest 1–2 sources to add.
6. If the answer is reusable, ask: "Save this as a page?" On yes, write it to `wiki/questions/` or `wiki/comparisons/`, update `index.md`, append an `ASK` line to `log.md`, then commit and push: `git add -A && git commit -m "ask: <short question>" && git push`.
