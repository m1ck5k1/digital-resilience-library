---
title: FOOD — Sources & Safe-Hold Items (confirm list)
category: FOOD
part: Reference (confirm-first)
source: DRL assessment — items requiring verified sourcing before publication
license: DRL origin
date: 2026-09-06
verified: 2026-09-06
priority: T1
---

# FOOD — Sources & Safe-Hold Items

> Category: **FOOD** · Part: **Reference (confirm-first)**
> This is the **honest-hold** list: items that are load-bearing and must NOT be published with
> made-up numbers. They are routed here until verified against a **live authoritative source**.
> This is exactly the kind of item the **human 20% gate** reviews.

## Why this exists
The `preservation.md` and `storage.md` docs deliberately avoid quoting precise per-food
shelf-life tables and canning parameters because the live sources were not reachable during
this autonomous pass. Publishing a wrong pressure-canning time or a wrong "safe for X days"
claim into a **public medical-adjacent** library is how trust gets destroyed. So the safe
move is: state what is certain, and **hold the uncertain exact numbers in this list** for
verification.

## Items to verify (do NOT auto-publish until confirmed against a live source)

| # | Item | Why it matters | Where it should land when verified |
|---|------|----------------|------------------------------------|
| 1 | Pressure-canning **time + PSI per food** (low-acid: vegetables, meats, soups) | Wrong value = botulism risk | `preservation.md` (with source) |
| 2 | Water-bath canning times + **which foods require added acid** | Safety-critical acidity boundary | `preservation.md` |
| 3 | **Per-food dry-storage shelf-life table** (grains, canned goods, etc.) for rotation | Precise numbers the public will act on | `storage.md` |
| 4 | Meat drying/curing/jerky exact safe process + salt % | Improper curing is dangerous | `preservation.md` |
| 5 | Refrigerator held-cold time **without power** per food class | Outage guidance people rely on | `storage.md` / a SHELTER-ENERGY doc |
| 6 | Root-cellar temperature/humidity range with a source | Exact target numbers | `preservation.md` |

## How these get resolved
- Each item is fetched from a **Single authoritative source** (USDA/FSIS, extension, WHO,
  Red Cross) during a sourcing pass.
- It passes the **4 gates** (source/integrity/render/editorial) with the source recorded in
  `sources-registry.md`.
- It is then moved **out** of this list into the relevant reference doc.
- Until then: **do not invent the number.** If a doc needs it now, restate the principle and
  reference that the exact figure is pending verification.

## Validation gates
1. **Source:** this is a DRL-origin control doc (not third-party content). ✅
2. **Integrity:** accurate — it correctly records what is NOT yet verified. ✅
3. **Offline rendering:** self-contained Markdown. ✅
4. **Editorial:** correct category/part; it actively prevents unsafe fabricated content. ✅