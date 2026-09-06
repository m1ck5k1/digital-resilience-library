# Retrieval + Validation Runbook

> **Status:** PLACEHOLDER. To be filled during the content phase, once the framework is
> accepted. Covers: capture tooling, the 4 validation gates, and the capture log.

## Planned shape (from FRAMEWORK.md §7)
- **Toolset:** `wget --mirror` / `httrack`; python + requests/bs4; `sha256sum`; offline-safe.
- **Cadence:** initial bulk capture (T1 by category), then gentle scheduled refresh of **T1
  only** (T2/T3 frozen) on a slow cadence (e.g. monthly).

## 4 validation gates (every artifact)
1. Source check — registry / T1-T2? License + redistributability OK?
2. Integrity — sha256 matches fetch; no truncation/encoding loss.
3. Rendering check — opens offline; no broken links/CDN; text layer present.
4. Editorial + part gate — correct category and part; facts cross-checked; no identifying data.

## Capture log
Every capture appends to `catalog.json` (path, category, part, source, license, sha256, date)
plus a dated log line. No capture enters without a log line.