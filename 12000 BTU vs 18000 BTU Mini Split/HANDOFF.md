# HANDOFF - 12000 BTU vs 18000 BTU Mini Split

Project path: `C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split`

## Current Files

- `PRD.md`
- `DESIGN.md`
- `PLAN.md`
- `implementation-notes.md`
- `HANDOFF.md`
- `NEXT_CODEX_PROMPT.md`
- `12000-btu-vs-18000-btu-mini-split.html`
- `12k vs. 18k Design Drafts.png`
- `12k.webp`
- `18k.webp`
- `assets/`

## Current Objective

Build and refine a Della topical decision landing page for `12000 BTU vs 18000 BTU Mini Split`, serving SEO research traffic and ads traffic.

Primary visitor decision: help shoppers decide whether to start with the 12000 BTU collection or the 18000 BTU collection. The page should not immediately force a SKU choice.

## Source Priority

Use this priority if anything conflicts:

1. User's latest explicit instruction in the active conversation.
2. `HANDOFF.md` and `NEXT_CODEX_PROMPT.md` latest notes.
3. `PRD.md`.
4. `DESIGN.md`.
5. `PLAN.md`.
6. Approved design draft image.
7. Existing Della reference pages and Della/PageFly design-system files.

Important: some latest user changes override older PRD/PLAN details. Do not blindly restore the old comparison table or old hero card treatment from earlier docs.

## Latest Approved Strategy

- Page type: Della topical decision landing page.
- Audience: US Della users, natural American English.
- Positioning balance: about 70% expert sizing judgment + 30% ecommerce guide, friendly and grounded.
- Routing: collection-first, PDP-second.
- Hero and decision CTAs route to collections:
  - `https://dellahome.com/collections/12000-btu-mini-split`
  - `https://dellahome.com/collections/18000-btu-mini-split`
- Product cards remain locked to the 8 approved PDPs only; do not auto-fill or replace from collections.
- Product card CTA: `View Product`.
- Della same-site collection/PDP links open in the same tab, no `target="_blank"`.
- No calculator, no inputs, no sliders.
- No canonical for now.
- No FAQ schema for now unless the user asks.
- Do not add sale/coupon/countdown language.
- Conservative sizing language only: use `common reference`, `worth checking`, `may`, `depends`, and installer confirmation language. Do not imply guaranteed coverage or guaranteed savings.

## Current Page Structure

Current HTML section order after merging the duplicate quick-decision modules:

1. `hero`
2. `choose-section` (now also carries the quick 12K vs 18K comparison task)
3. `factors-section` with `id="sizing-factors"`
4. `right-size-section`
5. `products-section`
6. `scenarios-section`
7. `services-section`
8. `faq-section`
9. `bottom-cta`
10. `mobile-sticky`

The former standalone `compare-section` / `12K vs 18K at a glance` module was removed because it duplicated the choose cards.
## Latest Implementation Notes

### Hero

- H1: `12000 BTU vs 18000 BTU Mini Split: When to Size Up`.
- H1 eyebrow/label above title was removed.
- Hero uses real local product-style images:
  - `12k.webp`
  - `18k.webp`
- Hero visual should not use fake AI product imagery.
- The hero product images should blend into the banner, without heavy card chrome around them.
- `12K` and `18K` small navy labels are retained above the images and should not cover the images.
- 12K and 18K image boxes were aligned: top, bottom, and height match on desktop.
- Hero card text under the product images was removed.
- Hero CTAs only:
  - `Shop 12000 BTU Mini Splits`
  - `Shop 18000 BTU Mini Splits`

### Choose Section

- Section title: `Choose the path that fits the room`.
- Section pill labels were removed globally; do not restore pills like `Quick direction`.
- This is now the only quick 12K/18K routing module; do not re-add a separate `12K vs 18K at a glance` section unless the user asks.
- Intro copy: `Use this as the quick 12K vs 18K comparison first. If the room feels borderline, the sizing factors below explain what can move the decision.`
- Two choice cards use left blue inline SVG house icons and right-side content.
- Each card has 5 decision bullets and a collection CTA.
- CTA styling should match the hero button feel.
- 18000/light-blue button hover/focus should turn background to `#0E1953`.

### Sizing Factors / What Can Move The Decision

- Current section title: `What can move the decision?`.
- This section uses compact decision cards.
- Desktop target: 6 cards in one row.
- Each card has:
  - blue inline SVG icon
  - compact title
  - one-sentence role/scene-aware explanation
  - existing `.tag` tendency label at the bottom
- Current card explanations:
  - Room Size: `If the room already feels spacious, 12K may have less margin on peak days.` / `May push toward 18K`
  - Insulation: `A tighter room helps the system hold comfort instead of fighting leaks.` / `May support 12K`
  - Sun Exposure: `Afternoon sun can turn a normal room into a hotter, harder-working space.` / `May push toward 18K`
  - Ceiling Height: `Tall rooms ask the system to condition more air than the floor area suggests.` / `May push toward 18K`
  - Open Layout: `When air spills into halls, kitchens, or dining areas, the load stops being one-room simple.` / `May push toward 18K`
  - Heat Load: `Cooking, tools, people, and garage heat can push the room beyond a simple sq. ft. estimate.` / `Needs installer review`
- Do not delete `Needs installer review`.
- Do not change tags to orange/green warning badges.
### Compare Section

- Removed by latest user direction and merged into `choose-section`.
- Do not restore the old `<table>`, mobile stacked table, compare-section buttons, or the two-card `12K vs 18K at a glance` module.

### Bigger Is Not Always Better

- Keep the section short and visual.
- Do not imply 18K is bad. Frame risks as `Oversized system risk`.
- Title/copy should sit above/right-sized comparison content without premature desktop wrapping.

### Products

- Product set is locked to 8 PDPs, 4 for 12K and 4 for 18K.
- Product cards show prices captured from live PDPs at implementation time.
- If prices are being refreshed and any specified PDP cannot be reached or parsed, stop and report missing items.
- Do not hide sold-out products and do not replace SKUs. Keep `View Product` CTA.
- Product image containers use `var(--blue-surface)` and product images use `mix-blend-mode: multiply` to reduce the visible white image background.

### Scenarios

- Keep 4 scenario cards only:
  - Bedroom or home office
  - Small living room
  - Garage or sunroom
  - Open living and dining area
- Each scenario card uses a real/lifestyle image from local assets or closest Della-owned source.

### Services

- User explicitly required Premium Della Services to be copied from the single-zone reference page.
- Do not change this section unless the user asks.

### FAQ

- Current FAQ has 5 high-value purchase-before questions.
- FAQ visual/interaction style follows the `single-zone-vs-multi-zone-mini-split.html` reference FAQ section, while keeping this page's existing font system.
- FAQ uses divider-line `details/summary` rows, navy default question text, brand-blue hover/open question text, and rotating arrow icon.
- User rejected adding more FAQs for now.
- Current Q4 is `Is bigger always safer when choosing between 12K and 18K?`, replacing the old faster-cooling question.
- Do not add FAQ schema unless asked.
### Bottom CTA

- Two collection path cards only.
- Short card positioning copy is allowed.
- No extra long note under cards.

### Mobile Sticky CTA

- Mobile-only sticky bottom CTA is approved.
- Desktop should not show sticky CTA.
- Buttons:
  - `Shop 12K`
  - `Shop 18K`
- Keep height around 56-64px and page bottom padding so it does not cover the bottom CTA.

## Current QA Status

Most recent checks after merging `choose-section` and the standalone `compare-section`:

- Static source check:
  - sections: 9
  - choice cards: 2
  - compare sections: 0
  - factor cards: 6
  - product cards: 8
  - scenario cards: 4
  - FAQ items: 5
  - no `compare-section`, no `glance-` CSS/HTML residue, no `12K vs 18K at a glance` heading
- Browser QA using local server and installed Chrome:
  - 1280px, 430px, and 390px all had no horizontal overflow.
  - `choose-section` and `factors-section` touch cleanly after the removed section.
  - FAQ click opened the first item at all checked widths.
- Previous banner image QA remains valid:
  - hero images use `12k-hero-transparent.webp` and `18k-hero-transparent.webp`.
  - both transparent images have alpha channels and aligned render boxes.

Recommended next QA before Shopify paste-in:

- Quick visual pass in the actual Shopify/PageFly paste context if available.
- Re-verify static product prices before publication because prices are snapshots.

## Known Risks / Notes

- Product prices are static snapshots. Re-verify before Shopify paste-in or final publication.
- The latest compare-section change overrides older PRD/PLAN wording that described a 6-row table.
- The latest factor-card design adds inline SVG icons directly in HTML; keep them inline, not external files.
- Some docs may still reference earlier structure; user asked not to rewrite PRD during visual iterations unless needed.
- No commit/push is approved.

## Next Action

If continuing, do only user-requested visual/content refinements or a Shopify paste-context check. Do not broaden scope, restore the old comparison table, add FAQ schema, or change the locked product set unless the user explicitly asks.


