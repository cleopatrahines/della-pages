# Implementation Notes - 12000 BTU vs 18000 BTU Mini Split

Status: pre-HTML validation
Last updated: 2026-06-22T11:15:28+08:00

## Product Data Verification

Source method: Della Shopify PDP and product JSON endpoints (`/products/{handle}.js`).

All eight locked products were reachable. All eight PDP pages returned HTTP 200. All eight provided CDN product image URLs returned HTTP 200 image/jpeg. Live selling prices were parsed successfully.

| Group | Product | Live title from Della | Live price | Available | PDP status | Image status | verified_at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12K | Optima 12K | DELLA Optima Series 12000 BTU 24 SEER2 Ultra Heat Mini Split AC - Up to 550 Sq.Ft. | $894.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 12K | Vario 12K | DELLA Vario Series 12000 BTU 23 SEER2 Mini Split Heat Pump AC - Up to 550 Sq.Ft. | $779.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 12K | Umbra 12K | DELLA Umbra Series 12000 BTU 17 SEER2 Mini Split Heat Pump AC - Up to 550 Sq.Ft. | $799.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 12K | Serena Cloud Air 12K | DELLA Serena CloudAir Series 12000 BTU 22 SEER2 Mini Split Heat Pump AC - Up to 550 Sq.Ft. | $809.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 18K | Serena 18K | DELLA Serena Series 18000 BTU 22 SEER2 Mini-Split Heat Pump AC - Up to 1000 Sq.Ft. | $1,049.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 18K | Vario 18K | DELLA Vario Series 18000 BTU 21 SEER2 Mini Split Heat Pump AC - Up to 1000 Sq.Ft. | $1,049.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 18K | Umbra 18K | DELLA Umbra Series 18000 BTU 19 SEER2 Mini Split Heat Pump AC - Up to 1000 Sq.Ft. | $1,029.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |
| 18K | Serena Cloud Air 18K | DELLA Serena CloudAir Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC - Up to 1000 Sq.Ft. | $1,079.96 | true | 200 | 200 image/jpeg | 2026-06-22T11:15:28+08:00 |

Implementation notes:

- Front-end coverage chip format should still use PRD style: `Up to 550 sq. ft.` and `Up to 1,000 sq. ft.`.
- Product titles may be cleaned for display capitalization and spacing, but must preserve verified product identity.
- Prices are static snapshots for standalone HTML. Re-verify before final publication or Shopify paste-in.
- No compare-at prices, badges, discounts, coupon copy, review stars, or sold-out labels should be added.

## Hero Product Image Mapping

Hero 12K representative:

- Product: DELLA Optima Series 12000 BTU 24 SEER2 Ultra Heat Mini Split AC
- Image: `12k.webp` from the project folder, supplied by the user.

Hero 18K representative:

- Product: DELLA Serena Series 18000 BTU 22 SEER2 Mini Split Heat Pump AC
- Image: `18k.webp` from the project folder, supplied by the user.

## Scenario Image Map - Pending Approval

These are proposed Della-owned/local lifestyle images for the four scenario cards. Final HTML should not start until this image map is approved.

| Scenario | Direction label | Source image | Proposed local asset name | Note |
| --- | --- | --- | --- | --- |
| Bedroom or home office | 12K starting point | `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\home-situations-single-zone-office.webp` | `assets/scenario-bedroom-home-office.webp` | Best fit for office; clean Della wall-mount scene. |
| Small living room | 12K or 18K based on layout | `C:\Users\18041\Desktop\della-pages\single-zone-vs-multi-zone-mini-split\banner desktop.webp` | `assets/scenario-small-living-room.webp` | Use object-position crop toward the living-room side; avoid showing the whole wide banner in a card. |
| Garage or sunroom | Check 18K | `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\assets\scene-sunroom.webp` | `assets/scenario-garage-sunroom.webp` | Sunroom fit; use copy carefully because garage loads vary. |
| Open living and dining area | 18K starting point | `C:\Users\18041\Desktop\della-pages\Ceiling Cassette vs Wall Mount Mini Split\assets\scene-open-living.webp` | `assets/scenario-open-living-dining.webp` | Strong open bright room visual; suitable for larger/open layout card. |

## Current Gate Status

Product data gate: passed.

Scenario image map gate: pending user approval.

HTML implementation: not started.

