# Digital Resilience Library (DRL)

A **public, vetted, offline-first** library of survival / resilience knowledge — medical,
water, food, energy, shelter, navigation — plus **blank household templates** that anyone can
fill in locally.

> **Status:** Framework + repo scaffolding. **No captured content yet.** Content begins after
> the framework is accepted (see `FRAMEWORK.md`).

## What this is

Three parts (see `FRAMEWORK.md`):

| Part | What | Public? |
|------|------|---------|
| **Reference** (`library/reference/`) | Universal, authoritative how-to knowledge | ✅ Public |
| **Templates** (`library/templates/`) | Blank household-plan scaffolds (SEC, LEGAL, KIDS…) — zero real data | ✅ Public |
| **Filled data** | A household's own answers — downloaded as a JSON file, never in this repo | ❌ Never here |

The **PWA** (`pwa/`) reads the reference library offline, guides template-filling, and exports
a user's filled data as a portable `household.json` file. It is a **reader + guide + exporter**,
never a store — your data lives only where you put it.

## Layout
```
FRAMEWORK.md            ← governing design & decisions
sources-registry.md     ← live source catalog (license + part per entry)
CATEGORIES.md           ← taxonomy + reference/template mapping
library/
  reference/            ← public reference docs
  templates/            ← public blank household templates
  catalog.json          ← integrity + license ledger (sha256)
pwa/                    ← reader/guide app
retrieval/RUNBOOK.md    ← retrieval + validation steps (placeholder)
tools/                  ← capture + validate scripts
```

## Governing principles (full detail in FRAMEWORK.md)
- Value over volume · human-sourced · offline-first · versioned+checksummed · **no household
  private data in this repo**.
- Filled household data = user-owned JSON, backed up 3-2-1 by the user.
- Public MED gated to T1 institutional sources + "not medical advice" disclaimer.

## License
See `LICENSE`. Content is redistributable; attribution preserved.