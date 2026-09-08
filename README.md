# Digital Resilience Library

> Status: **public · vetted · offline-first.** WATER is seeded as the pilot category; the
> framework is accepted. More categories follow.

A **public, vetted, offline-first** library of the knowledge that keeps a household alive
when everything else drops — medical, water, food, energy, shelter, navigation — plus
**blank household-plan templates** that anyone can fill in for themselves.

> **What this library houses, stores, and tracks is *publicly available data only*:** vetted,
> citable reference knowledge and blank templates derived from public sources we can verify
> and legally redistribute. We collect, version, and track that public data — and we
> deliberately hold **no personal, household, or private data anywhere in this repo.** The
> one thing that is *your* data (a filled household plan) never enters here.

This is my work as **h3rm5k1**, shaped by Michael's guidance. We built it the way we build
everything: **more useful shared than hoarded.** The internet can fall away; reliable
knowledge shouldn't have to.

---

## The idea, plainly

A library that can't be read offline isn't resilience — it's a hostage. So everything here
is a **self-contained file** that opens with no connection, no app, no account.

And a library that holds *hub-specific* answers (your shutoff valve, your family's contacts)
is fragile and outright dangerous to share. So we only ever keep **two kinds of thing** here —
and both are **publicly available by design** (verified reference knowledge, or blank forms):

| Part | What it is | Public? |
|------|------------|---------|
| **Reference** (`library/reference/`) | Universal, citable how-to knowledge — same for every house | ✅ Yes — meant to be shared |
| **Templates** (`library/templates/`) | **Blank** scaffolds for household plans (water, security, legal, kids…) — zero real data | ✅ Yes — the *form*, not the answers |
| **Filled data** (yours) | A household's own answers, exported as one `household.json` file | ❌ Never here — stays with you |

The templates hold **your** structure; you fill in **your** facts, locally and on your own
devices. The repo never sees them.

---

## The bounded truth about backups

Your filled-in `household.json` is the **one irreplaceable thing** in this whole system — a
re-published reference doc can be re-fetched; your routes and contacts can't. So backup is
not an afterthought, it's be-built-in:

> **Export a file. Copy it 3-2-1 — at least two copies, on two kinds of media, one offline.**

That's discipline we already run here and it's the same for anyone who uses this library.

---

## What's here now

### WATER (seeded pilot — because a person is hours from dehydration, not days)
- `library/reference/WATER/treatment-disinfection.md` — boil / bleach / tablets / filters, with the **exact CDC dosing table**
- `library/reference/WATER/storage.md` — how much, containers, rotation, backup sources
- `library/reference/WATER/catchment-testing.md` — rainwater/emergency collection + the practical "is it safe?" method
- `library/templates/WATER-household-supply.md` — your water plan, blank
- `library/reference/WATER/README.md` — index

### Governing design
- `FRAMEWORK.md` — the decisions and the why (the three-part model, no private tier, JSON-canonical/Markdown-render)
- `AGENTS.md` — how AI agents should operate here (and the hard rule: never commit filled data)
- `llms.txt` — a fast machine-readable overview for AI / search
- `CATEGORIES.md` — taxonomy + the Reference/Template mapping
- `sources-registry.md` — every source, its license, and its part
- `library/catalog.json` — the machine-readable navigation index

---

## The other design choices, in brief

- **No database.** A household needs dozens of fields, not thousands of rows. Filled data is a
  portable **JSON** file (canonical, round-trippable); print/read as **Markdown**.
- **PWA is a reader + guide + exporter, never a store.** The app helps you fill and hands you
  a file — it doesn't hold the truth, because "it's in the app" is exactly how data gets lost.
- **Trust is the product.** Public MED is **gated to institutional sources only** (WHO, CDC,
  Red Cross) with a "not medical advice" disclosure. Anything not legal to redistribute stays out.
- **Safety by structure.** No private tier to defend, nothing to leak — because sensitive data
  simply has no home here.

---

## Contribute / use

Browse the hosted reader, or clone the repo and keep a copy on a device that can survive
an outage. Fork it, extend it, make it yours. The richer the shared knowledge, the more
households it can carry through a bad week.

> **Not medical advice.** Read, adapt, and where it matters, confirm against current local /
> professional guidance.

---

*Built and maintained as the **Digital Resilience Library** — a sibling of the personal and
team playbooks, living on its own so the public good and the private plans never tangle.*