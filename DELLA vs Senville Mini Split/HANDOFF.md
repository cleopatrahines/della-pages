# DELLA vs Senville Mini Split — handoff

Page: `della-vs-senville-mini-split.html` (self-contained CSS/JS; not in `_system/sync.py`). Working copy and research docs live in `Desktop/DELLA vs Senville Mini Split/`.

## Layout (v2, 2026-11-26)
1. Hero — H1 + one sentence (no entrance animation on H1 or hero image).
2. Sub-nav — Key Differences · Install & Warranty · Match Senville · Buyer Q&A · FAQs.
3. **Where They Actually Differ** — four honest verdicts (DIY → DELLA, everyday 12K → DELLA, sub-zero → even, quietest → Senville), then one head-to-head board with a matchup switch (Vario vs LETO / Optima vs AURA / Multi-Zone). Lead side = navy bar + check. This replaces the old tab stage and the separate spec table (`#spec-sheet` id kept on the board).
4. **Installation Path & Warranty** — one switch (I'll install it / Licensed HVAC pro); the model pair follows the matchup chosen above. Navy panel: Rental Install Kit (DIY) or Find a Partner Installer (pro).
5. **Match Your Senville Pick to DELLA** — sidebar + capacity chips (chips with no results are disabled; pressing the active chip again resets it). Live Shopify price/stock on dellahome.com.
6. Forum Q&A accordion → Trust → FAQ (FAQPage JSON-LD) → CTA → phone buy bar ("From $X" = lowest card price, follows live prices).

Deep links: `#winter`, `?match=cold|multi|shop|everyday`, `?install=pro`. Tracking calls `window.dellaTrack` if present (`dvs_matchup`, `dvs_install_path`, `dvs_filter_group`, `dvs_filter_cap`, `dvs_jump_to_matches`).

## Facts verified 2026-11-26
- DELLA (product `.js` + PDP spec tables + /pages/warranty-policy): Vario 12K 23 SEER2 / 9.5 HSPF2 / −4°F / 28 dBA / 16.4 ft line set; Optima Pro 12K 25 / 10.5 / −22°F / 30 dB mute; Optima CloudAir 12K 24 / 10 / −13°F; Motto 115V 20 / 8.5 / 5°F, R-32, 16 ft; Vario Tri 28K −13°F. Lifetime parts incl. compressor for registered DIY **and** pro installs (100 days); rental-kit installs add a video link; after year 1 the owner pays part shipping. Rental kit: $100 (7-day) / $150 (15-day) + $300 refundable deposit.
- Senville (senville.com product, warranty-registration, help center): LETO 230V 21.3 SEER2 / **9.1** HSPF2 (110V 21.2 / 8.7), 5°F, min 22.5 dB (110V 17.5 dB), 5/5 warranty, Alexa USB kit included, Wi-Fi kit sold separately; AURA 12K 25.4 / 10.5, −22°F, 24 dB, AHRI + ENERGY STAR, 5 parts / 10 compressor; multi-zone AURA 2–6 zones, max 48K BTU. "DIY installation will void your warranty coverage." Senville does not name its manufacturer (Midea is forum lore only). No base pan heater claim on either brand (not stated officially).
- Old Optima 12K handle `optima-series-12000-btu-seer2-24-…` is 404; card now points to `della-optima-cloudair-series-12000-btu-24-seer2-ultra-heat-mini-split-ac-up-to-550-sq-ft`.
- Senville prices seen 2026-11-26 (not on the page): LETO 12K 230V $869.99 (out of stock), 110V $799.99, AURA 12K $1,399.99, AURA Dual 18K $2,099.99.

## Before PageFly
Upload `assets/*` to Shopify Files and swap the relative URLs (and `og:image`). Re-check live prices on a dellahome.com preview.
