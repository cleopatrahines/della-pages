# Codex visual audit — round 2 — 2026-09-21

## Observed blockers from the supplied screenshots

- Desktop selector is vertically unbalanced: the left media card ends after the image while the right question/result stack continues, leaving a large blank area under the image.
- The first priority row wraps to two controls plus one. The three controls need equal-width columns and must stay on one row at the desktop breakpoint.
- The visible illustration caption adds noise and is no longer wanted by the user. Remove it from the visible layout.
- Comparison header assets still read like large product showcases. They need to become small identification thumbnails, on both desktop and mobile.

## Required second-pass direction

- Desktop selector grid must stretch both columns to the same row height. The media frame should fill the left column height with `height: 100%`, a deliberate crop, and `object-fit: cover`; do not leave an empty white region below it.
- Selector options should use equal-width grid columns (`repeat(3, minmax(0, 1fr))`) at the desktop/tablet breakpoint. Reduce horizontal padding enough for “Keep walls clear”, “Limit ceiling work”, and “No preference” to fit in one row. Keep 44px minimum height.
- Remove the visible “Alternative installation locations…” caption. The info control may retain a hidden accessible explanation if needed.
- Comparison media frames should be identification-sized: desktop frame about 72–90px high, cassette image max about 110–125px wide, wall image max about 145–165px wide; mobile frame about 58–70px high with proportionally smaller images. Keep `object-fit: contain` and do not distort assets.
- Recheck the entire table at 1440px and 390px for alignment, overflow, and visual weight.
