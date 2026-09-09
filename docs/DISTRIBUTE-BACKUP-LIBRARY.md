---
title: Distribute & Back Up this Library (Artifact Longevity)
status: P-A · agent lane
date: 2026-09-09
---

# Distribute & Back Up this Library

> **P-A — why this exists.** This library may be a person's **only source of knowledge** for an
> extended period. That means the *artifact itself* has to outlive any single machine, this repo,
> or even GitHub. A library you can lose in one hard-drive failure is not a library — it's a
> hostage. The knowledge must be **carried, copied, printed, and stored** so it is reachable in a
> grid-down / offline / media-failure world.

The library is already **offline-first** (self-contained Markdown, a service-worker PWA). This
playbook is the operational "make your own copies" layer on top of it.

---

## 1. The principle: 3-2-1, applied to the library itself

The library's own filled-data rule is "2 copies on 2 media, one offline." The library artifact
deserves the same discipline:

- **3** total copies (live + backups),
- **2** different media types (e.g. a computer + a phone/USB/physical print),
- **1** copy offline (cold media not connected to the network).

> This is exactly the 3-2-1 rule the DRL teaches for household data — applied to the DRL itself,
> so a person never loses their only reference.

---

## 2. The four carry/copy channels

| Channel | Best for | How | Offline? |
|---------|----------|-----|----------|
| **1. Live PWA** | Everyday browse / search | `https://m1ck5k1.github.io/digital-resilience-library/pwa/`; install to home screen (PWA) so it works via the service worker | Needs first load online; then offline-capable |
| **2. Cloned repo (working copy)** | The raw Markdown + source, git history | `git clone https://github.com/m1ck5k1/digital-resilience-library` | Yes — the whole tree is local |
| **3. Static export / single-file bundle** | One portable artifact | Build a bundled HTML or file set from `library/` (see §4) | Yes |
| **4. Physical print / e-reader (Kindle)** | A durable, battery-openable copy | Render `library/` to PDF (see §4) and put on a reader / print select docs | Yes — most long-lived |

---

## 3. Where these copies should live

Keep the copies **geographically and medium-distributed**, so no single event takes them all:
- **Primary machine** — the cloned repo (your daily working copy).
- **External/cold media** — a USB drive / external disk (e.g. the machine's LUKS backup volume),
  refreshed after each content change.
- **A phone** — the installed PWA (works offline via service worker once loaded).
- **A stationary reader** — a Kindle or print of the `library/` reference PDFs, for a battery-durable,
  long-lived offline copy.

---

## 4. How to make a portable/print copy

The reader is static Markdown → many paths to a portable artifact. The highest-value, lowest-effort:

```bash
# 1. A single-file bundle of all reference docs (concatenated, frontmatter stripped)
#    — yields one self-contained .md you can read anywhere or feed to a renderer.
cd library
for f in reference/*/README.md reference/*/*.md; do echo; echo "===== $f ====="; done
# (preferred: use the PWA's own export / a small script — md -> PDF via pandoc/wkhtmltopdf)
```

- **PDF bundle:** `pandoc library/reference/*/*.md -o drl-reference.pdf` (or per-category PDFs).
  Markdown tables + code render well to PDF for the *ops/executable* playbooks (consistent with the
  household's own PDF preference for formatting fidelity).
- **e-reader:** per-category PDFs on a Kindle (consistent with the DRL household Kindle flow).
- **Just raw files:** copy the whole `library/` tree off.

> ⚠ PDFs/long docs are best built for the **reference/executable** content; the *searchable interactive*
> reader stays the PWA. The PWA is not the only copy — it is the *reader*, and it should never be
> the only place the knowledge exists.

---

## 5. The refresh / re-verify cadence

The artifact and its copies must not go stale:
- **After every content commit**: refresh the cold copies (rsync the repo → external disk; re-PDF
  if the reference set changed).
- **Use the `verified:` dates** (now in every doc's frontmatter, surfaced by `tools/validate.sh`)
  to spot which reference figures are oldest and most due a re-verify sweep.
- **Periodically** (seasonally / before storm season): re-load the PWA fresh (so the service
  worker caches the current content), re-sync copies, and confirm the offline/print copy is current.

---

## 6. Verification of your copies

- A copy is useless if it's corrupt. After making each copy:
  - `tools/validate.sh` passes (the tree is internally consistent),
  - `sha256sum` matches between the working copy and the external/offline copy's key files
    (defense-in-depth: verify, don't assume, mirroring the library's own checksum discipline),
  - the print/Kindle PDF opens and the figures are current (spot-check a `verified:` date).

---

## Status
P-A operational doc (artifact longevity). Agent lane. Pairs with:
`docs/LONG-TERM-EVOLUTION.md` (§4, P-E) and the household 3-2-1 rule in the FRAMEWORK.