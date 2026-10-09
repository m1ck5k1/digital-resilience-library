#!/usr/bin/env python3
"""refresh.py — DRL T1 retrieval cadence + weeding/retirement rule.

FRAMEWORK §7 cadence, made real: re-fetch every ACTIVE source in sources-registry.md
(T1 refreshed, T2/T3 frozen by default), fingerprint the fetched content (sha256),
compare against the last-known fingerprint, and emit a refresh report that tells the
librarian which docs are unchanged (fine), changed (needs re-verify), or unreachable
(needs attention/retirement).

Policies encoded here (the weeding rule):
- T1 sources are refreshed; T2/T3 are skipped unless --all.
- A source whose content hash changed vs. last good fetch => CHANGED (re-verify).
- A source that fails to fetch AND previously failed => DEAD twice => RETIRE (remove/
  re-source or move to HOLD). One transient failure => UNREACHABLE (recheck next cycle).
- Bot-blocked live sites (403) are retried via Wayback Machine CDX; if no snapshot is
  reachable, the source is UNREACHABLE, not retired (may be a network/UA issue).
- Non-http registry rows (in-repo templates/indexes) are skipped.

This tool NEVER edits library/reference docs or the catalog. It writes only:
  retrieval/source-state.json  — per-source fingerprint ledger (idempotent)
  retrieval/refresh-report.md  — human + agent readable findings
and bumps `last-checked` on ACTIVE rows in sources-registry.md.

Exit code: 0 = ok (may have findings), 2 = runtime error. Findings are NOT failures.

Usage: python3 tools/refresh.py [--all] [--dry-run] [--max N]
"""
import argparse, datetime, hashlib, json, os, re, sys, urllib.request, urllib.error

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REG = os.path.normpath(os.path.join(ROOT, "sources-registry.md"))
STATE = os.path.normpath(os.path.join(ROOT, "retrieval/source-state.json"))
REPORT = os.path.normpath(os.path.join(ROOT, "retrieval/refresh-report.md"))
UA = "Mozilla/5.0 (X11; Linux x86_64) DRL-refresh/1.0 (offline-first library maintenance)"
TIMEOUT = 45
MAX_BYTES = 8_000_000  # fingerprint full content but cap absurd downloads

CDX = "https://web.archive.org/cdx/search/cdx?url={u}&output=json&limit=1&filter=statuscode:200&filter=mimetype:text/html"


def fetch(url: str) -> tuple:
    """Return (status:int|None, final_url:str, sha256:str|None)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            data = r.read(MAX_BYTES)
            return r.status, r.geturl(), hashlib.sha256(data).hexdigest()
    except urllib.error.HTTPError as e:
        return e.code, url, None
    except Exception:
        return None, url, None


def wayback_sha(url: str) -> tuple:
    """Try Wayback CDX for a bot-blocked live site; return (final_url, sha256|None)."""
    try:
        req = urllib.request.Request(CDX.format(u=url), headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            rows = json.loads(r.read().decode("utf-8", "ignore"))
        if len(rows) < 2:
            return None, None
        snap = "https://web.archive.org/web/" + rows[1][1] + "/" + url
        st, fin, sha = fetch(snap)
        return (fin if st == 200 else None), sha
    except Exception:
        return None, None


def parse_registry(path: str) -> list:
    rows = []
    for line in open(path):
        if not line.startswith("|") or "| url |" in line or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 10:
            continue
        name, url, category, part, lic, authority, fmt, prio, checked, status = cells[:10]
        if not url.startswith("http"):
            continue  # in-repo entries (templates/indexes) are not fetched
        rows.append(dict(name=name, url=url, category=category, part=part, fmt=fmt,
                         prio=prio, checked=checked, status=status, line=line))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="refresh T2/T3 too (default: T1 only)")
    ap.add_argument("--dry-run", action="store_true", help="fetch + report, write nothing")
    ap.add_argument("--max", type=int, default=0, help="cap sources fetched (0=all)")
    args = ap.parse_args()

    rows = parse_registry(REG)
    active = [r for r in rows if r["status"] == "ACTIVE"]
    todo = active if args.all else [r for r in active if r["prio"] == "T1"]
    if args.max:
        todo = todo[: args.max]

    state = {}
    if os.path.exists(STATE):
        state = json.load(open(STATE))
    today = datetime.date.today().isoformat()
    findings = {"CHANGED": [], "RETIRE": [], "DEAD": [], "UNREACHABLE": [], "OK": [], "NEW": []}

    for i, r in enumerate(todo, 1):
        key = r["name"]
        prev = state.get(key)
        st, fin, sha = fetch(r["url"])
        via_wb = False
        if st == 403 or st is None:
            wb_fin, wb_sha = wayback_sha(r["url"])
            if wb_fin and wb_sha:
                st, fin, sha, via_wb = 200, wb_fin, wb_sha, True
        rec = dict(name=r["name"], url=r["url"], category=r["category"], prio=r["prio"],
                   last_checked=today, live_status=st, via_wayback=via_wb,
                   source_sha256=sha, final_url=fin)
        if not prev:
            findings["NEW"].append(rec); rec["verdict"] = "NEW"
        elif sha is None or st != 200:
            if prev.get("live_status") in (None, 404, 403, 500, 503) or prev.get("verdict") == "UNREACHABLE":
                rec["verdict"] = "RETIRE" if prev.get("verdict") == "RETIRE" else "DEAD"
                findings["DEAD"].append(rec)
                rec["verdict"] = "RETIRE"
                findings["RETIRE"].append(rec)
            else:
                rec["verdict"] = "UNREACHABLE"
                findings["UNREACHABLE"].append(rec)
        elif prev.get("source_sha256") != sha:
            rec["verdict"] = "CHANGED"; findings["CHANGED"].append(rec)
        else:
            rec["verdict"] = "OK"; findings["OK"].append(rec)
        state[key] = rec
        print(f"  [{i}/{len(todo)}] {r['prio']:3s} {r['category']:8s} "
              f"{rec['verdict']:11s} {r['name'][:55]}")

    # ---- report ----
    lines = [f"# DRL refresh report — {today}", "",
             f"Sources checked: {len(todo)} (T1 only unless --all) "
             f"| OK: {len(findings['OK'])} | CHANGED: {len(findings['CHANGED'])} "
             f"| NEW: {len(findings['NEW'])} | DEAD/RETIRE: {len(findings['RETIRE'])} "
             f"| UNREACHABLE: {len(findings['UNREACHABLE'])}", ""]
    for label in ("CHANGED", "RETIRE", "DEAD", "UNREACHABLE", "NEW"):
        if findings[label]:
            lines.append(f"## {label} ({len(findings[label])})")
            for r in findings[label]:
                lines.append(f"- **{r['name']}** [{r['category']} {r['prio']}] "
                             f"live={r['live_status']} sha={r['source_sha256'][:12] if r['source_sha256'] else 'n/a'} "
                             f"<{r['url']}>")
            lines.append("")
    if not args.dry_run:
        json.dump(state, open(STATE, "w"), indent=2, ensure_ascii=False)
        open(STATE, "a").write("\n")
        with open(REPORT, "w") as f:
            f.write("\n".join(lines) + "\n")
        # bump last-checked on ACTIVE fetched rows
        src = open(REG).read()
        for r in todo:
            src = src.replace(r["line"].rstrip("\n"),
                              r["line"].rstrip("\n").replace("| " + r["checked"] + " |",
                                                             "| " + today + " |", 1), 1)
        open(REG, "w").write(src)
        print(f"\nWROTE {STATE} + {REPORT} + updated last-checked in {os.path.basename(REG)}")
    else:
        print("\nDRY-RUN: no files written")
    return 0


if __name__ == "__main__":
    sys.exit(main())