# DELLA Mini Split Sizing Calculator — Recommendation Logic

Version: `1.2.0`
Supersedes: `Calculator_Recommendation_Logic_v1.1.0.md`
Engine: `della-sizing-engine-1.0.0`
Engine configuration: `calculator_config.json` version `1.1.0` (single source of all coefficients)
Product dataset: `della_calculator_products_v1.2.0.json` version `1.2.0`
Climate mapping: `della_series_mapping_v1`, version `1.0.0`

## What changed from 1.1.0

1. **121 published 55,000 BTU multi-zone systems added** (3-zone: 24, 4-zone: 42, 5-zone: 36, 6-zone: 19). The 2026-07-22 admin export recorded them as draft; a same-day storefront crawl verified all 121 published and purchasable. Each carries the warning `status_overridden_from_storefront`; the next admin export should re-confirm status and refresh their inventory quantities (93 of 121 lack inventory-export SKU rows and use the storefront available flag with null totals, `inventory_source = "storefront_available_flag"`).
2. **Multi-room review threshold raised from 48,000 to 55,000 BTU/h** (config 1.1.0, `complexity_rules.multi_room_review_total_btu`), matching the largest live outdoor unit. Config 1.1.0 and dataset 1.2.0 must deploy together: the higher threshold without the new products would send 48–55K projects into guaranteed no-match.
3. Head sizes now present in published bundles: 6,000 / 7,000 / 9,000 / 9,500 / 11,000 / 12,000 / 16,000 / 17,000 / 18,000 / 22,000 / 23,000 / 24,000. Standard-bin rooms (9K minimum) reach every combination a published bundle can serve; totals above 55K route to split-system paths.
4. Six-room projects are a supported outcome: 9K×6 (54K total) matches live six-zone systems.

## Dataset summary (v1.2.0 snapshot)

- Eligible products: **559** (69 single-zone, 490 multi-zone)
- Recommendable products (stock-independent): **559**
- In stock at snapshot time: **555**
- Product variants: **664**
- Unique head vectors: **240**
- Zone counts: 1: 69, 2: 86, 3: 158, 4: 138, 5: 79, 6: 29 (matches the live storefront collections)
- Voltage: confirmed on the product page (not a V1 filter)
- Heating load sizing: not supported in V1

## Unchanged rules

Room-load formula, confidence ranges, consumer capacity paths (9K–36K), preferred/conditional capacity ratios (1.15 / 1.25), single-zone catalog gaps (12,001–13,599 and 24,001–27,999; wall-mounted also 18,001–18,399), climate margins (summer +3°F, winter −5°F), the three-layer product selection architecture, the five-level Fallback Matrix, and all claims guardrails carry over from version 1.1.0 unchanged. See `Calculator_Recommendation_Logic_v1.1.0.md` for the full statements; that file remains valid except where this document supersedes it.

## Result card disclaimer

> This calculator provides a pre-purchase sizing estimate. It does not replace a professional Manual J calculation. Electrical requirements vary by model; confirm voltage and installation requirements on the product page.
