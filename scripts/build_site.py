#!/usr/bin/env python3
"""Build a sortable, filterable web page from the report list pages.

Parses each category page (llms.md, etc.) into structured records, validates
them, and writes:

    <out>/reports.json   all entries as JSON
    <out>/index.html     site/index.html with the entries embedded

Openness (open/closed) is inferred from the markdown itself:

  1. A family heading ending in "(closed)" or "(open-weight)" wins.
  2. Otherwise the company's section in the page intro decides: companies
     listed after "**Open-weight labs**" are open, after "**Closed ...**"
     are closed.
  3. Otherwise the entry is "unknown".

Exits non-zero if an entry line is malformed, so CI catches formatting
mistakes.

Usage: python3 scripts/build_site.py [--out _site]
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "llms.md",
    "vla-and-world-models.md",
    "image-and-video.md",
    "speech-and-audio.md",
]
TEMPLATE = ROOT / "site" / "index.html"
DATA_PLACEHOLDER = "/*__REPORTS_DATA__*/null"

ENTRY_RE = re.compile(
    r"^- (?P<date>\d{4}-\d{2}) · \[(?P<title>.+?)\]\((?P<url>https?://[^\s)]+)\)(?P<rest>.*)$"
)
KIND_RE = re.compile(r"\*\((?P<kind>[^)]+)\)\*")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
LAB_LINK_RE = re.compile(r"\[([^\]]+)\]\(#[^)]*\)")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
FAMILY_OPENNESS_RE = re.compile(r"\s*\((closed|open-weight|open)\)\s*$", re.I)


class ParseError(Exception):
    pass


def parse_page(path):
    """Return (page_title, entries) for one category page."""
    lines = path.read_text(encoding="utf-8").splitlines()
    page_title = None
    lab_openness = {}  # company name -> "open" | "closed"
    intro_mode = None
    in_body = False
    company = family = None
    family_openness = None
    entries = []
    errors = []

    for lineno, line in enumerate(lines, 1):
        if line.startswith("# ") and page_title is None:
            page_title = line[2:].strip()
            continue

        if not in_body:
            # Intro: collect the open/closed lab lists until the first "---".
            if line.strip() == "---":
                in_body = True
            elif line.startswith("**Open"):
                intro_mode = "open"
            elif line.startswith("**Closed"):
                intro_mode = "closed"
            elif intro_mode:
                for name in LAB_LINK_RE.findall(line):
                    lab_openness[name] = intro_mode
            continue

        if line.startswith("## "):
            company = line[3:].strip()
            family = None
            family_openness = None
        elif line.startswith("### "):
            heading = line[4:].strip()
            m = FAMILY_OPENNESS_RE.search(heading)
            family_openness = None
            if m:
                family_openness = "closed" if m.group(1).lower() == "closed" else "open"
                heading = heading[: m.start()].strip()
            family = heading
        elif re.match(r"^- \d", line):
            m = ENTRY_RE.match(line)
            if not m:
                errors.append(f"{path.name}:{lineno}: malformed entry: {line}")
                continue
            date = m["date"]
            month = int(date[5:])
            if not 1 <= month <= 12:
                errors.append(f"{path.name}:{lineno}: bad month in date {date}")
                continue
            if company is None:
                errors.append(f"{path.name}:{lineno}: entry outside a company section")
                continue

            rest = m["rest"]
            kind_m = KIND_RE.search(rest)
            kind = kind_m["kind"].strip() if kind_m else "report"
            if kind_m:
                rest = rest[: kind_m.start()] + rest[kind_m.end() :]
            note = LINK_RE.sub(r"\1", rest).strip(" .·")
            if re.fullmatch(r"\([^()]*\)", note):  # "(GPT-1)" -> "GPT-1"
                note = note[1:-1]

            openness = family_openness or lab_openness.get(company) or "unknown"
            arxiv = ARXIV_RE.search(m["url"])
            entries.append(
                {
                    "date": date,
                    "title": m["title"],
                    "url": m["url"],
                    "arxiv": arxiv.group(1) if arxiv else None,
                    "kind": kind,
                    "note": note or None,
                    "openness": openness,
                    "company": company,
                    "family": family,
                    "category": page_title,
                    "source": f"{path.name}#L{lineno}",
                }
            )

    if errors:
        raise ParseError("\n".join(errors))
    return page_title, entries


def load_entries():
    """Load all entries from the local markdown pages.

    This is the single data-source hook: swap or extend it later (e.g. to
    enrich entries with arXiv metadata) without touching the page.
    """
    entries, errors = [], []
    for name in PAGES:
        try:
            _, page_entries = parse_page(ROOT / name)
            entries.extend(page_entries)
        except ParseError as e:
            errors.append(str(e))
    if errors:
        raise ParseError("\n".join(errors))
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="_site", help="output directory (default: _site)")
    args = parser.parse_args()

    try:
        entries = load_entries()
    except ParseError as e:
        print(e, file=sys.stderr)
        return 1

    data = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "entries": entries,
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "reports.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    template = TEMPLATE.read_text(encoding="utf-8")
    if DATA_PLACEHOLDER not in template:
        print(f"{TEMPLATE}: missing data placeholder {DATA_PLACEHOLDER}", file=sys.stderr)
        return 1
    # Escape "</" so titles can't close the <script> tag.
    embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    (out / "index.html").write_text(template.replace(DATA_PLACEHOLDER, embedded), encoding="utf-8")

    counts = {}
    for e in entries:
        counts[e["openness"]] = counts.get(e["openness"], 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    print(f"Wrote {len(entries)} entries ({summary}) to {out}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
