---
name: process-inbox
description: Pull new links/notes sent to the Telegram bot, ingest each one into the wiki, and report back on Telegram. Runs automatically on a schedule; also use when the user says "process inbox" or "check telegram".
---

# Process the inbox

This runs **unattended** (no human watching), so never stop to ask questions:
ingest in "just do it" mode and make sensible choices.

## 1. Sync
```bash
git pull --rebase
python3 scripts/telegram_inbox.py fetch
git add -A && git commit -m "inbox: fetch" && git push   # only if something changed
```
Committing the fetched items **before** processing them means a crash later can't lose them.

## 2. Process each file in `inbox/pending/` (oldest `update_id` first)

For each item:

1. **Duplicate check.** If any URL in the item already appears in `wiki/log.md` or as an
   `Origin:` line in `raw/`, it was ingested before: move the item to `inbox/done/` with
   `"result": "duplicate"`, and continue.
2. **Save the raw source** (never edit it afterwards):
   - Item has a URL → fetch the page (WebFetch tool, or the web-fetch agent), and save the
     readable article text as `raw/articles/YYYY-MM-DD-<slug>.md` with a header:
     `> Origin: <url>` and `> Received via Telegram: <received>`.
     For YouTube, save the transcript if obtainable; otherwise the description.
   - Item is plain text (no URL) → save as `raw/notes/YYYY-MM-DD-<slug>.md` with
     `> Origin: Telegram note`.
   - Any extra words the owner wrote next to the link are their comment: keep them in
     the raw file under `## Owner's note`, and give them weight during ingest.
3. **Ingest** it with the `ingest` skill (no questions; "just do it").
4. **Mark done:** add `"result": "ingested"`, `"raw": "<path>"`, `"pages": [...]` to the item
   and move it to `inbox/done/`.
5. **Commit and push** after *each* item: `ingest: <slug> (via telegram)`.

### If an item fails (page can't be fetched, paywall, blocked site, etc.)
- Increase `"attempts"` and record `"last_error"` in the item file; leave it in `pending/`.
- When `attempts` reaches **3**, move it to `inbox/failed/` and tell the owner on Telegram
  that the link couldn't be read and they can paste the article text instead.
- One bad item must never stop the others.

## 3. Report on Telegram
Send **one** short summary (skip if nothing was processed and nothing failed):

```
🧠 Second brain updated
✅ Load balancing explained → 4 new pages, 2 updated
✅ Note on sharding → 1 new page
⚠️ 1 link failed (will retry): https://…
Next suggested read: consistent hashing
```
```bash
python3 scripts/telegram_inbox.py send "<summary>"
```

## 4. Finish
Append to `wiki/log.md`: `YYYY-MM-DD INBOX processed=N failed=M`, then commit and push.
Make sure `git status` is clean and nothing is unpushed.
