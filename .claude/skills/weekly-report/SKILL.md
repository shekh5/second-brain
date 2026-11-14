---
name: weekly-report
description: Weekly health check and learning summary for the second brain — runs lint, writes reports/YYYY-MM-DD.md, and sends a short version on Telegram. Runs every Sunday on a schedule; also use when the user asks for "weekly report".
---

# Weekly report

Runs **unattended**: don't ask questions; fix only safe things.

1. `git pull --rebase`
2. Run the `lint` skill (mechanical checks with `python3 scripts/lint.py`, plus judgement checks).
   Fix safe issues automatically. List anything that needs the owner's decision.
3. Gather the week's activity from `wiki/log.md` (last 7 days) and `inbox/failed/`.
4. Write `reports/YYYY-MM-DD.md`:

```markdown
# Weekly report — YYYY-MM-DD

## This week
- Sources ingested: N (list with links to wiki/sources pages)
- Pages created: N · updated: N
- Links that failed: N (list)

## Wiki health
- ✅ / ⚠️ each lint check, with counts
- Fixed automatically: …
- Needs your decision: …

## Learning progress (system design map)
- Topics covered: X of Y in wiki/topics/system-design.md
- Covered this week: …
- Suggested next 2 reads: … (follow the map's learning order)

## Quiz yourself
3 short questions based on this week's pages, with the answer page linked.
```

5. Append `YYYY-MM-DD REPORT reports/YYYY-MM-DD.md` to `wiki/log.md`.
6. Commit and push: `git add -A && git commit -m "report: YYYY-MM-DD" && git push`.
7. Send a short version (≤ 10 lines, with the GitHub link
   `https://github.com/shekh5/second-brain/blob/main/reports/YYYY-MM-DD.md`) via
   `python3 scripts/telegram_inbox.py send "<text>"`.
8. End your final message with the same short summary: the scheduler emails it and sends it
   as a phone notification.
