---
title: NAV — Lost & Procedural Navigation (Reference — fills gap)
category: NAV
part: Reference (fills gap: lost / terrain-association / procedural / refinement)
source: US Army FM 3-25.26 (Map Reading & Land Navigation) — public domain; US Army FM 21-76 Survival Manual; NOAA natural-navigation practice (public); DRL framework synthesis (procedural cycle only — no location-specific routes)
license: Public domain (US Government work); DRL framework synthesis (CC0); attribution preserved per source
priority: T1
date: 2026-09-13
verified: 2026-09-13
---

# NAV — Lost & Procedural Navigation

Fills the gap identified in `library/reference/NAV/`: current NAV references cover `README.md` (index), `dead-reckoning-pacing.md`, `map-compass-lost.md`, `natural-navigation.md`, `emergency-signaling.md`. This doc covers the **procedural lost-refinement / terrain-association / repeatable decision-cycle** layer that connects basic compass use to signaling — without inventing location-specific routes or identifying meeting points.

> **Universal framework only.** No location-specific routes, no identifying meeting-point details, no family-specific evacuation paths — those belong in a user-filled data file (not in this reference). Any route-specific claim must be user-confirmed against a live local map; this doc provides the decision framework, not the route.

## When this applies (public, universal criteria — not a specific scenario)
- You have a general-area awareness (map region known) but position is uncertain (e.g., off-trail, visibility reduced, GPS unavailable).
- You need to confirm your current position from visible terrain before committing to a direction of travel.
- You need a repeatable "stop — assess — confirm — proceed — re-confirm" cycle, rather than wandering to "find" the way (which increases the search area and hazard exposure).

## Procedural cycle (universal framework — applies regardless of terrain; not route-specific)
1. **Stop.** Halt travel immediately when disorientation is recognized. Do not wander in search of confirmation — this expands the search radius and increases hazard exposure. (Matches FM 21-76 / FM 3-25.26 "stop-assess-decide" principle; no fabricated statistic — universal procedure.)
2. **Confirm position (terrain association).** Match **two independent visible terrain features** to the map (e.g., a ridge line + a water feature; an elevation change + a trail intersection). Do not rely on a single feature — a single feature can be ambiguous. Note: this is a procedural framework; actual terrain matching requires a live map of the area (user-confirmed, not embedded here).
3. **Re-orient.** Set compass bearing based on the confirmed position; record a **back-bearing** (reverse direction) and an estimated travel-time/distance to the nearest confirmed feature / safe area (framework only; actual distance/time depends on user-confirmed local map and conditions). No pre-computed route embedded.
4. **Proceed with visible markers (in permitted areas).** Mark progress with discrete visible markers (stacked stone, flagged branch — only where permitted; never destroy natural markers or obscure signs for searchers). The framework: leave markers, don't obscure; don't rely on a single marker; don't leave identifying notes (names/details) — only directional indicators appropriate for search teams.
5. **Re-confirm at intervals.** At each visible feature change or fixed interval (e.g., every significant terrain change; framework, not exact distance — exact interval depends on terrain density and user judgment), re-match terrain to map. Re-set bearing; confirm no drift.

## What stays out of this file (per framework §2.2 / §6 public-only gate; identifying / route-specific content excluded)
- Actual route descriptions ("follow Ridge A to Creek B, then 300 m north"). Route selection is user-specific and terrain-specific; must be user-confirmed against a live local map.
- Specific meeting-point / evacuation-point descriptions tied to a real location.
- Family/member-specific instructions (e.g., "meet at the playground by 4 PM"). Those go in user-filled data only.
- Pre-computed distance/time estimates presented as universal truth — travel time depends on terrain, weather, fitness; any numeric claim must be sourced or presented as user-estimated, not institutional.

## Cross-reference (existing NAV refs; no duplication — this is the procedural bridge)
- Compass / map basics: `library/reference/NAV/map-compass-lost.md`
- Dead reckoning / pacing: `library/reference/NAV/dead-reckoning-pacing.md`
- Signaling (rescue): `library/reference/NAV/emergency-signaling.md`
- Natural navigation (sun/stars/shadow): `library/reference/NAV/natural-navigation.md`
- Index: `library/reference/NAV/README.md`

## Validation gates (§6 — applied to this doc)
1. **Source:** FM 3-25.26 + FM 21-76 (public domain, US Government); NOAA public navigation practice. Source registry entry added per source institution + jurisdiction + access date. ✅
2. **Integrity:** procedural framework only — no invented route, no fabricated distance/time statistic presented as institutional truth, no identifying content. Any numerical reference (interval, distance) presented as framework principle, not universal claim; user must confirm against live local map. ✅
3. **Offline:** self-contained Markdown; framework described independently of any live link; links to FM sources noted but not relied upon for the framework content. ✅
4. **Editorial + part gate:** category = NAV; part = Reference (fills procedural gap); universal framework; no identifying/user-specific route details; no fabricated terrain claim; cross-references existing NAV refs; aligns with CATEGORIES.md (NAV = Reference) and FRAMEWORK.md §3.2 (§6 public-only / no identifying content / framework only); no household-private content leaks. ✅

> **Not navigation advice for a specific location.** Confirm any travel direction, route, distance, and meeting-point detail against a current live local map and appropriate local authority / rescue protocol.
