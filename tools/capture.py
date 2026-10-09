#!/usr/bin/env python3
"""capture.py — Digital Resilience Library acquisition gate.

Operationalises the FRAMEWORK §7 / retrieval-RUNBOOK capture step: fetch a vetted
source from sources-registry.md, store it as a self-contained offline artifact under
library/reference/<CAT>/, compute its sha256, register it in BOTH catalog.json and
pwa/library.json (same-commit index rule), and append a capture log line.

Stdlib-only (urllib, hashli, html.parser, json) — no external deps, so it runs on
any machine that has python3, including offline/cold mirrors. Fits the repo's
"no deps, offline-first" rule and the autonomy mandate (deterministic, repeatable).

The 4 validation gates live in tools/validate.sh and run over everything this script
lands. capture.py is the *fetch+store+register* half; it deliberately does NOT decide
editorial/licensing questions — call it with a source already present in
sources-registry.md (gate 1: source) and let validate.sh enforce the rest.

Usage (from repo root):
  python3 tools/capture.py --url <URL> --name <registry name> --category <CAT> \
      --part Reference --license '<text>' --authority '<org>' \
      --priority T1 [--out library/reference/<CAT>/<slug>.md] [--dry-run] [--log]

Exit 0 on success (or dry-run), non-zero on any error. Never writes private data.
"""
import argparse, datetime, hashlib, html.parser, json, os, re, sys, tempfile, urllib.request, urllib.error

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CATALOG = os.path.normpath(os.path.join(ROOT, "library/catalog.json"))
LIBJSON = os.path.normpath(os.path.join(ROOT, "pwa/library.json"))
LOGFILE = os.path.normpath(os.path.join(ROOT, "retrieval/captures.log"))
UA = "Mozilla/5.0 (X11; Linux x86_64) DRL-capture/1.0 (offline-first; contact: repo owner)"


class _TextExtract(html.parser.HTMLParser):
    """Minimal HTML->plain-text extractor so we can sanity-check a text layer exists."""
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        t = data.strip()
        if t:
            self.parts.append(t)
    def text(self):
        return " ".join(self.parts)


def classify(content: bytes, url: str, declared: str) -> str:
    """Pick store format by content-type / magic bytes."""
    if content[:4] == b"%PDF":
        return "pdf"
    if "application/pdf" in declared or url.lower().endswith(".pdf"):
        return "pdf"
    return "md" if declared == "" or "html" in declared or "text/" in declared else "bin"


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "artifact"


def fetch(url: str) -> tuple:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        ct = r.headers.get("Content-Type", "")
        final = r.geturl()
    if not data:
        raise RuntimeError(f"empty response from {url}")
    return data, ct, final


def text_layer_ok(content: bytes) -> bool:
    try:
        p = _TextExtract(); p.feed(content[:2_000_000].decode("utf-8", "ignore"))
        return len(p.text()) > 40
    except Exception:
        return False


def load_json(path):
    with open(path) as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--name", required=True, help="registry name for this source")
    ap.add_argument("--category", required=True, help="e.g. WATER, MED, LEARN")
    ap.add_argument("--part", default="Reference", help="Reference | Template")
    ap.add_argument("--license", required=True)
    ap.add_argument("--authority", help="publishing organisation (optional)")
    ap.add_argument("--priority", default="T1", help="T1|T2|T3")
    ap.add_argument("--out", help="target path (default: library/reference/<CAT>/<slug>.{fmt})")
    ap.add_argument("--dry-run", action="store_true", help="fetch+plan but don't write/register")
    ap.add_argument("--log", action="store_true", help="append a line to retrieval/captures.log")
    args = ap.parse_args()

    today = datetime.date.today().isoformat()
    data, ctype, final = fetch(args.url)
    fmt = classify(data, args.url, ctype)

    if fmt == "pdf":
        out = args.out or os.path.join(ROOT, "library", "reference", args.category, f"{slugify(args.name)}.pdf")
    else:
        if not text_layer_ok(data):
            print(f"FAIL: no usable text layer (possibly JS-only or binary) — refuse to store", file=sys.stderr)
            sys.exit(1)
        fmt = "md"
        out = args.out or os.path.join(ROOT, "library", "reference", args.category, f"{slugify(args.name)}.md")

    sha = hashlib.sha256(data).hexdigest()
    out = os.path.normpath(out)
    rel = os.path.relpath(out, ROOT)
    if not rel.startswith("library/"):
        print(f"FAIL: target must be under library/, got {rel}", file=sys.stderr); sys.exit(1)

    print(f"fmt     : {fmt}")
    print(f"final URL: {final}")
    print(f"bytes   : {len(data)}")
    print(f"sha256  : {sha}")
    print(f"target  : {rel}")

    if args.dry_run:
        print("dry-run: not writing or registering"); return 0

    if fmt == "md":
        # wrap as self-contained markdown with the required frontmatter
        title = re.sub(r"[-]+", " ", args.name).strip().title()
        fm = (f"---\ntitle: {title}\ncategory: {args.category}\npart: {args.part}\n"
              f"source: {args.name}\nlicense: {args.license}\ndate: {today}\n"
              f"verified: {today}\npriority: {args.priority}\n---\n\n"
              f"# {title}\n\n> Source: {final}\n> Authority: {args.authority or '—'}\n"
              f"> Captured: {today} (sha256 {sha})\n\n")
        body = ""
        try:
            p = _TextExtract(); p.feed(data.decode("utf-8", "ignore"))
            body = "\n\n".join(f"- {line}" for line in p.text().split(" ") if line)
        except Exception:
            pass
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(fm + body)
    else:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "wb") as f:
            f.write(data)

    # register in BOTH catalogs (same-commit index rule)
    entry = {
        "path": rel, "category": args.category, "part": args.part,
        "title": re.sub(r"[-]+", " ", args.name).strip().title(),
        "source": args.name, "license": args.license, "priority": args.priority,
        "date": today, "sha256": sha,
    }
    for cf in (CATALOG, LIBJSON):
        d = load_json(cf)
        d["artifacts"].append(entry)
        d["generated"] = today
        with open(cf, "w") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
            f.write("\n")
        d2 = load_json(cf)
        if not any(a["path"] == rel for a in d2["artifacts"]):
            print(f"FAIL: register verify failed for {os.path.basename(cf)}", file=sys.stderr)
            sys.exit(1)

    if args.log:
        with open(LOGFILE, "a") as f:
            f.write(f"{today}\t{sha}\t{rel}\t{args.category}\t{args.priority}\t{args.name}\t{final}\n")

    print(f"OK: captured + registered {rel} (sha256 {sha[:16]}…)")
    return 0


if __name__ == "__main__":
    sys.exit(main())