---
title: Energy & Power — Batteries & Portable Power (Read & Understand Capacity)
category: ENERGY
part: Reference
source: US EIA — Energy Storage for Electricity Generation; Use of Electricity
license: US-gov public domain
date: 2026-09-08
verified: 2026-09-08
priority: T1
---
# Energy & Power — Batteries & Portable Power (Read & Understand Capacity)

> Category: **ENERGY** · Part: **Reference** (public)
> Primary source: **US EIA** (Energy Storage for Electricity Generation; Use of Electricity).
> Verified 2026-09-08.
> **Not a substitute for your device's label or manual.** Use the concepts here to **read your own
> device's ratings** rather than relying on a number from memory.

The single most useful skill for backup power is being able to **read and compare the two
ratings** on any battery / portable power station.

---

## 1. Two ratings: power capacity vs. energy capacity (EIA)

An energy-storage system (ESS) — including a portable power station or household battery — has
**two** distinct ratings:

- **Power capacity** — *"the maximum instantaneous amount of electric power that can be generated
  on a continuous basis"*, measured in **watts** (kW, MW, GW). This answers *"what can I run at
  once?"* (how many/fast appliances).
- **Energy capacity** — *"the total amount of energy that can be stored in or discharged from the
  storage system"*, measured in **watthours** (kWh, MWh, GWh). This answers *"how long can it
  run?"* (total stored energy).

> **The distinction matters.** A unit can have high power (runs a high-watt appliance) but low
> energy (runs it only briefly), or the reverse. Always check **both** numbers.

### How to size a load from labels
- Nameplate watts on an appliance (or amps × volts) tell you the **power** draw;
- The battery's **power capacity (W/kW)** must be ≥ the sum of what you run **simultaneously**;
- The battery's **energy capacity (kWh)** tells you total runtime ≈ kWh ÷ watts-with-a-load being
  drawn.

---

## 2. "Utility scale" vs "small scale" (context)

- *"Utility scale or large scale have at least 1 MW of net generation capacity; small scale have
  less than 1 MW, and many are owned by electricity end users that use solar photovoltaic systems
  to charge a battery."* — a household battery is **small scale**.

---

## 3. Storage is a SECONDARY source

*"ESSs are not primary electricity generation sources. They must use electricity supplied by
separate electricity generators or from an electric power grid to charge the storage system, which
makes ESSs secondary generation sources."*

So a battery doesn't create power on its own — it must be **charged** (grid, generator, or solar)
before it can provide power during an outage.

---

## 4. What the market uses (order by U.S. power capacity, end-2022)

Type of energy storage in commercial U.S. use, by power capacity: **pumped-storage hydroelectric →
batteries (electro-chemical) → solar-thermal with storage → compressed-air → flywheels.** For
household backup, **batteries** ("the majority of U.S. utility-scale BESSs use lithium-ion
batteries") are the relevant small-scale category.

---

## 5. Context: what electricity is used for at home (EIA)

- *"Total U.S. electricity consumption in 2025 was about 4.20 trillion kWh,"* ~14× the 1950 level.
- *"Heating and cooling (air conditioning) account for the largest annual uses of electricity in
  the residential sector."* → In an outage, **heating/cooling is usually the biggest load** to
  plan around.

---

## Not verified / how to handle numbers
- **No specific run-time or "what it can run" for any named product** is asserted — those are
  vendor-specific and change. **Read your own device's W and kWh ratings** and compute runtime as
  above; don't rely on a memorised or invented figure.

---

## Validation gates (this artifact)
1. **Source:** US EIA (T1, public domain). ✅
2. **Integrity:** the power-vs-energy capacity distinction and the secondary-source point are
   transcribed from the fetched text. ✅
3. **Offline rendering:** self-contained Markdown. ✅
4. **Editorial:** correct category (ENERGY) • Reference; no identifying data. ✅

*Attribution: US EIA — Energy Storage for Electricity Generation; Use of Electricity.*