#!/usr/bin/env python3
"""Telegram inbox for the second brain. No dependencies.

Commands:
  fetch      Pull new messages from the bot into inbox/pending/ (one JSON file each).
  send TEXT  Send a message to the owner's chat.
  whoami     Show chat ids of recent messages (used once during setup).

Environment:
  TELEGRAM_BOT_TOKEN        bot token from @BotFather (secret)
  TELEGRAM_ALLOWED_CHAT_ID  only messages from this chat are accepted
  TELEGRAM_API_BASE         optional, for tests (default https://api.telegram.org)

Design notes (system design):
  - inbox/pending/ is a QUEUE. Each message becomes one file named by Telegram's
    update_id, so fetching the same message twice overwrites the same file
    (idempotent) instead of creating a duplicate.
  - The read position ("offset") is saved in inbox/state.json. Telegram forgets
    a message only after we ask with a higher offset, so the offset is advanced
    only AFTER the files are written. A crash in between means re-fetching
    (safe, idempotent) rather than losing messages: at-least-once delivery.
  - Telegram keeps unfetched messages for ~24 hours only (retention), so the
    fetch must run at least once a day.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"
PENDING = INBOX / "pending"
STATE = INBOX / "state.json"
URL_RE = re.compile(r"https?://\S+")


def api(method: str, **params):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        sys.exit("TELEGRAM_BOT_TOKEN is not set (add it in the environment settings).")
    base = os.environ.get("TELEGRAM_API_BASE", "https://api.telegram.org")
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(f"{base}/bot{token}/{method}", data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.load(resp)
    if not body.get("ok"):
        sys.exit(f"Telegram error: {body}")
    return body["result"]


def allowed_chat() -> str:
    chat = os.environ.get("TELEGRAM_ALLOWED_CHAT_ID")
    if not chat:
        sys.exit("TELEGRAM_ALLOWED_CHAT_ID is not set. Run `whoami` to find it.")
    return chat


def load_state() -> dict:
    return json.loads(STATE.read_text()) if STATE.exists() else {"offset": 0}


def fetch() -> None:
    chat_id = allowed_chat()
    state = load_state()
    updates = api("getUpdates", offset=state["offset"], timeout=0, allowed_updates='["message"]')
    PENDING.mkdir(parents=True, exist_ok=True)

    saved, ignored = 0, 0
    for upd in updates:
        msg = upd.get("message") or {}
        text = (msg.get("text") or msg.get("caption") or "").strip()
        if str(msg.get("chat", {}).get("id")) != chat_id or not text or text.startswith("/"):
            ignored += 1  # strangers, empty messages, bot commands like /start
            continue
        item = {
            "update_id": upd["update_id"],
            "received": datetime.fromtimestamp(msg["date"], timezone.utc).isoformat(),
            "text": text,
            "urls": URL_RE.findall(text),
            "attempts": 0,
        }
        (PENDING / f"{upd['update_id']}.json").write_text(json.dumps(item, indent=2) + "\n")
        saved += 1

    if updates:
        # Advance only after every file is written (see design notes).
        state["offset"] = updates[-1]["update_id"] + 1
        STATE.write_text(json.dumps(state, indent=2) + "\n")
        api("getUpdates", offset=state["offset"], timeout=0)  # tell Telegram: these are done

    print(f"fetched={len(updates)} saved={saved} ignored={ignored} "
          f"pending_total={len(list(PENDING.glob('*.json')))}")


def send(text: str) -> None:
    api("sendMessage", chat_id=allowed_chat(), text=text[:4000], disable_web_page_preview="true")
    print("sent")


def whoami() -> None:
    for upd in api("getUpdates", timeout=0):
        msg = upd.get("message") or {}
        chat = msg.get("chat", {})
        print(f"chat_id={chat.get('id')}  from={chat.get('username') or chat.get('first_name')}  "
              f"text={msg.get('text', '')[:40]!r}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "fetch":
        fetch()
    elif cmd == "send" and len(sys.argv) > 2:
        send(" ".join(sys.argv[2:]))
    elif cmd == "whoami":
        whoami()
    else:
        sys.exit(__doc__)
