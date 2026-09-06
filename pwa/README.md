# PWA — Digital Resilience Library reader/guide

> **Status:** PLACEHOLDER. The app is to be built in the **content phase**. This documents the
> intended role so the build has no ambiguity.

## Role
The PWA is a **reader + guide + exporter**. It never stores the truth.

1. **Reader** — browse/cache `library/reference/` offline (service worker; install-to-homescreen).
2. **Guide** — walk a household through each blank `library/templates/<cat>-plan` scaffold.
3. **Export** — produce a single portable **`household.json`** (canonical) + optional Markdown
   render. That file is the user's data, owned by them, backed up by them. **Not kept in the app
   as the source of truth; never uploaded anywhere.**

## Build constraints (from FRAMEWORK.md)
- No database — file-based (JSON canonical / Markdown render). No server, no sync.
- Filled data never leaves the user's device except as their downloaded file.

## Expected structure (to be fleshed out)
```
pwa/
  index.html
  manifest.json
  sw.js               ← offline cache of public reference + templates
  app.js              ← guide + fill + export logic
  assets/
```