#!/usr/bin/env python3
"""Build the reports web page from the YAML files in data/.

Each data/<company>.yaml file lists a company's model families and their
releases. The script validates every file, then writes:

    <out>/reports.json   all releases as JSON
    <out>/index.html     all releases embedded
    <out>/<cat>.html     one page per category (llm.html, vla.html, ...)

Openness and category are inherited: release > family > company.

Exits non-zero on any validation error, so CI catches bad data.

Usage: python3 scripts/build_site.py [--out _site]
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE = ROOT / "site" / "index.html"
DATA_PLACEHOLDER = "/*__REPORTS_DATA__*/null"
PAGE_PLACEHOLDER = "/*__PAGE__*/null"
TITLE_TAG = "<title>Model Tech Reports</title>"

CATEGORIES = {
    "llm": "LLMs and VLMs",
    "vla": "VLAs",
    "world-model": "World Models",
    "image-video": "Image and Video",
    "speech": "Speech and Audio",
}
OPENNESS = {"open", "closed", "unknown"}
WRITEUP_KINDS = {"report", "blog", "model-card", "docs"}

COMPANY_KEYS = {"company", "openness", "families"}
FAMILY_KEYS = {"name", "category", "openness", "releases"}
RELEASE_KEYS = {"name", "date", "openness", "category", "note", "weights", "writeups", "related"}
WRITEUP_KEYS = {"kind", "title", "url"}
RELATED_KEYS = {"title", "author", "url"}

DATE_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
URL_RE = re.compile(r"^https?://\S+$")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")


class Validator:
    def __init__(self):
        self.errors = []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def mapping(self, obj, where, allowed, required):
        if not isinstance(obj, dict):
            self.error(where, f"expected a mapping, got {type(obj).__name__}")
            return False
        for k in obj.keys() - allowed:
            self.error(where, f"unknown key '{k}'")
        for k in required - obj.keys():
            self.error(where, f"missing required key '{k}'")
        return True

    def string(self, obj, key, where, required=True):
        v = obj.get(key)
        if v is None:
            return None if not required else self.error(where, f"'{key}' is required")
        if not isinstance(v, str) or not v.strip():
            self.error(where, f"'{key}' must be a non-empty string")
            return None
        return v

    def enum(self, obj, key, allowed, where):
        v = obj.get(key)
        if v is not None and v not in allowed:
            self.error(where, f"'{key}' must be one of {sorted(allowed)}, got {v!r}")
            return None
        return v

    def url(self, v, where):
        if not isinstance(v, str) or not URL_RE.match(v):
            self.error(where, f"invalid URL {v!r}")
            return None
        return v

    def items(self, obj, key, where, required=False):
        v = obj.get(key)
        if v is None:
            if required:
                self.error(where, f"'{key}' is required")
            return []
        if not isinstance(v, list) or (required and not v):
            self.error(where, f"'{key}' must be a {'non-empty ' if required else ''}list")
            return []
        return v


def load_file(path, v):
    """Validate one company file and return its releases as flat records."""
    rel_path = path.relative_to(ROOT).as_posix()
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        v.error(rel_path, f"invalid YAML: {e}")
        return []
    if not v.mapping(doc, rel_path, COMPANY_KEYS, COMPANY_KEYS):
        return []

    company = v.string(doc, "company", rel_path)
    company_open = v.enum(doc, "openness", OPENNESS, rel_path)
    records = []
    for fi, fam in enumerate(v.items(doc, "families", rel_path, required=True)):
        fwhere = f"{rel_path}: families[{fi}]"
        if not v.mapping(fam, fwhere, FAMILY_KEYS, {"name", "category", "releases"}):
            continue
        family = v.string(fam, "name", fwhere)
        fwhere = f"{rel_path}: {family}"
        family_cat = v.enum(fam, "category", CATEGORIES, fwhere)
        family_open = v.enum(fam, "openness", OPENNESS, fwhere)

        for ri, rel in enumerate(v.items(fam, "releases", fwhere, required=True)):
            rwhere = f"{fwhere}: releases[{ri}]"
            if not v.mapping(rel, rwhere, RELEASE_KEYS, {"name", "date", "writeups"}):
                continue
            name = v.string(rel, "name", rwhere)
            rwhere = f"{fwhere}: {name}"
            date = rel.get("date")
            if not isinstance(date, str) or not DATE_RE.match(date):
                v.error(rwhere, f"'date' must be YYYY-MM, got {date!r}")

            writeups = []
            for wi, w in enumerate(v.items(rel, "writeups", rwhere, required=True)):
                wwhere = f"{rwhere}: writeups[{wi}]"
                if not v.mapping(w, wwhere, WRITEUP_KEYS, WRITEUP_KEYS):
                    continue
                v.enum(w, "kind", WRITEUP_KINDS, wwhere)
                v.string(w, "title", wwhere)
                v.url(w.get("url"), wwhere)
                arxiv = ARXIV_RE.search(w.get("url") or "")
                writeups.append({**w, "arxiv": arxiv.group(1) if arxiv else None})

            related = []
            for xi, x in enumerate(v.items(rel, "related", rwhere)):
                xwhere = f"{rwhere}: related[{xi}]"
                if not v.mapping(x, xwhere, RELATED_KEYS, {"title", "url"}):
                    continue
                v.string(x, "title", xwhere)
                v.string(x, "author", xwhere, required=False)
                v.url(x.get("url"), xwhere)
                related.append(x)

            weights = [u for u in v.items(rel, "weights", rwhere) if v.url(u, f"{rwhere}: weights")]

            records.append(
                {
                    "name": name,
                    "date": date,
                    "company": company,
                    "family": family,
                    "category": v.enum(rel, "category", CATEGORIES, rwhere) or family_cat,
                    "openness": v.enum(rel, "openness", OPENNESS, rwhere) or family_open or company_open,
                    "note": v.string(rel, "note", rwhere, required=False),
                    "writeups": writeups,
                    "weights": weights,
                    "related": related,
                    "source": rel_path,
                }
            )
    return records


def load_releases():
    """Load and validate every data file. Raises ValueError listing all errors."""
    v = Validator()
    records = []
    for path in sorted(DATA_DIR.glob("*.yaml")):
        records.extend(load_file(path, v))

    # The same write-up URL should never appear twice.
    seen = {}
    for r in records:
        for w in r["writeups"]:
            url = w.get("url")
            if url in seen:
                v.error(r["source"], f"{r['name']}: write-up URL also used by {seen[url]}: {url}")
            seen[url] = f"{r['source']} ({r['name']})"

    if v.errors:
        raise ValueError("\n".join(v.errors))
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="_site", help="output directory (default: _site)")
    args = parser.parse_args()

    try:
        releases = load_releases()
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1

    data = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "categories": CATEGORIES,
        "releases": releases,
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "reports.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    template = TEMPLATE.read_text(encoding="utf-8")
    for token in (DATA_PLACEHOLDER, PAGE_PLACEHOLDER, TITLE_TAG):
        if token not in template:
            print(f"{TEMPLATE}: missing placeholder {token}", file=sys.stderr)
            return 1
    # Escape "</" so titles can't close the <script> tag.
    embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    def write_page(page, name):
        html = template.replace(DATA_PLACEHOLDER, embedded)
        html = html.replace(PAGE_PLACEHOLDER, json.dumps(page))
        if page:
            html = html.replace(TITLE_TAG, f"<title>{CATEGORIES[page]} · Model Tech Reports</title>")
        (out / name).write_text(html, encoding="utf-8")

    write_page(None, "index.html")
    for cat in CATEGORIES:
        write_page(cat, f"{cat}.html")

    counts = {}
    for r in releases:
        counts[r["openness"]] = counts.get(r["openness"], 0) + 1
    summary = ", ".join(f"{n} {k}" for k, n in sorted(counts.items()))
    n_writeups = sum(len(r["writeups"]) for r in releases)
    print(f"Wrote {len(releases)} releases, {n_writeups} write-ups ({summary}) to {1 + len(CATEGORIES)} pages in {out}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
