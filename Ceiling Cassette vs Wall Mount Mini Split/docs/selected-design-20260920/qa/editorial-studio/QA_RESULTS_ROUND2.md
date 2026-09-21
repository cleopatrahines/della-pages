# QA — round 2: selector alignment + compact comparison (2026-09-21)

Target: `ceiling-cassette-vs-wall-mount-mini-split.html`
Backup before round: `backup-align-round2-20260921-102706.html`

Note: this round's brief referenced `.checker-grid` / `.checker-scene`, which were
renamed to `.checker-studio` / `.checker-media` in the previous round. The
requested behavior was applied to the current classes.

## 1. Selector

- Media card uses a **fixed aspect ratio** so it never changes size with the
  right column: 16:9 on mobile, 1:1 on desktop (`align-items: start`, no stretch),
  with `object-fit: cover; object-position: right center` on desktop.
  Measured at 1440: frame height **601px in default, recommended and installer
  states (stable, identical)**; frame ratio 1.000.
- Image still shows **both** devices (ceiling cassette and wall unit); wide 16:9
  source is cropped from the right so both remain in view. Rendered box ratio
  1.03 vs natural 1.78 confirms intentional cover crop.
- `.checker-options` is now `grid-template-columns: repeat(3, minmax(0,1fr))` on
  all breakpoints; the first group renders **3 options on 1 row**. Option height
  is 44px (single line) after setting `.checker-option` to 13px with a 15px
  radio and 7px gap (`9px 12px` padding). Measured: 1 distinct top row,
  heights [44,44,44] ≥ 44px; at 14px "Limit ceiling work" wrapped to 2 lines.
- Visible caption removed (0 occurrences of the text and of
  `.checker-media__caption`). HTML markers removed (0 occurrences). Info button
  + hidden accessible note kept (note text updated to not reference markers).

## 2. Comparison

- Desktop media frame 84px; cassette image 115×82px, wall image 155×57px,
  both `object-fit: contain` at natural ratio (1.40 and 2.73). Type name 18px.
- Mobile (390) media frame 64px; cassette 80×57px, wall 108×40px; name 17px.
- 22/39/39 column structure intact; both data columns equal (colDiff 0).
  Semantic table/caption/6 rows/group labels unchanged.

## 3. Verification

- Default: 0 radios checked, result empty, Reset hidden → no preselection.
- ceiling=yes + wall=yes + priority=look → "Compare ceiling cassettes first".
- Reset clears radios + result. Info note opens on click, closes on Escape.
- No horizontal overflow: 1440 / 1024 / 768 / 430 / 390 / 360 all
  `scrollWidth == clientWidth`.
- FAQ visible (5) matches JSON-LD (5). `#products` (4 cards) and `#services`
  (4 cards) present; that region is byte-identical to the pre-round backup.
- Console: no errors or warnings.

## Screenshots (absolute paths)

```
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-1440-round2.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\selector-390-round2.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\comparison-1440-round2.png
C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\docs\selected-design-20260920\qa\editorial-studio\comparison-390-round2.png
```

Module clips (element bounds).

## Residual visual risks

- Tall-screen desktop (>~700px right column): the right-aligned cover crop keeps
  the wall unit fully visible but may clip the left edge of the ceiling cassette.
- Comparison thumbnails are intentionally small; on very wide screens they read
  as tiny identification icons rather than product shots.
- Mobile comparison type names can wrap to two lines at 360–390px.

## Mobile product cards (learned from Mini Split vs Window AC vs Portable AC)

Reference: `.product-image-wrap { aspect-ratio: 1/1 }` full-width image on top,
single-column at <=600px. Applied the same pattern to `.project-product-card` at
`<=780px`:

- Card is now `display: flex; flex-direction: column` (was a `112px + 1fr` grid
  with a small thumbnail).
- `__image` is `width: 100%`, `aspect-ratio: 1/1`, `padding: 16px`, hairline
  bottom border; image `object-fit: contain; max-height: 100%`.
- `__body` stacks below (type, title, capacity, meta, price, View Product).

Measured:
- 390px: image box **356x356** (was 112x112), card width 358, 1 column, no
  horizontal overflow; all 4 product images load (`failed imgs: 0`).
- 1440px: **unchanged** - image box 286x236, card width 288.
- Console: none.

Screenshot: `products-390-round2.png`
