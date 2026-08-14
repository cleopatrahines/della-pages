# Ductless Mini Split vs Central Air — Handoff

Project path: `C:\Users\18041\Desktop\della-pages\Ductless Mini Split vs Central Air`  
Implementation status: HTML implementation complete; local browser QA passed  
Approved design: `Design.png`

## Current files

- `PRD.md`
- `GEMINI_DESIGN_PROMPT.md`
- `Design.png`
- `DESIGN.md`
- `PLAN.md`
- `ductless-mini-split-vs-central-air.html`
- `sources.md`
- `qa-report.json`
- `assets/fonts/`
- `assets/products/`

## Latest approved strategy

- Hero → Project Gateway → Conditional Shopping → Verify → **Premium Della Services (owner-added 2026-08-13)** → FAQ → Contextual CTA.
- Gateway is the sole selector: Replace, Add, Supplement.
- Organic state is neutral; `?path=` may preselect without auto-scroll.
- No Benefit Strip, Quick Answer, duplicate tabs, or extra editorial modules; Services module explicitly owner-approved.
- Ductless is room/use-case-led; Central is capacity-led; Supplement has no product grid.
- All 8 product cards use uniform navy `View Product` (new tab); no cart code.
- FAQ trimmed to 4 questions (owner-approved; JSON-LD matches) in single-column reference style.

## Product runtime state captured 2026-08-13

- ~~Direct ATC: Vario 18K, Vario 28K Dual, Vario 35K Quad~~ — superseded by owner decision 2026-08-13: these three cards now use `View Product` (PDP, new tab); no cart code in the page.
- ~~Choose Options: Serena 12K and all four Central systems~~ — superseded 2026-08-13: **all eight product cards now use a uniform navy `View Product` button opening the PDP in a new tab**; no secondary links, no Choose Options, no cart runtime.
- Central fitting-area figures omitted because a consistent official field could not be verified.
- Production hydration now updates prices only (Ajax Product API on dellahome.com); there is no variant/ATC runtime anymore.

## Runtime behavior

- Static/local/GitHub: dated price snapshot, no real cart transaction.
- DELLA Shopify host: hydrate current product data; enable direct ATC only for one available Variant.
- Successful ATC navigates to same-tab Cart.
- Production canonical is not included in the standalone preview; use Liquid `canonical_url` after the Shopify Page handle exists.

## QA status

Passed local Chrome QA on 2026-08-13.

- Responsive layout checked at 1440, 1280, 1024, 768, 430, 390, and 360px with no horizontal overflow.
- Desktop Ductless and mobile Central active states were visually reviewed against `Design.png` and `DESIGN.md`.
- Neutral, Ductless, Central, and Supplement states passed.
- `?path=` preselection, query-parameter preservation, contextual final CTA, static-preview cart protection, and no-JS fallback passed.
- 8 product cards, 3 direct ATC actions, 5 Choose Options actions, 6 FAQs, and 6 FAQ schema entries passed.
- No page or console errors were found.

Production Shopify QA is still required after PageFly/theme integration, especially live price hydration, Variant resolution, `/cart/add.js`, Cart redirect, analytics, and canonical output.

## Integration-era rules (agreed 2026-08-14)

- **Ad-ops message-match rule**: `?path=` is a message-match mechanism, not blanket paid personalization. Only attach it to ads whose creative explicitly promises one path (e.g. "Replace Your Ducted HVAC System" → `?path=central`). Generic comparison ads must land neutral.
- **Dual source of truth**: Shopify (Liquid/Ajax) owns product facts — title, URL, image, price, availability, variants. The page owns merchandising config — role labels, path assignment, display priority, fallback products. Never parse product titles to infer zone/room roles.
- **Measurement KPIs**: do not optimize path stability (a path change can be a successful correction). Track Qualified Action Rate (PDP/collection/installer/finder), Qualified Progression by final path, Correction Rate (diagnostic, not failure), and conversion by final path × traffic source.
- **Decay triggers**: price-hydration failure alert at integration; annual review of owner-supplied policy copy (shipping / 30-day / lifetime compressor); periodic link validity spot-check; set og:image to the absolute Shopify CDN URL when the page goes live.

## Git status

Commit/push not approved and not performed.
