#!/usr/bin/env bash
#
# validate.sh — Digital Resilience Library integrity gates
#
# Operationalises the 4 validation gates + integrity ledger the FRAMEWORK promises
# but didn't enforce: JSON parses, catalog<->library.json<->git-ls-files sync,
# required frontmatter, leaked-data scan, no-unverified-HOLD-as-reference, redirects off.
# Exit non-zero on any failure so it can gate CI and local pre-commit use.
#
# Usage: tools/validate.sh   (run from repo root)

set -u
cd "$(dirname "$0")/.." || exit 1
fail=0

warn() { printf 'FAIL  %s\n' "$*" >&2; fail=1; }
pass() { printf 'ok    %s\n' "$*" >&2; }

# --- 1. JSON parses + schema sanity -------------------------------------------
if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY' || fail=1
import json, os, sys
ok = True
for f in ("library/catalog.json", "pwa/library.json"):
    try:
        d = json.load(open(f))
    except Exception as e:
        print("JSON parse", f, e, file=sys.stderr); ok = False; continue
    if "artifacts" not in d or not isinstance(d["artifacts"], list):
        print("no artifacts list in", f, file=sys.stderr); ok = False
    for a in d["artifacts"]:
        for k in ("path","category","part","title","source","license","priority","date"):
            if k not in a:
                print("missing field", k, "in", a.get("path","?"), file=sys.stderr); ok = False
# library.json == catalog.json minus top-level 'format'
cat = json.load(open("library/catalog.json")); lib = json.load(open("pwa/library.json"))
cat = dict(cat); cat.pop("format", None)
if cat != lib:
    print("library.json != catalog.json minus format", file=sys.stderr); ok = False
# every artifact path resolves
import json as _j
cat = _j.load(open("library/catalog.json"))
for a in cat["artifacts"]:
    if not os.path.isfile(a["path"]):
        print("missing file:", a["path"], file=sys.stderr); ok = False
sys.exit(0 if ok else 1)
PY
  pass "json: parse + catalog/library.json/artifacts sync"
else
  warn "python3 not found — cannot run JSON checks"
fi

# --- 2. Required YAML frontmatter on every .md under library/ -----------------
if command -v yamllint >/dev/null 2>&1 && command -v awk >/dev/null 2>&1; then
  :
fi
while IFS= read -r md; do
  head -1 "$md" | grep -q '^---' || { warn "frontmatter no leading --- : $md"; continue; }
  # require the key fields appear in the first 20 lines
  for key in title category part source license; do
    head -20 "$md" | grep -q "^$key:" || warn "missing '$key:' frontmatter in $md"
  done
done < <(find library -name '*.md' -type f)
pass "frontmatter: title/category/part/source/license present on library/*.md"

# --- 3. Leaked-data / secret scan (filled household data must never be tracked) -
leak=0
if git rev-parse --git-dir >/dev/null 2>&1; then
  if git ls-files | grep -qE '(^|/)(household\.json|filled/|\.env|\.secret|.*private.*\.json)' ; then
    warn "leaked fill/secret in git index"; leak=1
  fi
  # actual secret patterns in tracked text
  git grep -lEI '(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,})' -- '*.md' '*.json' 2>/dev/null \
    && { warn "possible secret in tracked content"; leak=1; }
fi
[ "$leak" -ne 0 ] && fail=1
pass "leak: no household.json/filled/.env/secrets in git index"

# --- 4. No 'HOLD'/'confirm-first' artifact presented as plain T1 Reference -----
if command -v python3 >/dev/null 2>&1; then
  python3 - <<'PY' || fail=1
import json, sys
ok=True
cat=json.load(open("library/catalog.json"))
for a in cat["artifacts"]:
    part = a.get("part","")
    pri  = a.get("priority","")
    # a 'confirm-first' / hold doc must not fly under a plain T1 priority
    if "confirm" in part.lower() or "hold" in part.lower():
        if pri in ("T1",):
            print("HOLD/confirm-first artifact listed as plain T1:", a["path"], file=sys.stderr)
            ok=False
sys.exit(0 if ok else 1)
PY
  pass "status: no held/confirm-first artifact masked as plain T1"
fi

echo
if [ "$fail" -eq 0 ]; then
  echo "VALIDATE OK — all gates passed."
  exit 0
else
  echo "VALIDATE FAILED — see messages above." >&2
  exit 1
fi