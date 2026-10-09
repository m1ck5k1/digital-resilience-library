# Retrieval + Validation Runbook

> Status: ACTIVE. Capture half is implemented (`tools/capture.py`), test run
> end-to-end (Oct 09 2026) against the EIA Energy Storage source (fetched, hashed,
> registered, passed all gates in a scratch copy). The editorial half stays a human/lane
> gate — this runbook records that split.

Covers: capture tooling, the 4 validation gates, and the capture log.

## Toolset (implemented)
- `tools/capture.py` — stdlib-only capture: fetch + text-layer check + sha256 +
  store self-contained artifact under `library/reference/<CAT>/` + register in BOTH
  `library/catalog.json` and `pwa/library.json` (same-commit index rule) + optional
  capture-log line. No external deps (fits offline-first rule).
- `tools/validate.sh` — the 4 validation gates, run over everything that lands.
  CI runs this on every push/PR (required check `validate`).

## Usage
From repo root:
```
python3 tools/capture.py --url <URL> --name "<registry name>" --category <CAT> \
    --part Reference --license "<terms>" --authority "<org>" --priority T1 \
    [--out <path>] [--log] [--dry-run]
```
- `--dry-run` fetches + classifies + hashes + prints the planned target, writes nothing.
- Partial/captured artifacts are **scaffolds** — auto-extracted text, not hand-vetted
  content. See "Editorial gate" below before anyone commits a capture as public vetted
  content.

## The 4 validation gates (every artifact)
1. Source check — from `sources-registry.md` / authoritative T1-T2 source;; license OK.
2. Integrity — sha256 matches fetch;; no truncation/encoding loss.
3. Rendering check — opens offline;; no broken links/CDN;; text layer present
   (enforced in capture: refuses JS-only/binary-no-text-layer).
4. Editorial + part gate — correct category AND part;; facts cross-checked;; MED = T1
   institutional + "not medical advice" disclaimer;; no identifying data.

## Editorial gate (the human 20%)
`capture.py` fetches + stores, but it does NOT decide vetted-ness. A captured artifact
(ASCII text dump of a source` is **not yet public "reference knowledge"** — that status
requires the same assurances as any other artefactin: facts cross-checked, attribution,
no leak, MED disclaimer, readable manual prose. Treat a fresh capture as a **draft**:
turn it into proper `library/reference/<CAT>/<name>.md` prose (editing the auto-text wisely,
adding citable attribution + back-links), then validate, then commit with its catalog row
in the same commit.

## Capture log
`retrieval/captures.log` — tab-separated: `date sha256 rel-path category priority name
final-url`. Any artifact landed via the fetcher gets a line (optional `--log`).