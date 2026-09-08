---
title: ENERGY — Index
category: ENERGY
part: Reference (index)
source: DRL origin
license: CC0
date: 2026-09-07
---

# ENERGY — Index

> Category: **ENERGY** · Reference + one Template.

Third seeded category. Chain of priority: **water → food → energy**. Once hydration and
calories are secured, a household can keep itself functional through an outage — but only if
the power-safety fundamentals (above all, carbon monoxide) are handled correctly.

## Reference docs (public)
- [`backup-power-generators.md`](./backup-power-generators.md) — portable generators: the CO
  hazard, safe placement (outdoors, ≥20 ft), CO alarms, electrical/fuel safety, and what never
  to run indoors. Grounded in EPA / Ready.gov-FEMA / CPSC.
- [`batteries-portable-power.md`](./batteries-portable-power.md) — the **power-capacity vs
  energy-capacity (W vs kWh)** distinction and how to read your own device's ratings. EIA.
- [`solar-basics-backup.md`](./solar-basics-backup.md) — cell → module → array, DC→AC inverter,
  sun-facing; the universal how-it-works baseline. DOE.
- [`reducing-demand-outage.md`](./reducing-demand-outage.md) — surge protection, fridge/freezer
  food-safety (4-hr / 48-hr / 40 °F-2 hr), full-tank, lighting. Ready.gov.
- [`safe-fuel-chemical-handling.md`](./safe-fuel-chemical-handling.md) — household hazardous
  waste: no-food-containers, no-mixing, label/disposal rules. EPA.
- *(still not yet)* generator **sizing / run-time** and **fuel-storage numeric limits** — held at
  the review gate until verified against a current source.

## Household template (`library/templates/`)
- [`ENERGY-household-backup-plan.md`](../templates/ENERGY-household-backup-plan.md) — fill in YOUR
  backup-power source, run-time plan, CO-safety checklist, and load priorities. Fill locally;
  your answers never go in this repo.

## Place in the build order
WATER → FOOD → ENERGY → (SHELTER, SAN, NAV…) are the agreed seed order. ENERGY reference is
seeded here; a household **off-grid / generator plan template** can follow in a later pass.

## Status note on this seed
The ENERGY doc is deliberately **safety-first**: the life-critical fixed truths (CO kills;
never run a generator indoors/within 20 ft; CO alarms; cool-before-refuel). Exact
appliance-sizing and run-time numbers are **not** included because they could not be verified
against a reachable T1 source this pass — they are flagged for the human review gate rather
than guessed.