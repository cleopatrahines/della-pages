# Implementation Notes

## Snapshot Metadata

- Capture time: 2026-07-14 16:27:22 +08:00 / 2026-07-14 08:27:22Z.
- Product source: official Della Shopify public product JSON at each approved PDP handle.
- Claim source: current official Della coupon page and installer page.
- Manual source: official PDF links exposed by Della PDP HTML.
- Browser fallback: Chrome CDP was unavailable because the system Node.js 22 prerequisite was missing; official direct reads and Shopify JSON were used instead.

## Product Snapshot

All eight products were available at capture time. Prices below are current snapshots, not permanent promises.

| System Type | Product | Preview Price | Live range | Varies | Available variants | Image check |
| --- | --- | ---: | ---: | --- | ---: | --- |
| Ceiling Cassette | DELLA 12,000 BTU 22 SEER2 Ceiling Cassette Ductless Mini Split AC - Up to 550 Sq.Ft. | From $1,394.96 | $1,394.96-$1,634.96 | Yes | 5/6 | Approved CDN image matches featured image |
| Ceiling Cassette | DELLA 18,000 BTU 20.5 SEER2 Ceiling Cassette Ductless Mini Split AC - Up to 1000 Sq.Ft. | From $1,784.96 | $1,784.96-$2,084.96 | Yes | 6/6 | Approved CDN image matches featured image |
| Ceiling Cassette | DELLA 18000 BTU Dual Zone Ceiling Cassette Mini Split AC (9K + 12K) - Up to 950 Sq.Ft. | $2,769.96 | $2,769.96 | No | 1/1 | Approved CDN image matches featured image |
| Ceiling Cassette | DELLA 27000 BTU Tri-Zone Ceiling Cassette Mini Split AC (9K + 12K + 12K) - Up to 1500 Sq.Ft. | $3,879.96 | $3,879.96 | No | 1/1 | Approved CDN image matches featured image |
| Concealed Ducted | DELLA 11000 BTU 19 SEER2 Concealed Ducted Mini Split Air Conditioner | From $1,144.96 | $1,144.96-$1,384.96 | Yes | 5/6 | Approved CDN image matches featured image |
| Concealed Ducted | DELLA 22000 BTU 19 SEER2 Concealed Ducted Mini Split Air Conditioner | From $2,119.96 | $2,119.96-$2,489.96 | Yes | 6/6 | Approved CDN image matches featured image |
| Concealed Ducted | DELLA 27000 BTU Dual Zone Concealed Ducted Mini Split Heat Pump AC (9.5K + 17K) | $2,939.96 | $2,939.96 | No | 1/1 | Approved CDN image matches featured image |
| Concealed Ducted | DELLA 34000 BTU Tri-Zone Concealed Ducted Mini Split Heat Pump AC (9.5K + 11K + 17K) | $4,179.96 | $4,179.96 | No | 1/1 | Approved CDN image matches featured image |

Notes:

- Do not use compare-at prices; the captured product JSON reports no approved compare-at price for this module.
- The live tri-zone cassette title omits spaces around `+`; this is a non-material punctuation difference. Keep the user-approved PRD title unless the user requests exact live-title mirroring.
- Preview implementation must use the `From` prefix for all four variable-price products.
- Production must use Shopify `price_varies` and money formatting rather than these literals.
- Reverify all prices and availability during final QA.

## Official Manual Evidence

### Usable Manuals

1. Single-zone Ceiling Cassette family:
   - `https://dellahome.com/cdn/shop/files/Della_048-CC_series_manual.pdf?v=4425906318345005421`
   - 84 pages.
   - Relevant evidence: pages 18-20 for accessible maintenance location, ceiling structure/opening/clearance, line-set route, drain route, and electrical route; pages 31 and 71 for return grille/filter access.

2. Single-zone Concealed Ducted family:
   - `https://dellahome.com/cdn/shop/files/DC_Series_user_manual.pdf?v=9671945254900585407`
   - 88 pages.
   - Relevant evidence: pages 14-22 for indoor-unit space, maintenance access, air return position/filter, supply and return duct paths, line-set/drain/electrical route, and drain connection; page 75 for filter maintenance.

3. Multi-zone family covering Cassette and Concealed Ducted indoor units:
   - `https://dellahome.com/cdn/shop/files/Della_048-TLP_MODU_series_manual.pdf?v=1939818704050222471`
   - 140 pages.
   - Cassette evidence: pages 45-65; specifically pages 50-51 for ceiling opening/clearance and line-set/drain/electrical planning.
   - Concealed Ducted evidence: pages 67-90; specifically pages 73-79 for return filter, supply/return duct paths, drain route, and service relationships.

### PDP Link Caveats

- The multi-zone cassette product-specific `1D3 Non-Ducted Indoor Units` PDF resolves to an AHRI certificate, not an installation manual.
- The dual-zone concealed-ducted product-specific `1D3 DUCT INDOOR UNIT` link returned HTML instead of a valid PDF at capture time.
- The tri-zone concealed-ducted product-specific `1D4 Ducted Indoor Units` PDF resolves to an AHRI certificate, not an installation manual.
- The 140-page common multi-zone family manual remains the usable first-party source and explicitly includes both indoor-unit types.

### Diagram Decision

The approved conceptual relationships are supported at family level:

- Ceiling Cassette: ceiling opening, available clearance, drain route, line-set route, service/filter access.
- Concealed Ducted: indoor-unit space, supply duct route, return-air path, drain route, service/filter access.

Do not copy exact dimensions, port positions, route lengths, construction steps, or equipment cutaways. A named Della product/HVAC reviewer must still approve the new page diagrams before publication.

## Premium Della Services Verification

Official source checked:

- `https://dellahome.com/pages/coupon-code`

Exact labels present at capture time:

- `Free & Fast Shipping`
- `Pay in 6 Months, 0% APR`
- `24×7 Live Chat Support`
- `Lifetime Coverage (Mini Splits)`

Use these short labels only. Do not expand financing eligibility, lifetime coverage, parts, compressor, labor, or duration details on this page. Reverify immediately before publication.

## Installer Route

- URL: `https://dellahome.com/pages/find-a-installer`
- Result at capture time: HTTP 200 with the same effective URL.
- Approved CTA: `Find a Della HVAC Installer`.

## Localized Assets

### Fonts

| File | SHA-256 |
| --- | --- |
| `assets/fonts/Poppins-400.woff2` | `CDEDB1729ACAC414ED01744A11DA7BADB86ADF13108E7BD3FA161B9323F7FE54` |
| `assets/fonts/Poppins-600.woff2` | `DAE40CA7B35FE7501BDA2E4140A6860B1DB47330BE5D3C8AB6971FD83A70E9A5` |
| `assets/fonts/Spectral-Regular.woff2` | `4F0438786FAAACDB6B752DC24FA7BD864F7D414AFD9818F3793CE8940BFAA21C` |
| `assets/fonts/Spectral-PageFly-Medium.woff2` | `AEE9EBCEBFCB9A773D48D0646F22AE69294E7A9669420311965A47AB5EB75B65` |
| `assets/fonts/Spectral-Bold.woff2` | `1CB11A74AE37B6A14020151339FD805F54F3B4E0ED6C50A7DB27EADAC33250FA` |

The hashes match the approved 2-Zone and Single-Zone reference assets.

### Service Icons

| File | Source role | SHA-256 |
| --- | --- | --- |
| `assets/images/services/free-fast-shipping.png` | Shipping truck | `7CE1F85284209DCC7AF13478B28634969396472E81080AC366A7481D8925026A` |
| `assets/images/services/financing-0-apr.png` | Financing card | `6741523BCA44DDD987934DBB690577F7052322640A8D8BF4F2EF87D8DA20A387` |
| `assets/images/services/live-chat-support.png` | Chat support | `C796384F964D590ACD9163B9B101E367B71A4D3E6ED2819E10CA3375808740F0` |
| `assets/images/services/lifetime-coverage.png` | Service wrench | `19488B40909E0CDDCE9D3304629A80AA6DC568999E8DBB071E9A57E1AB03872B` |

The four files were visually inspected and match the official icons in the approved local reference section.

Original official CDN sources from the approved reference:

- Shipping: `https://cdn.shopify.com/s/files/1/0785/7763/1520/files/80x80px-40_488310fc-d38a-4d43-bcc2-b1b5e44d2fa4.png?v=1764578865`
- Financing: `https://cdn.shopify.com/s/files/1/0785/7763/1520/files/20250609-092813.png?v=1749432513&width=2048`
- Live chat: `https://cdn.shopify.com/s/files/1/0785/7763/1520/files/20250922-160254_998da76a-d533-49ca-a79b-0ce8b4a70261.png?v=1765275088&width=2048`
- Lifetime coverage: `https://cdn.shopify.com/s/files/1/0785/7763/1520/files/80x80px-45_b280ec24-a703-42bb-b37e-aa83a9a6c424.png?v=1765275087&width=2048`

## Asset Map And Gaps

| Page use | Status | Decision |
| --- | --- | --- |
| Product cards | Ready | Use exact approved Della CDN URLs |
| Fonts | Ready | Source archive under `assets/fonts/`; flat runtime copies use `assets/della-*.woff2` |
| Premium Della Services icons | Ready | Source archive under `assets/images/services/`; flat runtime copies use `assets/della-service-*.png` |
| Quick Answer product visuals | Ready in principle | Use approved product imagery; final crop decided in Step 3 |
| Installation diagrams | Source relationships ready | Draw as editable conceptual SVG/HTML later; HVAC review still required |
| Hero desktop comparison | Approved approach | Compose from official product imagery and CSS; no generated technical equipment |
| Hero mobile comparison | Approved approach | Responsive version of the same official-product composition |
| Open-Concept Living Area | Ready | Reused as `assets/della-project-open-concept.webp` |
| Finished Basement | Ready | Reused as `assets/della-project-finished-basement.webp` |
| New Construction | Temporary neutral placeholder | Replace with approved non-technical scene-only image before visual acceptance |
| Multi-Room Renovation | Temporary neutral placeholder | Replace with approved non-technical scene-only image before visual acceptance; wall-mount imagery prohibited |

The prior Cassette vs Wall Mount Hero files are not usable because they show the wrong comparison. Mockups cannot be sliced into production assets.

Asset path approved by the user on 2026-07-14. The accepted three-part mockup remains unchanged and is not sliced into runtime assets.

## Step 2 Shared Foundation Record

- CSS namespace: `.della-compare`.
- JavaScript root: `[data-della-compare]`.
- Tab list contract: `[data-system-tabs]` with `role="tab"`, `data-tab-target`, and matching `role="tabpanel"` IDs.
- Progressive fallback: both panels remain available without JavaScript; tabs appear only after enhancement.
- Shopify lifecycle: reinitialize only newly loaded roots on `shopify:section:load`; `WeakSet` prevents duplicate bindings.
- No analytics event name is invented.
- Runtime CSS and JavaScript line counts: 320 and 90, respectively.
- Browser fixture checks passed at 1440, 1280, 768, 430, 390, and 350 pixels with no horizontal overflow or console warning/error.
- The temporary test fixture was not copied into the project.

Contrast record:

| Use | Colors | Ratio | Result |
| --- | --- | ---: | --- |
| Primary accessible blue button | `#FFFFFF` on `#416FCF` | 4.77:1 | WCAG AA normal text |
| Navy text/focus on white | `#0E1953` on `#FFFFFF` | 16.37:1 | WCAG AAA |
| Muted text on white | `#53617F` on `#FFFFFF` | 6.21:1 | WCAG AA |
| Decorative brand blue with white | `#FFFFFF` on `#5884E7` | 3.58:1 | Not used for normal-size button text |

## Step 3 Preview Sections 1–6 Record

- Preview file: `ceiling-cassette-vs-concealed-ducted-mini-split.html`.
- Implemented exactly six sections: Benefit Strip, Hero, Quick Answer, Project Fit, Key Differences, and Installation Requirements.
- Hero and comparison visuals use the approved official 18K Ceiling Cassette and 22K Concealed Ducted CDN images; type labels remain HTML text.
- Quick Answer uses the same official product images and routes directly to the two approved collections.
- Project Fit uses the approved Open-Concept and Finished-Basement local scenes. New Construction and Multi-Room Renovation remain neutral temporary panels and are not accepted as final visual assets.
- Installation uses simplified inline SVG planning relationships only. No exact dimension, construction sequence, port position, or internal cutaway is presented.
- Desktop comparison uses a semantic six-row table. Mobile presents the same six factors as readable cards while the table is visually hidden.
- Same-site links open in the same tab and carry stable `data-cta-location` and `data-cta-destination` attributes without invented analytics event names.
- Static checks found one H1, six sections, six table rows, no Header/Footer, and no missing local assets.
- Browser checks at 1440, 1280, 768, 430, and 390 found no horizontal overflow, broken image, warning, or error.
- Focused evidence and the remaining visual blocker are recorded in `design-qa.md` and `qa-evidence/`.

## Step 4 Preview Record — 2026-07-14 17:46 +08:00

- The static preview now contains all ten approved sections; Shopify Liquid and JSON remain unstarted.
- Product merchandising uses two ARIA tabs with four approved cards each. Ceiling Cassette is the default and only one panel is exposed at a time.
- Official Shopify product JSON was checked on 2026-07-14. All eight products were available at capture time.
- Captured preview prices: cassette 12K From $1,394.96; cassette 18K From $1,784.96; cassette dual $2,769.96; cassette tri $3,879.96; ducted 11K From $1,144.96; ducted 22K From $2,119.96; ducted dual $2,939.96; ducted tri $4,179.96.
- `From` is retained only on the four products whose Shopify variants contain multiple prices.
- The Premium Della Services strip uses the four approved local icons and exact approved labels. It does not expand policy wording.
- Six FAQ disclosures use native `details`/`summary`, start collapsed, and have no FAQPage schema.
- Focused browser checks covered both tab states, ArrowRight/Home/End keyboard behavior, FAQ click behavior, current link destinations, image state, console state, and 1440/1279/768/430/389/350 responsive layouts.
- No horizontal overflow, clipped product CTA, missing product/service image, warning, or error was found. The two known project-scene placeholders remain the only unresolved image assets.

## Step 5 Acceptance Record — 2026-07-14 18:04 +08:00

- Reverified all eight official Shopify product JSON endpoints. Every product remained available and every Preview Price, price range, `From` state, variant count, and featured-image identity matched the static preview.
- Reverified the current official Della coupon/service source. All four approved Premium Della Services labels remain present.
- Current-run browser evidence covers approximately 1440, 1280, 768, 430, 390, and 350 CSS pixels; two product states; six FAQ open/close cycles; focus visibility; link mapping; image dimensions/loading; console state; and horizontal overflow.
- Source verification confirms the reduced-motion rule and the no-JavaScript fallback: the tab control is hidden without enhancement and both Recommended Product Sets plus both Collection Paths remain available.
- The in-app automation surface did not dispatch native click activation for Enter/Space on HTML buttons or summaries. Arrow/Home/End behavior and focus visibility passed, while native `button`/`summary` semantics provide the intended Enter/Space behavior. Record a manual real-browser Enter/Space check before production acceptance.
- Step 5 result is `blocked`: two Project Fit scene cards still contain explicit pending-approval placeholders, and both Conceptual Planning Diagrams still need named Della product/HVAC approval.

## Draft FAQ Answers - Pending Approval

These answers are drafts only. Do not enable FAQPage JSON-LD until the user approves them.

1. **Is a ceiling cassette or concealed ducted mini split better for an open room?**
   A ceiling cassette is often the better starting point for one open room because its central ceiling position can distribute air in multiple directions. It still requires a suitable ceiling opening, drainage route, and service access. Concealed ducted can also work when the project has room for the hidden indoor unit and properly designed supply and return paths.

2. **Which option hides more of the indoor equipment?**
   Concealed ducted hides more of the indoor equipment because the air handler sits above a ceiling or inside another planned cavity. The supply and return grilles remain visible. A ceiling cassette is recessed, but its ceiling panel remains visible in the room.

3. **Can one concealed ducted unit serve more than one room?**
   It may serve more than one planned space through designed supply ducts and a suitable return-air path. That does not automatically provide independent temperature control in every room. A qualified HVAC professional should confirm room loads, airflow, return design, and the selected system configuration.

4. **Does a ceiling cassette require a drop ceiling?**
   Not necessarily. It does require a suitable ceiling opening and enough space above the finished ceiling for the indoor unit, drainage, refrigerant lines, and future service access. The ceiling structure and product-specific requirements must be reviewed before installation.

5. **Which option is easier to install in an existing home?**
   It depends on the available ceiling space and routing. A cassette may be the more direct option for an open room with suitable overhead access. Concealed ducted usually needs additional space for the indoor unit plus supply and return paths, which can make it better suited to a planned renovation.

6. **How should I size a ceiling cassette or concealed ducted mini split?**
   Start with a room-by-room load calculation rather than square footage alone. Insulation, windows, sun exposure, ceiling height, climate, occupancy, and the planned airflow path can all change the required capacity. Confirm the final equipment and system configuration with a qualified HVAC professional.

## Shopify And Measurement Gaps

- Active Della theme source or preview environment: not supplied.
- Theme product-object conventions and section lifecycle behavior: not yet testable.
- Header/Footer exact-once behavior: not yet testable.
- Existing analytics event naming: not supplied.
- Final Shopify URL and canonical behavior: not confirmed.
- Decision: use stable data attributes only until current theme and analytics conventions are inspected.

## Reference File Hashes

| Reference | SHA-256 |
| --- | --- |
| `2-zone-vs-3-zone-mini-split.html` | `CE92621F234BD4866303D5FB58FF64F94457311B021D77C1BA6E1E4AB83BC5FA` |
| `single-zone-vs-multi-zone-mini-split.html` | `708CB08BA0ADFE5F4CB89ED167DB3A857307B2CE93BF76FFFCF8F02A0E0516C5` |
| `della-memorial-day-design-system.md` | `119A039D551A05943574CA02FA6B8BE00E1B0CC9FF8A0C5E3C90A813620069D6` |
| `page.pf-ef33e2e6.json.txt` | `01210FC7B0C621E32F568F5ED38D7260DD91EF578FC0C74F475C722BFA8AE6A4` |
| `pf-ef33e2e6.liquid.txt` | `6A1F49ACC1A4F548846890F45371C5B97C8A32DFFCDB5D94BBA0E931AA6C7008` |
