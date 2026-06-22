# Next Codex Prompt - Della 12000 BTU vs 18000 BTU Mini Split

You are continuing work on a Della topical decision landing page.

Project path:
`C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split`

Primary file:
`C:\Users\18041\Desktop\della-pages\12000 BTU vs 18000 BTU Mini Split\12000-btu-vs-18000-btu-mini-split.html`

Before editing, read:

1. `HANDOFF.md`
2. `PRD.md`
3. `DESIGN.md`
4. `PLAN.md`
5. `implementation-notes.md`

Use `della-page-builder` for Della-specific rules. Use the user's latest instruction as the highest source of truth.

Important current state:

- The old full comparison table has been replaced. Do not restore it.
- `compare-section` should be `12K vs 18K at a glance`: two compact summary cards, no buttons, no table, no SKU/price/SEER/product image.
- `factors-section` should be compact decision cards: desktop 6 cards in one row, each with blue inline SVG icon, compact title/copy, and existing `.tag` at the bottom.
- Hero uses local `12k.webp` and `18k.webp`; keep product images aligned and blended into the banner. Do not add card borders/backgrounds around them unless user asks.
- Section-label pill tags were removed. Do not restore labels like `Quick direction`.
- Hero and choose-section collection CTAs stay. Compare-section has no CTA buttons.
- Product set is locked to the approved 8 PDPs. Do not auto-fill or replace products from collections.
- Use same-tab links for Della collection/PDP links.
- No calculator, no canonical, no FAQ schema, no extra FAQ unless user asks.
- Conservative sizing language only. Do not guarantee coverage, savings, or performance.

Current approved section order:

1. hero
2. choose-section
3. factors-section
4. compare-section
5. right-size-section
6. products-section
7. scenarios-section
8. services-section
9. faq-section
10. bottom-cta
11. mobile-sticky

Before reporting completion, browser-check at least:

- 1440px desktop
- 1280px laptop
- 430px mobile
- 390px mobile

Validation points:

- No horizontal overflow.
- Factor cards: 6 icons, 6 cards, desktop 6 columns, mobile 2 or 1 columns depending width.
- Compare section: 2 cards, no `<table>`, no compare buttons.
- Hero 12K/18K image top/bottom/height alignment remains good on desktop.
- Mobile sticky CTA appears only on mobile and does not cover bottom CTA.
- Product sections, services, FAQ, and bottom CTA remain intact unless user explicitly asks to change them.

Do not commit, push, create branch, or change long-term config unless the user explicitly approves.
