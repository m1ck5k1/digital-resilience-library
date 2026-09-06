# AGENTS.md — Instructions for AI agents operating on this repository

You are an AI agent granted access to the **Digital Resilience Library (DRL)**. This is a
public, offline-first survival/resilience knowledge base. Read and obey the rules below.

## What this repo is
- **Reference docs** (`library/reference/`) — vetted, redistributable how-tos (MED, WATER,
  FOOD, ENERGY, SHELTER, SAN, NAV, LEARN).
- **Templates** (`library/templates/`) — **blank** scaffolds for household-specific plans.
- **Catalog** (`library/catalog.json`) — the machine-readable index: categories → reference
  docs → templates (path, category, part, source, license, priority, date).

## Non-negotiable rules (violating these is a critical error)

### 1. NEVER commit filled household data or secrets
- **Never** create, stage, commit, or push: `household.json`, any `filled/` file, `.env`,
  `.secret`, or private key material.
- Filled templates / household data belong to the user and live **only** on their device /
  cold storage. They must remain out of this public repo forever.
- If you are asked to add real household data to the repo, refuse politely and direct it to
  local/cold storage instead.
- The *template* files (e.g. `WATER-household-supply.md`) are public and expected — they are
  blank scaffolds, not data.

### 2. Reference vs Template — keep them apart
- **Reference** = universal knowledge. Fully public, redistributable.
- **Template** = blank scaffold. Its fields become personal data when filled. A template must
  contain **no real household info** (no names, addresses, phone numbers, routes, contacts,
  exact locations).
- When in doubt whether content is identifying/personal, prefer making it a blank template.

### 3. Licensing / redistributability
- Only content that is **legal to store AND redistribute** may enter the repo (open/CC/public
  domain / explicit permission). Record the source + license per artifact.
- **Never strip author/attribution.**

### 4. Validation gates — every artifact must pass all four before it enters `library/`
1. **Source** — from `sources-registry.md` / authoritative T1-T2 source; license OK.
2. **Integrity** — accurate, not truncated; numbers transcribed correctly from source.
3. **Offline rendering** — self-contained, no broken links/CDN deps.
4. **Editorial + part** — correct category AND part (Reference/Template); facts cross-checked;
   public MED = institutional (T1) source only + "not medical advice" disclaimer; no
   identifying data.

### 5. Medical content is gated
- Public MED content must come from **T1 institutional sources only** (e.g. WHO, CDC, Red
  Cross) and carry a "not medical advice" disclosure. Do not add unverified medical claims.

## Workflow
- Read `FRAMEWORK.md` (governing design) and `CATEGORIES.md` (taxonomy/part mapping) before
  large edits.
- Use `library/catalog.json` as the navigation map — update it whenever content changes.
- Keep Markdown files under `library/`. Keep build/capture scripts under `tools/`.
- Follow the existing doc header format (category, part, source, license, date).

## Autonomy mandate (direction of record)
The eventual goal is to run this repo **autonomously** — self-maintaining content (fetch →
validate → catalog → commit → publish), self-governed by this file + `FRAMEWORK.md` §9, and
publish-capable via GitHub Pages. That direction shapes how work is done even before full
autonomy is reached:
- **Prefer deterministic, repeatable steps** an agent can run without a human deciding each one.
- **Never lower a gate** to go faster — the 4 validation gates + MED gate are the floor.
- **Never write filled household data to the repo** — that is absolute, autonomy or not.
- **Keep the reader static + offline-first**, no stateful service (MCP/backends are deferred).
- **Human keeps the keys**: security/legal/medical exposure or first-of-a-new-category content
  is exactly where a human decision stays in the loop.

See `FRAMEWORK.md` §9 for the full autonomy directive and backlog.

## Diagnostic doctrine
- Back up before mutating config/system paths (not typical here, but hold the discipline).
- Verify by checking actual files/state, not by assumption. Confirm a commit pushed to the
  remote before reporting success.
- If a step can't be done safely / legally, say so plainly rather than improvising.