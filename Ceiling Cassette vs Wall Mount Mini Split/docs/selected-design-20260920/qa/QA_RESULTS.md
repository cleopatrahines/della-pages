# QA results — SELECTED_DESIGN implementation + visual-fix round

All checks run in real headless Chrome via CDP against the local file.
Screenshots in this folder.

## Round 2 — local visual/semantic fixes

### Fix 1 — Q1 wording now matches the resolver

- Legend changed from `Ceiling installation checked?` to
  **`Can your ceiling accommodate a cassette?`**
- Options changed to **Feasible / Not feasible / Not sure** (internal values
  unchanged: yes / no / unknown).
- Added the hint: *Choose Not sure if ceiling space, drainage and service access
  have not been checked.*
- Resolver/matrix unchanged. 27-combination re-test: **0 mismatches**,
  `ceiling = no` never recommends a cassette.

### Fix 2 — mobile selector density and selected state

- Options are now 3 equal columns per question at 360 / 390 / 430 (labels wrap,
  no shrinking): `optionCols = 3`, option font 13px, option height 46–51px.
- Selector module height: **390px 1,084px** and **360px 1,135px**
  (was ~1,426px at 390px).
- Empty / incomplete result uses a plain 15px sans prompt + Compare both styles;
  Reset is hidden until an answer exists (`empty.resetHidden = true`,
  `empty.titleFont = Poppins`, `empty.titleSize = 15px`).
- Recommended result keeps title + reason + verify + CTA.
- Selected option is now light blue + navy border + navy radio dot
  (`rgb(237,242,255)` bg, `rgb(14,25,83)` border) instead of a solid navy button.
  (A first read at t=0 showed white because of the 150ms CSS transition; the
  settled value is correct.)

### Fix 3 — desktop comparison columns

- `table-layout: fixed` with `<colgroup>` 22% / 39% / 39%.
- Data column widths at 1440 and 1280: **468px vs 468px (diff 0px)**.
- Type name centered over its column; body text stays left aligned.
- Per-type display caps: cassette image 240px, wall image 300px, media height
  180px, aspect ratio preserved (no stretch).

### Fix 4 — duplicate `</head>` removed (was lines 1006–1007); now 1 occurrence.

### Fix 5 — Services icons

Not a page fault: the white line icons are `loading="lazy"` data-URI images and
had not been scrolled into view when the earlier screenshot was taken. After
scrolling `#services` into view and awaiting decode,
`services-1440-loaded.png` shows all four glyphs; `failedImages = 0`.
Services source/content was not modified.

## 1. Selector resolver — 27/27 (re-run)

0 mismatches against the PRD matrix; 0 `ceiling = no` → cassette cases.
Key states unchanged: `yes/yes/look → Compare ceiling cassettes first`,
`unknown/unknown → Check the installation locations` (installer CTA),
incomplete states give no recommendation and keep Compare both styles.

## 2. FAQ visible vs JSON-LD

Visible items 5; schema questions 5; decoded question + answer strings match
exactly.

## 3. Responsive / overflow (clientWidth / scrollWidth)

| viewport | client | scroll | page overflow |
|---|---|---|---|
| 1440 | 1425 | 1425 | 0 |
| 1280 | 1265 | 1265 | 0 |
| 1024 | 1009 | 1009 | 0 |
| 768 | 753 | 753 | 0 |
| 430 | 430 | 430 | 0 |
| 390 | 390 | 390 | 0 |
| 360 | 360 | 360 | 0 |

## 4. Console

No errors or warnings.

## 5. Images

After a full scroll pass: failed images = 0 on both 1440 and 390.

## 6. Keyboard / reduced motion / no-JS (round 1, unchanged)

Radio group responds to arrow keys; FAQ summary toggles; reduced motion swaps the
project tab image immediately; with JS disabled the Hero, 3 questions,
comparison rows/groups, 4 product cards and 5 FAQ items still render.

## 7. Frozen module regression

`#products` + `#services` remain **byte-identical** to
`backup-selected-design-20260920-093959.html` (length 20,135; string equality
re-checked after the visual-fix round).

## Screenshot index (this folder)

Module-clip (element bounds) unless marked full page:

- Hero: `hero-1440.png`, `hero-390.png`
- Selector: `checker-empty-1440.png`, `checker-partial-1440.png`,
  `checker-rec-look-1440.png`, `checker-installer-1440.png`,
  `checker-empty-390.png`, `checker-rec-look-390.png`, `checker-empty-360.png`,
  `checker-rec-work-430.png`
- Comparison: `comparison-1440.png`, `comparison-1280.png`,
  `comparison-390.png`, `comparison-360.png`, `comparison-430.png`
- Services (loaded): `services-1440-loaded.png`
- FAQ open (mobile, acceptance only): `faq-open-390.png`
- Footer: `footer-1440.png`, `footer-390.png`
- Full page (all images loaded): `full-1440.png`, `full-390.png`

Note: `products-1440.png` / `services-1440.png` from round 1 are module clips;
`full-1440.png` / `full-390.png` are full-page captures taken after a scroll pass.
