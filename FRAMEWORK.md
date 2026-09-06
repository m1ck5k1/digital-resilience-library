# Doomsday Preparedness — Digital Resilience Library (Framework)

> **Status:** FRAMEWORK (decision/scoping). **No data retrieval yet.**
> **Codename:** `digital-resilience-library` (DRL)
> **Repo (target):** `github.com/m1ck5k1/digital-resilience-library` — a **public** standalone repo,
> separate from the playbooks. Created at go-live.
> **Why a framework first:** before any web-scraping/scheduling happens, we must fix the
> *what*, *why*, *where*, and *how-validated*. Retrieval is the easy part; deciding what to
> keep and keeping it trustworthy is the real work. This playbook settles the design.

---

## 1. Objective

Build a **public, offline, human-readable** library of high-value survival/resilience
knowledge — how-tos, medical, scientific, farming, energy, repair, self-sufficiency — so
that if the internet is unavailable, degraded, or compromised, **any** household can still
find actionable answers. **Not** a hoard of everything; a **vetted, categorized, portable**
reference used like a field manual.

**Purpose: it is more useful shared than hoarded.** The curation, validation, and offline
packaging is the value-add. This is a public good.

### Golden rules (set now, hold later)
1. **Value over volume.** A few hundred vetted pages beat a million junk pages. Usable by a
   stressed, non-expert human, not a search-index dump.
2. **Anthrop-sourced, human-verifiable.** Prefer authoritative, citable primary sources
   (institutional orgs, field manuals, government standards, respected NGOs). No paywalls.
3. **Offline-first.** Every artifact is a self-contained file (HTML/PDF/Markdown) that opens
   without internet, bundled media, no external CDN deps.
4. **Versioned + integrity-checked.** Every capture is checksummed; nothing enters unvalidated.
5. **Portable + redundant.** The library is mirrored to cold/offline media (external disk,
   Kindle, offline reader). A library on a dead server is not a library.
6. **No household-private data in the repo.** The repo holds only reference knowledge + blank
   templates — never anyone's filled-in data. Sensitive data has **no home in this repo.**

---

## 2. The three-part model

This is the core architecture. There are **exactly three** distinct content types, and each
has a clear home.

### 2.1 Parts overview
| Part | What it is | Public? | Home |
|------|-----------|---------|------|
| **Reference** | Universal *how-to* knowledge — authoritative facts usable by anyone anywhere | **PUBLIC** | Public repo `library/reference/` (re-fetchable, low backup concern) |
| **Templates** | **Blank** scaffolds for household-specific plans. **Zero real data.** | **PUBLIC** | Public repo `library/templates/` (re-fetchable, low backup concern) |
| **Filled data** | A household's actual answers (shutoffs, contacts, inventory, routes) | **NEVER PUBLIC** | The user's **own device/local/cold storage** — never in any repo |

### 2.2 Why this dissolves the "private tier"
A "private tier" only existed to answer *"where do we hide sensitive data?"* The answer is:
**don't put it in the library at all.** The library holds reference knowledge (no household
data by definition) and blank templates (which become data only in the user's hands). So:
- **Zero leak surface** — no sensitive data in *any* repo, nothing to gitignore, nothing to
  protect, nothing to leak.
- **Fully public = fully shareable** — the public-good thesis survives with no compromise.
- **Templates are the better deliverable anyway** — a pre-filled plan for one house is
  useless to another; a fill-in scaffold is universal.

### 2.3 Assumption dropped (explicitly, per the "eradicate assumptions" goal)
- ~~Private tier as a storage location~~ — **Gone.** Everything is public.
- ~~Cold mirror stores "private rest content"~~ — Cold mirror now stores **your filled-in data**
  (your choice) + a full copy of the library. Repo carries zero private content.
- ~~"When in doubt, classify private"~~ — Becomes **"When a doc is household-specific, make
  it a template; keep actual data out of the repo."** Self-executing, because sensitive data
  has no home.

---

## 3. Categories

### 3.1 Category → part mapping
| ID | Category | Part | Notes |
|----|----------|------|-------|
| MED | Medical & First Aid | **Reference** (public protocols) + **Template** (personal-med/home-kit | Public MED = T1 institutional only + disclaimer |
| WATER | Water | **Reference** + optional Template (household supply log) |
| FOOD | Food & Farming | **Reference** + optional Template (seed/preserve plan) |
| ENERGY | Energy & Power | **Reference** + optional Template (off-grid plan) |
| SHELTER | Shelter & Repair | **Reference** + optional Template (house repair plan) |
| SAN | Sanitation & Hygiene | **Reference** |
| COMMS | Communications | **Reference** (generic ham/mesh) + **Template** (net config — private net details are data) |
| SEC | Security & Safety | **Reference** (generic) + **Template** (household plan — location/details are data) |
| NAV | Navigation & Survival | **Reference** |
| LEGAL | Legal & Documentation | **Template** (important-papers inventory — entries are data) |
| KIDS | Family & Kids | **Template** (contacts/schooling/emergency — entries are data) |
| LEARN | Skills & Trades | **Reference** |

Rule: a category that would otherwise carry household-identifying detail is delivered as a
**blank template** — the reference knowledge inside it is public, but any field a user fills
is data that lives only with them.

### 3.2 Explicitly excluded (anti-hoarding + legal-to-share guardrails)
- Redundant/news/opinion → only if the underlying fact isn't captured elsewhere.
- Paywalled / ToS-breaking / pirated → out. Sources must be **legal to store AND redistribute**
  (needed for the public tier). If it can't be legally shared, drop it.
- JS-heavy-interactive-only content with no storable form → out.
- Duplicates of content already held → out.

---

## 4. Storage & data model

### 4.1 Public repo layout
```
digital-resilience-library/          ← public repo (root = repo root)
  FRAMEWORK.md            ← this file (moved here at go-live as the governing design)
  sources-registry.md     ← live source catalog (Sec 5)
  CATEGORIES.md           ← taxonomy + reference/template mapping (Sec 3 expansion)
  retrieval/
    RUNBOOK.md            ← eventual retrieval/validation steps (placeholder)
  library/
    reference/            ← PUBLIC reference docs (MED/WHO.pdf, WATER, FOOD, ...)
    templates/            ← PUBLIC blank scaffolds (SEC-plan.md, LEGAL-inventory.md, ...)
    catalog.json          ← index: path, category, part, source, license, sha256, date
  pwa/                    ← the reader/guide app (built from library/reference + templates)
  tools/                  ← capture + validate scripts (built in retrieval phase)
```

### 4.2 The filled-data FILE (canonical: JSON; render: Markdown)
Templates are filled via the PWA into a **portable plain-text file** — **no database, no
server, no sync.**

| | JSON | Markdown |
|---|---|---|
| Role | **The canonical filled-data file** | A human-readable render |
| Why | PWA must **round-trip** — import a saved file to edit, re-export. Pure structured data → exact, lossless, no parsing ambiguity. One file, schema-defined, trivially backed up & diff'd. | Someone in a crisis must read the backup **without the app**; MD reads in any viewer and prints to paper. |
| Truth | **Single source of truth** | A **render, never a second truth** — regenerated from JSON |

**Flow:** PWA fills template → exports / downloads a single **`household.json`** (the backed-up
artifact). The PWA also offers **"print / export Markdown"** so the same data renders as
readable text for reading/paper.

**Why not SQLite:** browsers can't run it natively (needs WASM + shcema + migcsations + export
plumbing), it hies data inside a blob you then export anyway (extra step, extra failure point),
and it's structure for volume a household doesn't have. A flat file is easier, cleaner, safer,
and reuses the existing storage/backup discipline.

### 4.3 Backup of filled data (the only irreplaceable part)
A user's filled `household.json` is **sensitive + irreplaceable**. Applies 3-2-1:
- **at least 2 copies** on **2 media**, **1 offline**.
- Home: existing secrets/cold-mirror discipline. For m1ck5k1: `mycelium-seagate` 4T (LUKS)
  as primary + Kindle personal / local private dir as second.
- The repo NEVER holds filled data. Backup lives where the user already protects sensitive
  data.

---

## 5. Source strategy

### 5.1 Source catalog — living registry
`name | url | category | part | license/terms | authority | format | priority | last-checked | status`
The **license + part** columns are load-bearing: only redistributable material may be public.

### 5.2 Priority tiers
| Tier | Meaning | Capture priority |
|------|---------|------------------|
| T1 Canonical | Institutional field manuals, standards, versioned papers (WHO, CDC, FEMA, Red Cross, USDA ext, UK gov) | Capture fully, first. Highest trust. Mostly Reference. |
| T2 Curated | Well-regarded non-institutional how-tos, community guides | Capture selectively; cross-check. |
| T3 Ephemeral | Blogs/forums/social/AI-generated | Mostly OUT. |

### 5.3 Licensing & attribution
Prefer open/CC/PD. Record source + access date + license per artifact. Never strip
attribution. Public-tier artifacts MUST be redistributable.

---

## 6. Validation & trust (non-negotiable)

Every incoming artifact passes the 4 gates before entering `library/`:
1. **Source check** — registry / T1-T2? License (and redistributability for public) OK?
2. **Integrity** — sha256 matches fetch; no truncation/encoding loss.
3. **Rendering check** — opens offline; no broken links/CDN; text layer present (PDFs via
   `pdftotext`, not byte-scan).
4. **Editorial + part gate** — correct category AND part (Reference vs Template)? Facts
   cross-checked (T2/T3 vs T1)? **For public MED: T1-institutional-only + disclaimer.**
   **For all public: no identifying/personal data present (self-executing if it's a blank
   template or a reference doc with no data).**

Output: a `catalog.json` row + dated capture log (what, source, part, license, why, sha256).
No capture enters without a log line.

---

## 7. Retrieval + publication architecture — framework only, NOT scheduled yet

Skeleton; gated on this framework being accepted.
- **Toolset:** wget / `wget --mirror` / `httrack`; python+requests/bs4 for targeted pulls;
  `sha256sum`; all offline-safe.
- **Cadence:** initial bulk capture (T1 by category), then gentle scheduled refresh of T1 only
  (T2/T3 frozen) e.g. monthly.
- **PWA:** built from `library/reference/` + `library/templates/`. Acts as **reader (view the
  library, offline-cacheable via service worker) + guide + fill + export** of `household.json`.
  It **never stores the truth** — the file it exports is the artifact, owned by the user.
- **Cold mirror:** m1ck5k1's `mycelium-seagate` (LUKS) holds a full library copy + any personal
  filled data; Kindle personal collection for portable reads.
- **Publication:** GitHub Pages serves the public repo's `pwa/` + `library/reference/` +
  `library/templates/`. Private/filled data and personal cold mirrors stay off the public
  surface entirely.

> DO NOT commence retrieval/publication until categories + part mapping (Sec 3), source
> registry (Sec 5), and validation gates (Sec 6) are accepted. Design first; automate second.

---

## 8. Open questions to settle before building (for us)

**Resolved (LOCKED 2026-09-06):**
- No private tier; everything public. Templates for household-specific data.
- Three parts: Reference / Template / Filled-data (JSON canonical, MD render).
- No SQLite — file-based.
- Filled data backed up 3-2-1 via existing cold-storage/secrets discipline.
- Standalone public repo, separate from playbooks.
- Medical-public gate = T1-only + "not medical advice" disclaimer.

**Still open:**
1. Top 3 seed categories — propose **MED, WATER, FOOD** (life-critical). Confirm/override.
2. Target size/grade — ~300-500 reference artifacts / ~1-2 GB ceiling?
3. Languages — English-only, or also ES/other?
4. Final repo name + privacy of the standalone repo (public per Sec 7; confirm at go-live).

---

## 9. Change log
| Date | Change | Status |
|------|--------|--------|
| 2026-09-05 | Created framework (decision/scoping). | Framework — PENDING |
| 2026-09-05 | Public/Private tier model introduced. | Superseded |
| 2026-09-05 | **Standalone-repo decision** + medical-public gate resolved. | DECIDED |
| 2026-09-06 | **Re-architected:** private tier REMOVED → three-part model (Reference / Template / Filled-data-as-file). JSON canonical + Markdown render. No SQLite. Filled data backed up 3-2-1 via existing cold storage. | LOCKED |