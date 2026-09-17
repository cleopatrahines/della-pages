# Design — 2026-09-17 image and typography refinement

User-authorized design baseline. Codex supplies planning/art/review; OpenCode / DeepSeek implements. Authority: latest user request → PRD → LOCKED-COPY/products.json → DESIGN → PLAN → mockup pixels.

Current scoped refinements: LAYOUT-REFINEMENT.md and transparent image manifest. Overall layouts: `design/final-mockup-v6.png`, `design/portable-panel-v6.png`. Keep the current three independent scene assets. Exact sources/selectors are in REFERENCE-MAP-2026-09-17.md. The Portable close-up primarily locks three equal cards and their internal order; retain the page's 4px rectangular Tab treatment rather than its illustrated pill tabs. Use actual product photos/data and real source icons, not crops from either mockup.

## Width, type and rhythm

All sections below Hero use Whole House's border-box max-width 1360px container, centered, desktop inner padding 24px, below 768px 16px. At 1440px CSS viewport the inner span is 1312px and visible content margins are 64px. Remove nested 1200px/900px caps from comparison, product grid, services, FAQ and final routes.

All H2 elements, including Services, FAQ and closing: Della AC Spectral / Georgia / serif, 32px, weight 500, line-height 1.15, #0E1953 at every breakpoint. Allow wrapping and rearrange closing actions on narrow screens.

Section spacing about 40–56px desktop / 32–40px mobile; do not compound large padding and empty blocks. Spectral for headings/series/questions, Poppins for body/controls. Navy #0E1953, brand blue #5884E7. Copy the local Spectral-PageFly-Medium.woff2 for 500 weight. Navy active tabs stay approved. Small text remains readable; use blue for border/arrow accents rather than low-contrast small white-on-blue text.

## Hero

H1 and existing short lead, vertically centered in the clear copy area; keep full product names together. The precise lead is in LOCKED-COPY, even where the generated image shows a different short sentence.

Display the complete hero-desktop.png at intrinsic ratio, text inside its clear left area. At <=1100px stack copy over hero-mobile.png, whose initial reserved ratio is 4:3. No crop or text overlap on the condenser, wall head, window unit or two-hose portable.

## Open visual comparison

Three equal open columns under the H2, without outer rounded boxes or a blue table header. Each column: contained p01/p07/p11 category image in a 280px-high media area above 1100px (max image width about 330px); 220–240px at 768–1100px and 220px on mobile → Spectral category name about 26px → short 16px fit phrase → Setup and Upfront rows → text-arrow action.

Use only the exact short phrases from LOCKED-COPY. Thin horizontal rules align facts across columns; no default winner, price, rating, dense paragraphs, helper subtitle, rating band or footnote. Detailed explanation lives in Evidence. Target approximately 80 English words or less excluding H2 and repeated row/category labels.

Desktop gaps 24–32px. At <=767px use a bounded horizontally scrollable strip of the three columns, each about 78–85% of available width, with next-column peek. Scroll snap and 44px previous/next controls enhance discoverability; no added swipe paragraph. All categories stay in DOM, native scrolling remains available without JS, and only this strip scrolls horizontally.

## Products — Whole House card grammar

Heading → three Tabs → cards. No section intro, fit-check bar, shared coverage note or multi-room helper line under the grid.

Grid: Mini/Window 4 columns >1100px, 2 at 601–1100px, 1 <=600px. Portable 3 full-width equal columns >900px, 2 at 601–900px, 1 <=600px. In the intermediate two-column state keep equal card widths. At 1280/1440/1920 there is no empty fourth Portable track.

Reuse source `.product-card` details:

- square border, 1px #E2E6EE; hover blue border and subtle 0 6px 18px shadow;
- square contained media using the transparent localImage derivatives on white, preserving all equipment and accessories; margin 10px 14px 0, no nested rounded border, scale 1.02 on hover;
- inset 18px desktop / 12px mobile;
- short series name Spectral Medium 23px/1.2; separate capacity subtitle 14px;
- three solid-rule dl rows, 9px vertical padding, muted labels and navy right values;
- Full model name disclosure BEFORE price, underlined summary, initially closed;
- Spectral Bold 25px price, 16px top padding and 16px space before the purchase button; full-width navy/white 46px button with 4px radius and inversion on hover;
- flex/auto margin aligns purchase areas; no large fixed title heights.

Use the explicit field mapping in LOCKED-COPY. Repeated series H3s are valid; validate uniqueness with series + capacity + variant. Do not add an availability badge from an old snapshot merely because the source card includes one.

Below the grid use the source's right-aligned collection text-arrow link, with subtle arrow motion and keyboard focus. No centered framed browse button.

## Evidence

52/48 image/questions on desktop, vertically centered with align-items:center; stack <=1100px. H2-to-grid gap 32px desktop / 24px mobile. Keep natural content height when answers expand; stacked image-to-questions gap about 28px. Entire installation image visible, without overlay labels, figure caption or explanatory text underneath. Descriptive alt text remains.

Four question-only rows, all closed initially. Remove closed-state second-line summaries. Answers remain in DOM. Native details, visible focus, multiple items can be open when chosen.

## Services — direct Central Air reuse

Reuse `.dsc-services`, `.dsc-heading`, `.dsc-svc-grid`, `.dsc-svc`, `.dsc-svc__icon`, linked h3, paragraphs and original embedded icons. Scope them within this page; adapt only outer container to 1360px.

Confirmed: white section; LEFT-aligned Spectral Medium 32px/1.15 heading; 26px grid gap and 32px heading-to-grid margin; #F3F7FC cards, 6px radius, padding 30px 26px 28px; centered blue 58px circle with original white 50px icon; Spectral Medium 22px/1.35 linked title; 15px/1.6 paragraph. Title underline-border hover; no separate Learn more link.

Copy neutral policy sentences from LOCKED-COPY. Source responsive behavior: 4 desktop, 2 <=820px, 1 <=560px. This latest owner-selected source supersedes the previous two-column-phone recommendation.

## FAQ — Whole House reuse

#F8F9FB section, centered Spectral heading, list spans the full global content width; thin top/row rules; no outer rounded border and no 900px cap.

Summary: Spectral Medium 20px/1.28, minimum height 60px, 18px vertical padding, 9px right chevron. At <=560px: 18px and 56px height. Answer Poppins 15px/1.7. Reuse native details, chevron rotation, gentle expansion and reduced-motion handling. Keep navy small text where needed for contrast; blue can accent chevrons/rules.

All four FAQ items, four Evidence items and every product-identity disclosure initially closed. Preserve multiple-open and keyboard behavior.

## Final routes — Whole House closing band

Bounded pale-blue band, outer max-width 1360px, about 30px 40px padding, 6px radius. Left: Ready to explore your options? Right: three equal outline/navy-label shopping buttons. No paragraph or icon. These are stable three-category routes, not selected-path personalization.

Mobile stacks heading/actions, large touch targets and full-width buttons when needed. Retain hover/focus/inversion and reduced-motion behavior. Align the band with the sections above.

## Acceptance

Measure actual container widths, three equal desktop Portable columns, no deleted helper text, all details closed, unobstructed equipment, readable text and correct real product data. Preserve synchronized Tab/URL/history, nonduplicated events and stable mobile Hero sizing during delayed loading. Test 1440/1280/1024/768/430/390/360. Code changes remain within this project.
