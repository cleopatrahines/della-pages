# QA — owner refinement round (2026-09-20)

Baseline HTML: `ceiling-cassette-vs-wall-mount-mini-split.html`
Backup before this round: `backup-owner-refinement-20260920-102803.html`
Prior evidence kept in `../` (round 1) and `../` screenshots.

## 1. Hero button removed

- `Compare the styles` link removed; no replacement button/arrow. Copy block stays
  vertically centered (`.hero-overlay` flex center); the `margin` reserved for the
  button was dropped. Hero height unchanged.
- See `hero-1440.png`, `hero-390.png`.

## 2. Selector wording, order, and state consistency

Order is now priority → wall → ceiling:

1. `What matters most to you?` — Keep walls clear / Limit ceiling work / No preference
2. `Is there an open area high on a wall?` — Looks possible / No clear spot / Not sure
   (hint: an installer still needs to check clearances and the pipe route)
3. `What did an installer say about a ceiling cassette?` — Can install / Cannot install / Not checked

Values unchanged (yes/no/unknown, look/work/neutral).

Result copy no longer treats a homeowner wall observation as confirmed:
`unknown/yes` → *You have identified a possible wall location; the ceiling has not
been assessed.* `wall=no` → *no clear wall spot was found* (not an absolute claim).

### State-consistency defect — reproduced and fixed

Reproduction (CDP, headless Chrome): clear the form, set the three radios
`checked = true` **without** firing `change`, then read the result.

- Before fix: 3 radios visually checked but title still
  `Answer all three questions…` → **bug reproduced**.
- Root cause: `state` was only written inside the `change` handler; nothing rebuilt
  state from the DOM on init or on form restore.
- Fix: single data path — `readState()` reads the checked radios, `syncStyles()`
  rebuilds `.is-selected` / `.is-answered`, `render()` computes the result. Called
  from `change`, `reset`, initial load, and `window.pageshow`.
- After fix: dispatching `pageshow` on the pre-checked DOM gives
  `Compare wall mounts first`, `is-empty = false`, 3 `.is-selected`. No per-case
  exceptions were added.

`unknown/unknown` now → `Review both installation options` (installer primary +
Compare both styles). Checked 27-combination matrix: **0 mismatches**;
`ceiling = no` never recommends a cassette.

## 3. Scene image fills the card; note moved into an `i` button

- Bottom figcaption bar removed; image fills the media card at 4:3 with
  `object-fit: cover` (no stretch). Markers positioned against the media container.
- Info button (`i`), 44px hit area, keyboard-focusable, toggles the note
  `Two alternative locations are shown for comparison. This is not an installation drawing.`
  Button is above the note (z-index 2), so it closes on tap and on Escape.
  Verified at 360px: opens on click, closes on second click and on Escape.
- See `selector-info-open-360.png`.

## 4. Comparison images and centering

- Cassette image 205px, wall image 255px, media height 160px; aspect preserved.
- Table stays `table-layout: fixed` 22 / 39 / 39; both value columns centered with
  their type image/name; attribute column and group labels remain left aligned;
  cells vertically centered. Mobile keeps label-on-top + two values, left aligned.
- At 1440 and 1920: `cassetteW 205`, `wallW 255`, `colDiff 0`.
- See `comparison-1440.png`, `comparison-1920.png`, `comparison-390.png`.

## 5. FAQ H2 full width

- Removed `.faq-section .section-head { max-width: 760px }`.
- 1440 and 1920: H2 renders on a single line (height 39px, 1 line). Narrow screens
  wrap naturally. See `faq-1440.png`, `faq-1920.png`.

## 6. Footer reuses the reference closing-band

- Limited-width `#EDF2FF` band, radius 6, padding 30px 40px; left title
  `Explore both indoor-unit styles`, right two equal outline buttons (navy text,
  blue border); links unchanged. Mobile: left aligned, stacked full-width, 24px.
- See `footer-1440.png`, `footer-1920.png`, `footer-390.png`.

## 7. Regression / environment

- Widths 1440/1280/1024/768/430/390/360: `scrollWidth == clientWidth`.
- Console errors/warnings: none.
- `#products` + `#services` unchanged (same region as the frozen baseline; only
  the selector/comparison/footer/hero regions were edited this round).
- Five FAQ Q&A and JSON-LD unchanged.

## Screenshots (this folder)

- `hero-1440.png`, `hero-390.png`
- `selector-empty-1440.png`, `selector-rec-look-1440.png`,
  `selector-installer-1440.png`, `selector-empty-390.png`,
  `selector-rec-look-390.png`, `selector-info-open-360.png`
- `comparison-1440.png`, `comparison-1920.png`, `comparison-390.png`
- `faq-1440.png`, `faq-1920.png`
- `footer-1440.png`, `footer-1920.png`, `footer-390.png`
- `full-1440.png`, `full-390.png` (full page, after scroll so lazy images load)

Module clips are element-bounds captures; `full-*` are full-page captures.
