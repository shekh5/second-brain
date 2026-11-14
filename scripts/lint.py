#!/usr/bin/env python3
"""Mechanical health checks for the wiki. No dependencies.

Checks:
  - broken [[links]]            (link target page doesn't exist)
  - orphan pages                (no other page links to them)
  - pages missing from index.md
  - index entries pointing to missing pages
  - pages missing frontmatter

Usage: python3 scripts/lint.py   (exit code 1 if problems found)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SPECIAL = {"index", "log"}
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def main() -> int:
    pages = {p.stem: p for p in WIKI.rglob("*.md")}
    content = {name: p.read_text(encoding="utf-8") for name, p in pages.items()}

    broken, inbound = [], {name: 0 for name in pages}
    for name, text in content.items():
        for target in set(LINK_RE.findall(text)):
            target = target.strip()
            if target not in pages:
                broken.append((name, target))
            elif target != name and name not in SPECIAL:
                inbound[target] += 1

    index_links = set(t.strip() for t in LINK_RE.findall(content.get("index", "")))
    regular = [n for n in pages if n not in SPECIAL]
    missing_from_index = sorted(n for n in regular if n not in index_links)
    dead_index = sorted(t for t in index_links if t not in pages)
    orphans = sorted(n for n in regular if inbound[n] == 0)
    no_frontmatter = sorted(n for n in regular if not content[n].startswith("---"))

    sections = [
        ("Broken links (page -> missing target)", [f"{a} -> {b}" for a, b in sorted(broken)]),
        ("Orphan pages (nothing links to them)", orphans),
        ("Missing from index.md", missing_from_index),
        ("index.md entries with no page", dead_index),
        ("Missing frontmatter", no_frontmatter),
    ]
    problems = 0
    print(f"Wiki: {len(regular)} pages\n")
    for title, items in sections:
        mark = "OK " if not items else "!! "
        print(f"{mark}{title}: {len(items)}")
        for item in items:
            print(f"     - {item}")
        problems += len(items)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
