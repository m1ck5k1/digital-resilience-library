---
title: Long-Term & Medium-Term Survival — DRL Evolution Brief
status: DESIGN BRIEF (draft-for-review)
date: 2026-09-09
---

# Long-Term & Medium-Term Survival — How the DRL Must Evolve

> **Design brief, not shipped content.** This is the thinking document for how the Digital
> Resilience Library should evolve, because it may become **a person's only source of knowledge**
> for an extended period. That is a serious responsibility. It reframes the library from
> "survive the first 72 hours" to "sustain a household across **medium** (weeks–months) and
> **long-term** (indefinite) disruption."

---

## 1. The three time-horizons (the core reframe)

The library currently optimises for the **acute** phase. Long-term and medium-term survival are
different problem spaces and are currently underserved.

| Horizon | Timeframe | The real problem | Current DRL coverage |
|---------|-----------|------------------|----------------------|
| **Acute** | Hours–days (≤72 h) | Stockpile, first aid, shelter, signal, evacuate | **Well covered** (kit, CPR, generator, shelter-in-place, storm) |
| **Medium** | ~3 weeks–6 months | **Sustainment**: extending water/food/energy, chronic care, staying healthy, maintaining tools, avoiding burnout | **Thin** — the most-neglected span |
| **Long-term** | Indefinite | **Closed-loop self-reliance**: growing/trapping/preserving food, seed-saving, indefinite water/energy, improvised care, community | **Absent** — the new responsibility |

> **Why medium-term is the neglected critical span:** most "bad" scenarios (supply-chain
> disruption, regional power/winter event, a slow-burning crisis) last weeks to months before
> either recovery or true collapse. It wants **sustainment** — not just stockpiling — which is
> exactly the learned, skills-heavy knowledge the library under-serves today.

---

## 2. The responsibility: "only source of knowledge"

If the library is a person's **only** reference for an extended period, several new hard
requirements emerge:

1. **Integrity over time.** A person may act on a stale or wrong number *years* later with no
   external check. Accuracy is life-critical. The library must actively resist **drift** — both
   our content becoming wrong as guidance changes, and a user relying on outdated guidance.
2. **The "not medical advice" caveat changes meaning.** At 72 h, "call a professional" is enough.
   At months alone, that answer stops being available. The library must eventually teach
   **improvising care without a professional** — the highest-liability content we could add, and
   therefore the most carefully gated.
3. **Skills, not just facts.** Long-term survival is about **developing and maintaining
   capability** (farming cycles, seed-saving, hand tools, preservation), which is a *practice*, not
   a lookup. This implies a learning/skills tier distinct from reference docs.
4. **The artifact itself must be resilient.** A person's only source must be **durable,
   self-contained, printable, and redundant across media** — not dependent on this repo, GitHub,
   or any one machine. The offline-first ethos must extend to: a printable/physical pathway and a
   clear "make your own copy" story.

---

## 3. Evolution principles (draft)

These should govern how the DRL grows toward medium/long-term:

- **Tier the library by time-horizon, not just by category.** Give every category an
  acute → medium → long-term spine so a reader can go from "first 72 h" to "sustain indefinitely"
  in one category.
- **Add a SUSTAIN / LONG-TERM lens to existing categories first** (water: catchment→storage→
  indefinite source; food: store→grow→preserve→seed-save; energy: battery→solar→wood/sustain).
  Don't spawn a dozen new categories; deepen the ones that map to survival needs.
- **Introduce a Learning/Skills tier** — a distinct part (Reference vs **Practice**) marking
  content that must be *learnt and practised*, not just read (seed-saving, canning, hand-tool
  craft, garden cycles). This is the highest-leverage shift for long-term.
- **Add the psychological + social survival layer** (now at the plan stage, human-gated): months
  of disruption is as much a mental/community survival problem as water. Long-neglected in
  preparedness.
- **Treat medium-term as its own first-class horizon**, not a footnote between acute and
  long-term — it is the most likely shape of a real crisis and the least prepared-for.

---

## 4. Integrity & longevity workstreams (what "stays trustworthy for years" needs)

1. **Provenance + "verified as of" on every doc** — we already log source dates; formalise it so
   each doc states when its figures were verified and that they may drift.
2. **Staleness handling** — a review/sweep process (re-fetch key T1 sources periodically) and a
   visible way to mark a doc "needs re-verification." `validate.sh` guards *structure*; it cannot
   guard *correctness over time* — that's a content-maintenance cadence.
3. **Extend `validate.sh`** to check for stale "verified"/date fields and surfaced
   hold/confirm-first items, not just structural sync.
4. **Longevity of the artifact** — a "distribute/print/back-up this library" playbook: how a
   person carries it (offline PWA, printable PDF, cold storage), so the knowledge outlives any
   single host.
5. **Traceability to source** — every number keeps its exact source URL (already the practice);
   make it hard-coded and audit-friendly.

---

## 5. Proposed evolution phases (draft, to sequence with you)

- **P-A (integrity/longevity):** extend `validate.sh` (staleness/last-verified surfacing),
  author a **Distribute & Back Up this Library** playbook, add "verified as of" to doc headers.
  *(agent lane)*
- **P-B (medium-term content):** add the sustainment layer — e.g. water *indefinite sourcing*,
  food *growing/preserving/seed-saving + garden calendar*, energy *sustain*, MED *chronic/months
  with no professional* (human-gated). *(part agent, part human)*
- **P-C (learning tier):** introduce the **Practice** part and seed it (canning, seed-saving,
  hand-tool craft, fire-by-friction with periodic re-practice markers). *(design decision →
  human)*
- **P-D (social/psychological):** draft the months-alone/stressed-group mental-health +
  community-knowledge layer (human-gated, high sensitivity). *(human)*
- **P-E (artifact longevity):** printable/bundle/Kindle path so the whole library can live off
  any one machine. *(agent lane)*

---

## 6. Explicitly deferred / not yet decided (the human's 20%)

- Whether to restructure categories by time-horizon or keep category + add horizon tags.
- Whether the "improvise care with no professional" MED tier is in-scope (highest liability).
- Whether the learning/Practice tier should change the catalog schema or just the docs.
- Whether print/bundle is in-scope (it affects PWA and repo layout).

---

## Status
This is a **design brief for review** — deliberately not pushed as library content. It frames
the medium and long-term responsibility, the integrity/longevity workstreams, and a draft
evolution path, and is held for agreement before building.