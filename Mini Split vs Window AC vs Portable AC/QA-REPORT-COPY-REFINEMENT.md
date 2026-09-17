# QA report — copy refinement (2026-09-17)

Build: `mini-split-vs-window-ac-vs-portable-ac.html` — 66,193 bytes, SHA256 `11DF4D0CDF4191ACA2E378F49ACB59E4406A034F7A38A50171C87715AC8B6CC8`.
Round: apply the 12 editorial-final copy changes from `copy-replacements-20260917.json` / `LOCKED-COPY.md`. No layout, marketing or data changes.
Status: implemented and browser-verified; returned to Codex for review. Local review build only — not committed, pushed or published. This round is recorded separately from the previous commit.

Codex audit material (`COPY-AUDIT-20260917.md`, `copy-replacements-20260917.json`) and all earlier evidence folders were preserved.

## 1. The 12 applied changes

| id | element | new text |
|---|---|---|
| hero-lead | hero lead | "Compare installation, noise, and upfront cost to choose an AC for your room." |
| installation-question | Evidence 1 question | "What does installation involve?" |
| installation-answer | Evidence 1 answer | revised install text incl. portable drainage requirement |
| noise-question | Evidence 2 question | "What affects noise in the room?" |
| noise-answer | Evidence 2 answer | revised last sentence, test-condition caveat retained |
| ratings-question | Evidence 3 question | "How do BTU and efficiency ratings differ?" |
| ratings-answer | Evidence 3 answer (first paragraph only) | new BTU/SACC/SEER2-CEER wording |
| cost-question | Evidence 4 question | "When is a mini split worth the installation cost?" |
| cost-answer | Evidence 4 answer | "…may cost less upfront"; upfront/installation cost framing |
| rental-answer | FAQ 1 answer | "a window or venting setup that fits the model and is allowed by your building" |
| window-answer | FAQ 2 answer | "A portable AC may work…"; "check whether you can install a mini split" |
| winter-answer | FAQ 4 answer | "heating output at winter temperatures where you live"; installer wording |

Exact old/new strings live in `copy-replacements-20260917.json`; the render follows `LOCKED-COPY.md`.

## 2. How it was verified

Two runners, both exit non-zero on failure:

- `qa/copy-refinement-implementation-20260917/verify-copy.mjs` — static mapping: for each JSON change, the old string is absent from the HTML and the new string is present. Output: `copy-mapping.txt`; **exit 0**.
- `qa/copy-refinement-implementation-20260917/capture.mjs` — CDP browser run over the local HTTP server. **44 assertions, 44 passed, 0 failed**; 7 screenshots. Includes a selector-based live-DOM mapping of all 12 elements and a PNG pixel check that the hero scene is really painted.

Additionally, the full image-refinement suite `qa/image-refinement-implementation-20260917/capture.mjs` was re-run unchanged: **127/127 pass, exit 0**.

## 3. Results

### Copy mapping
- Live DOM: `document.querySelector(selector).textContent` matches the new string for all 12 items (`copy-mapping-all-12`).
- Static: 0 old strings remain; 12/12 new present.

### Hero
- `hero-lead` present; at 1440 the lead wraps to 2 lines inside the copy column; at 390 and 360 it wraps without overflow.
- Hero not covered: `elementFromPoint` at the lead centre lands inside `.hero-copy` at 1440 and 390.
- Paint proof: `copy-1440-hero-clip.png` analysed in-runner (`nonUniform 0.80`, `distinct` high) — the scene is drawn, not a plain rectangle. (The capture pipeline needed the renderer-backgrounding flags plus image `decode()` and a double `requestAnimationFrame` before capture; without them a full-page capture could return a blank hero. This is a capture-timing fix, not a page change — the CSS was already correct.)

### Evidence
- Questions exactly: installation / noise / ratings / cost (new wording).
- Closed first: `evidence-closed` 0 open; H2-to-grid gap 32px.
- Expanded (all four): every answer `scrollHeight <= clientHeight + 1` (no clipping, no truncation); image/list centres within 2px (vertically centred); natural height growth.

### FAQ / structure
- FAQ 4 questions unchanged (rental / window doesn't fit / two rooms / winter heating).
- 19 `<details>`, 0 open initially; 4 Evidence, 4 FAQ, 11 cards, 6 H2.
- Comparison entry activates Window AC (`#window-ac-products`), Portable tab switches URL and panel.

### Immutable fields and links re-checked
- Prices unchanged and in order: 729.96 / 799.96 / 1049.96 / 1249.96 / 169.96 / 269.96 / 379.96 / 359.96 / 309.96 / 379.96 / 599.96.
- 11 `View Product` CTAs, 11 hrefs carrying `variant=`.
- Source links preserved: `energy.gov` and `energystar.gov` in Evidence 3; `single-zone-vs-multi-zone` in FAQ 3.
- Existing mobile one-row tabs CSS and the 16px price/button gap remain present.
- No page-level horizontal overflow at 1440/390/360; 0 console errors, 0 failed requests.

## 4. Not verified / limitations

- Only installed Chrome 152 headless was used (local HTTP and the one static mapping run); no real devices, Safari or Firefox.
- The hero paint check is a presence/diversity check on a captured clip, not a formal image diff.
- Product commercial facts were not re-fetched this round; the same-day 2026-09-17 live recheck (`qa/visual-refresh-20260917/live-verification-20260917.md`) stands and no product data changed.
- Shopify theme embedding, canonical and production analytics remain later integration work.

## 5. Files

- `mini-split-vs-window-ac-vs-portable-ac.html` (66,193 bytes; SHA256 `11DF4D0C…`)
- `qa/copy-refinement-implementation-20260917/`: `verify-copy.mjs`, `copy-mapping.txt`, `capture.mjs`, `qa-results.json`, 7 screenshots (1440 hero clip + full, 390 hero, 1440 evidence closed/expanded, 360 full, 1440 full)
- `QA-REPORT-COPY-REFINEMENT.md` (this file), updated `HANDOFF.md`
