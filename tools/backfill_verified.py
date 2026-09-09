#!/usr/bin/env python3
"""Backfill `verified:` (as-of) date into library reference docs' frontmatter.

Idempotent: adds `verified: <date>` immediately after `date:` on any content
Reference doc (skips indexes and templates) if not already present. Uses the
existing `date:` value (the doc records it was verified that day).

Usage: python3 tools/backfill_verified.py [--dry-run]
"""
import re, glob, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "library")
DRY = "--dry-run" in sys.argv

def main():
    updated, skipped_index, need_date, already = 0, 0, 0, 0
    for md in glob.glob(f"{ROOT}/**/*.md", recursive=True):
        src = open(md).read()
        head = "\n".join(src.splitlines()[:25])
        if not head.startswith("---"):
            continue
        part = re.search(r'^part:\s*(\S.*)$', head, re.M)
        date = re.search(r'^date:\s*(\S+)\s*$', head, re.M)
        ver  = re.search(r'^verified:\s*\S', head, re.M)
        if not part:
            continue
        p = part.group(1).strip()
        if "index" in p.lower():
            skipped_index += 1; continue
        if "reference" not in p.lower():
            continue  # templates leave verified off (they're per-user)
        if ver:
            already += 1; continue
        if not date:
            need_date += 1; print(f"  ! no date, cannot set verified: {os.path.basename(md)}")
            continue
        d = date.group(1).strip()
        # insert `verified: <date>` on its OWN new line right after the `date:` line
        new = re.sub(r'^(date:\s*\S+)\s*$', r'\1\nverified: ' + d, src, count=1, flags=re.M)
        if new == src:
            need_date += 1; continue
        if not DRY:
            open(md, "w").write(new)
        updated += 1
        print(f"  + {os.path.basename(md)}  verified={d}")
    print(f"\n[{'DRY-RUN ' if DRY else ''}]backfilled={updated}  already={already}  "
          f"skipped-index={skipped_index}  need-date/err={need_date}")

if __name__ == "__main__":
    main()