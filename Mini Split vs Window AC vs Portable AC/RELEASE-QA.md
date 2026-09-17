# Final local release review — 2026-09-17

Status: accepted for the owner-authorized local Git commit. No remote push or publishing is included.

Reviewed file: mini-split-vs-window-ac-vs-portable-ac.html, 66,058 bytes.
SHA256: 594E411912104FED9E8FF5F5AD76DF23210784A81D08DDFC2FC9DC2401F17151

## Verification

- Codex reran the supplied dependency-free Chrome CDP suite against the unchanged final HTML: **121/121 passed, exit code 0**, with 14 newly captured images. The copied runner's project path points at this project and its output points at an isolated review directory. Compact results: qa/codex-final-review-20260917/qa-results.json. Reproduce using the project's qa/image-refinement-implementation-20260917/capture.mjs.
- Inspected supplied desktop/mobile captures and the actual-painted Hero clip. Accepted comparison scale 280/235/220px and proportional 330px width cap; complete products are visible. Accepted transparent media, 32px Spectral H2, centered Evidence, four FAQs and 16px price/button spacing.
- Source-checked Hero has no button/link and the shared price rule provides 16px bottom margin. Verified local HTML image and font references exist.
- Existing suite covers 14 cutout positions, 11 product mappings, 19 initially closed disclosures, tabs/history/single event, mobile rail bounds, text contrast, no-JS, reduced motion, file URL and eight widths including 1920/1440/360. No console errors or failed requests.
- All production HTML code is DeepSeek's reviewed implementation. Codex reconciled only planning/status documents before committing.

## Limits

Full-page automated captures may omit the desktop Hero after scrolling; the dedicated actual-painted clip contains the scene and the pixel check passes. This remains a capture limitation and should not be represented as a successful full-page image diff. Real-device touch feel, Safari/Firefox and Shopify embedding are not verified.

This is a static review page. Commercial facts were unchanged; the recorded same-day live check belongs to DeepSeek, not a fresh Codex price fetch. Shopify theme offsets, live product rendering and production canonical are later integration work.

## Commit scope

Only the Mini Split vs Window AC vs Portable AC page, its runtime fonts/scenes/cutouts, original product images for reproducibility, manifest, processing script, core maintenance documents and compact QA records. Historic screenshots and research/generation bundles are preserved locally. Unrelated repository changes are excluded.
