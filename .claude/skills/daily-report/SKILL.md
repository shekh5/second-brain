---
name: daily-report
description: Short daily learning nudge for the second brain — what was added today, a quick recap of one concept, 2 quiz questions and the next suggested read, sent on Telegram. Runs every evening on a schedule; also use when the user asks for "daily report" or "today's summary".
---

# Daily report

Runs **unattended**: don't ask questions. It is **read-only**: it changes no files and makes no
commits, so it works even if the session can't push.

1. `git checkout main && git pull --rebase`
2. Find today's activity (UTC date): lines in `wiki/log.md` starting with today's date, and
   pages whose frontmatter `created:` or `updated:` is today.
3. Pick **one concept to recap**:
   - if something was ingested today → a concept page created today;
   - otherwise → a page created earlier, to space out revision (prefer one not recapped
     recently; vary the choice day to day).
4. Pick the **next suggested read**: the first ⬜ item in the learning order of
   `wiki/topics/system-design.md`.
5. Send **one** Telegram message (≤ 15 lines) with
   `python3 scripts/telegram_inbox.py send "<text>"`:

```
🧠 Daily brain — 14 Nov
📥 Today: TAO article → 6 new pages (sharding, replication, …)
   (or: "Nothing new today — here's a revision")

💡 Recap: Sharding
Split data across many servers by a shard key. Watch for hot spots…  (2–3 lines)

❓ Quiz
1. Why did Facebook pick eventual consistency for TAO?
2. What is a hot shard, and one way to fix it?
(answers: wiki/concepts/sharding.md, wiki/concepts/eventual-consistency.md)

📖 Next read: CAP theorem — send me a link!
```

6. End your final message with the same text.

Answers in the quiz must come from wiki pages, not general knowledge.
