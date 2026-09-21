# Codex visual research and acceptance notes — 2026-09-21

## User goal

Make the “Which style fits your room?” decision module feel like a polished Della product page and remain easy to use on mobile. Make the “Ceiling cassette or wall mount?” comparison less image-heavy, with smaller product images that do not dominate mobile.

## Reference patterns reviewed

- Della coupon page: warm white canvas, navy navigation/CTA, editorial serif headings, product groups separated by generous whitespace and light neutral blocks.
- Insta360 X6 product page: clear split between product imagery and decision controls; modular pale cards for secondary actions; sticky purchase action is visually distinct.
- EcoFlow Delta Pro Ultra: strong visual hierarchy, separate media and narrative columns, short feature lists, clear section transitions and primary CTA.
- Govee/Anker/Dreame product pages: white or very light surfaces, compact product cutouts, controlled borders/shadows, and cards that keep the product as the focal point without filling the viewport.

## Direction to implement

1. Selector: use an editorial “decision studio” treatment. Keep the room illustration and location markers, but put it inside a controlled media card with a deliberate crop/height. Put the three questions in a compact numbered/stepped panel with stronger grouping, clear selected states, one quiet result card, and one primary action. Keep all original radio names, result logic, reset, compare link, and accessible labels.
2. Selector mobile: title and one-line intro first, then a compact scene card, then questions. Avoid a 4:3 image that consumes the whole first viewport. Keep touch targets at least 44px and allow labels to wrap without clipping.
3. Comparison: keep the semantic table and six factual rows. Present the two indoor-unit assets in smaller, equal visual frames with generous white space. Cap cassette and wall images independently so neither makes the table header tall; verify at 390px as well as desktop.
4. Visual system: reuse local Spectral/Poppins, navy #0E1953, blue #5884E7, warm white/very light blue surfaces, 1px neutral borders, modest radii, and a single navy CTA. Avoid heavy gradients, giant rounded containers, and decorative product copy.

## Acceptance checks

- No product image in the comparison header exceeds the compact frame on desktop or mobile; no horizontal overflow at 390px.
- Selector options, result matrix, info note, reset, compare link, products tabs, services, FAQ, and JSON-LD remain functional and unchanged in meaning.
- Default selector state is neutral/unanswered; result updates after any three answers and remains readable when labels wrap.
- Run focused browser checks at 1440px and 390px, capture selector and comparison screenshots, and record any remaining caveat.

## Optional visual asset created

- `assets/selector-editorial-room.png` is a generated wide editorial room scene with both indoor-unit placements at restrained scale and open negative space. Use it only if browser QA shows a clearer crop than `assets/selector-alternatives.png`; keep the existing image as the fallback and preserve the installation-illustration disclaimer.

## Authority note

The user's current request overrides earlier design-task wording in repository docs when they conflict. Repository docs are implementation context and acceptance evidence; they are not additional user instructions.
