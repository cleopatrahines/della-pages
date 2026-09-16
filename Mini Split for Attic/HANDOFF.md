# Attic Page Handoff

Updated 2026-09-16.

## Current page

- Source: `../mini-split-for-attic.html` relative to this repository asset folder.
- Purpose: help buyers judge which installation types fit a finished attic, understand capacity, zoning and installation boundaries, then choose a type collection or a specific model.
- Flow: Hero (image + H1 + one-line intro, no CTA buttons) → five-anchor on-page nav → three-type comparison (tabs) → concealed attic cutaway (four hotspots) → four equal product cards → Premium Della Services → four FAQs → "Shop by Installation Type" collection CTA.
- Hero: no in-page buttons; the immediately following anchor nav provides the next entry points. Desktop min-height ~520px, mobile text area shrinks to content. Desktop banner is top-aligned (`object-position: 50% 0%`) so the DELLA indoor unit and a little headroom stay fully visible; the inaccurate `2400×900` attributes were corrected to the real `2800×1200`. Mobile keeps its own `One Finished Bedroom.webp` fully shown (`object-fit: contain`).
- Products: on mobile the card badge is `justify-self: start`, so it shrinks to its label width instead of spanning the full card (desktop behaviour unchanged).
- Nav: the band background matches the comparison section (`--gray-50`) so the two form one continuous band, and the five anchor pills are white (same treatment as the comparison tabs). Buttons are horizontally centered inside the content container on desktop; on mobile they stay left-aligned with accessible horizontal scroll (no clipped/unreachable first button).
- Comparison: three tabs (Wall-Mounted / Ceiling Cassette / Concealed Ducted). Each tab changes one luxury scene image, a short distinction, three key conditions, a native `details` for extra conditions, and one type-collection button. No per-option model or capacity recommendation remains. The type-collection button sits at the bottom-right of its card content edge (normal-flow flex, no absolute positioning) and uses the same navy default / white-on-navy hover / visible focus states as the product CTA (size, padding and typography unchanged). The `#find-setup` anchor still reaches the comparison heading area.
- Collection mapping (destination verified 2026-09-16):
  - Wall-Mounted → https://dellahome.com/collections/wall-mounted-mini-split
  - Ceiling Cassette → https://dellahome.com/collections/ceiling-cassette-mini-split
  - Concealed Ducted → https://dellahome.com/collections/concealed-ducted-mini-split
- Cutaway: DELLA outdoor-unit cutaway of a concealed ducted attic install, four linked hotspots (Indoor unit, Service access, Supply & return airflow, Outdoor route), a desktop "View larger" dialog that loads the original PNG only on first open, and a mobile "Open full-size image" link. Caption "Conceptual layout. Confirm model-specific clearances and installation requirements." is vertically centered with the "View larger" button (text left, button right, button not squeezed); narrow screens stack left-aligned.
- Products: four equal cards — Serena 12K, Ceiling Cassette 12K, Concealed Ducted 9.5K, Dual-Zone Concealed Ducted 17K with 9.5K + 9.5K indoor units. Desktop 2×2, mobile single column. Each card links to its own PDP; collection links are not used here. Product IDs, price variants, images and PDP paths are retained.
- Images: responsive WebP (`-600/-1080/-1536`) served from this repository folder; the original cutaway PNG is requested only for full-size viewing. Desktop uses the existing banner, mobile uses `One Finished Bedroom.webp`.
- FAQs: four questions with native details/summary, visible keyboard focus and a matching four-entry FAQPage JSON-LD.
- Premium Della Services: unchanged Bedroom transplant (centered Spectral heading, Poppins body, four cards, base64 icons, `/pages/contact` link). It loads `Poppins-400.woff2` and `Spectral-PageFly-Medium.woff2` from `Mini Split for Bedroom/assets/`.

## Decision-path revision (2026-09-16)

- Removed the Hero's two jump buttons and rebalanced Hero spacing (desktop ~520px); kept the five-anchor nav.
- Unbounded the short-heading area (`.section-header`) so section H2s use the content width and read on one line at 1440px; long FAQ/body copy keeps a readable measure, and the comparison title/scene share one 1080px baseline.
- Rewrote short headings/intros: Compare Attic Mini Split Types; Plan a Concealed Attic Installation; Mini Splits for Finished Attics; Attic Mini Split FAQs; Shop by Installation Type.
- Replaced each comparison option's product strip (thumbnail, MATCHED OPTION, model, BTU, PDP button) with a single type-collection button; the three scenes, conditions and `details` are kept.
- Replaced the bottom CTA's two jump-back buttons with three same-level collection entries (Wall-Mounted / Ceiling Cassette / Concealed Ducted).
- Reduced the FAQ from six to four decision questions and synced the JSON-LD to the same four:
  1. What size mini split does my attic need?
  2. Can the indoor and outdoor units both go in the attic?
  3. Do I need single-zone or multi-zone for my attic?
  4. What affects the total cost of an attic mini split?
- FAQ answers avoid unverified national pricing, efficiency claims or per-room promises; capacity points to a room-specific load calculation confirmed by the installer.
- Kept the previously fixed cutaway behaviour: deferred original PNG, mobile full-size link, short-viewport contain fit, centered dialog, Escape and focus return.
- Validation: 26/26 Playwright checks on the served page (1440/1024/768/390/320, single-line headings, per-tab collection destinations, four-card PDPs, four matching FAQs, dialog regression). Evidence: `C:/Users/18041/Documents/Playground/della-ui-review-20260911/attic-design-prototype-20260916/qa/repo-page-20260916b/`.
- Source SHA256 before this revision: `7CF3930561367F0A82DB9945DA2AEC2ED7FE5858686567D7477A216CA5DA0FD4` (backup: `mini-split-for-attic.before-decision-path-20260916.html`).

## Banner, nav & compare-button polish (2026-09-16)

- Scope: local visual-only adjustment of `mini-split-for-attic.html`; content, links and interactions retained.
- Banner: desktop hero image changed from `object-position: 50% 40%` (cropped the unit's top) to `50% 0%` (top-aligned) so the whole DELLA indoor unit plus a little headroom stay visible; image ratio and full-bleed cover retained, no image was stretched or regenerated. Corrected the `width`/`height` attributes from `2400×900` to the real `2800×1200`. Verified at 1920, 1440, 1280 and 1024px. Mobile `One Finished Bedroom.webp` display unchanged.
- Nav: `.anchor-nav ul` is centered (`justify-content: center`) on desktop, preserving order, size and 10px gap; the mobile query keeps `justify-content: flex-start` with horizontal scroll so the first button is never clipped.
- Comparison buttons: `.cmp-actions` is now `display: flex; justify-content: flex-end` (normal flow, no absolute positioning), so each type-collection button aligns to its card content right edge (32px inner padding); mobile keeps the full-width rule. Colour states now match the product CTA — default navy `#0E1953` background / white text / navy border, hover white background / navy text / navy border, and a `2px` navy `focus-visible` outline. Padding (13px 24px), 14px font, 48px min-height, 4px radius and 1px border are unchanged, so button size is identical.
- Removed two helper texts and their dead styles: the comparison cross-option caption "Illustrative interiors. Confirm layout and capacity with your installer." (`.cmp-caption`) and the cutaway kicker "How It Fits Together" (`.section-label`); also removed the now-dead `.bottom-cta .btn-navy:hover` rule. Option conditions, `details` and the four FAQs are kept.
- Dividers: removed the `1px` separator lines at the nav→comparison boundary (`.anchor-nav` `border-bottom`, `.compare-section` `border-top`), above the cutaway (`.cut-section` `border-top`) and above the products (`.products-section` `border-top`). The white↔light-gray background change now provides the separation. In-card separators (`.cmp-actions`, `.cmp-media`, FAQ rows) and the dialog bar are unchanged.
- Cutaway caption: `.cut-caption` uses `align-items: center` with the text taking the remaining space (`flex: 1 1 auto`) and the button `flex: 0 0 auto`, so the caption and "View larger" are vertically centered, text left / button right, and the button is not squeezed; narrow screens stack left-aligned and keep the "Open full-size image" link.
- Validation: 28/28 Playwright checks on the served page (banner machine visibility + correct attributes at 1920/1440/1280/1024, nav centering, button right-alignment, colour states, unchanged button metrics, removed texts, caption centering, collection links, dialog deferred PNG + Escape/focus, hotspots, tabs, four FAQs, no overflow at 1440/390, no 404/console errors). Evidence: `C:/Users/18041/Documents/Playground/della-ui-review-20260911/attic-design-prototype-20260916/qa/repo-page-20260916c/`.
- Source SHA256 after this revision: `EB2D0AED7165D09CCEFD1AAF61B4C71E22AC379810A744B160C2AC36C59FF8ED`. SHA256 before this revision: `856DDCFA72D27E49B063A8E74C5CF85062F79AC13CC403EE19793FF30D04684B`.

## Historical — visual upgrade (2026-09-15)

- Scope: local CSS/font-only refinement of `mini-split-for-attic.html`; the body markup, page order, facts, product IDs, price variants, images, PDP links, FAQ content/schema, canonical and metadata are retained.
- Typography: the page now loads the locally supplied Spectral 500/700 and Poppins 400/600 weights. H1, H2, comparison-card titles and product titles use Spectral; body copy, specs, buttons and helper text use Poppins.
- Cards/actions: comparison and product cards use coordinated 14px radii, calmer borders and content-driven spacing. Product actions remain flex-aligned without new fixed-height content bands; product CTA buttons use a navy/white hover treatment with visible focus outlines.
- Rhythm: section headers, installation checks, FAQ rows and the final CTA have clearer vertical spacing. The mobile Hero title and CTA stack were enlarged for stronger entry-point hierarchy while the existing mobile product cross-row behavior remains.
- Premium Della Services remains the approved Bedroom transplant and was not structurally redesigned in this round.
- Final source SHA256: `A3E0D4518BB40A9BFA885C0872F80FDE7DE579921A9C36505A554A7BA59DDEF9`. The pre-upgrade backup SHA256 is `9D3D82F7FEB43A144D6DBD192BF98CB92C274015E0B10524063BE83B30CD1772`.

Visual evidence folder: `C:/Users/18041/Documents/Playground/della-ui-review-20260911/attic-visual-upgrade-20260915/`.

- `before.html`: pre-upgrade source backup.
- `before-final-1440.png` / `before-final-390.png`: pre-upgrade full-page captures with lazy product images loaded.
- `after-1440.png` / `after-390.png`: final full-page captures.
- `before-compare-module-1440.png` / `after-compare-module-1440.png`: comparison module before/after viewport captures.
- `before-products-module-1440.png` / `after-products-module-1440.png`: product module before/after viewport captures.
- `qa-visual-upgrade.json`: focused technical QA result.

## Validation

- The prior service-module work copy had 14/14 focused checks passed for SHA256 `9D3D82F7FEB43A144D6DBD192BF98CB92C274015E0B10524063BE83B30CD1772`.
- The Bedroom reference and Attic service module have matching four-card DOM, text, base64 icon images and support link. Poppins and Spectral loaded from the referenced asset files.
- Nominal viewport widths: 1440, 1024 and 390px. The service module had no page or element overflow and all four service images loaded at each width. A 200% focused check at 390/1024px also passed; the reference behavior was retained without additional layout changes.
- Tab traversal reached the copied support link with keyboard-visible focus. Raw source fingerprints for Hero, compare, installation checks, products, FAQ and bottom CTA match the 296… source backup; raw FAQ schema text and all four product ID/variant pairs are unchanged. Desktop input source remained at SHA256 `296571FCD6BDD4B306EBE24197F04438FBE1329BC7CA5C9E873AF7B7FFA4F986`.

- Visual-upgrade QA: 22/22 focused checks passed. The run covered 1440, 1024, 768, 390 and 360px, plus 200% effective CSS widths of 195px and 497px; it verified font families/loading, image loading, no page/card overflow, body/schema/product-data preservation, real CDP mouse clicks for the primary CTA and product disclosure, and a real CDP Space-key FAQ expansion. The report distinguishes this targeted input run from a full end-user browser session.

Evidence folder: `C:/Users/18041/Documents/Playground/della-ui-review-20260911/attic-bedroom-services-20260915/`.

- `qa/focused-services.json`: focused browser checks, reference parity and viewport measurements.
- `QA_REPORT.md`: focused QA summary.
- `screenshots/` and `qa/`: normal and enlarged-text captures for the service module.
- `before.html`: backup of the 296… source before this service-module revision.
- `before-HANDOFF.md`: backup of the previous HANDOFF before this revision.
- `bedroom-service-reference.html` is preserved at `C:/Users/18041/Documents/Playground/bedroom-service-reference.html`.
- Formal reference URL: `https://cleopatrahines.github.io/della-pages/Mini%20Split%20for%20Bedroom/mini-split-for-bedroom.html`.

## Delivery boundary

The user authorized this local page optimization. Commit, push and production publishing require separate authorization.

Prices are a static snapshot. The page has no shared live-price integration; a bare PDP link does not explicitly select the stored price variant. Shopify theme integration, canonical/CDN deployment checks and analytics remain separate work.

Before restoring `before.html`, check for any subsequent changes to the repository file. The input SHA256 for the prior service-only revision is `296571FCD6BDD4B306EBE24197F04438FBE1329BC7CA5C9E873AF7B7FFA4F986`. The current visual-upgrade revision is stored locally and is not committed, pushed or published.
