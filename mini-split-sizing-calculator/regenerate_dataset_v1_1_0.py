#!/usr/bin/env python3
"""Regenerate the DELLA calculator product data package as version 1.1.0.

Executes the PRD 16.2 eligibility-field migration:
  calculator.enabled          -> calculator.recommendable
  calculator.priority_score   -> calculator.merchandising_priority (CSV/Excel naming)

Rules applied (PRD 16.2 / 25.7):
  - recommendable is derived WITHOUT inventory. The four products whose only
    legacy disable reason was zero stock are re-evaluated: no independent
    exclusion exists, so they become recommendable=true and are filtered only
    by live stock at result time.
  - data_quality_score is recomputed without the stock deduction.
  - climate blocks gain climate_value_source and climate_mapping_version.
  - runtime_config is removed from the product JSON; calculator_config.json
    is the single source of engine coefficients.
  - The Shopify import CSV drops the head_vector JSON column; the canonical
    lookup field is head_vector_key (PRD 16.1).

Inputs  (v1.0.0): ../della_calculator_products.json
                  ../DELLA_Calculator_Product_Dataset_Final.xlsx
Outputs (v1.1.0): ../dataset_v1.1.0/
"""
import json
import os
from datetime import datetime, timezone

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "dataset_v1.1.0")
os.makedirs(OUT, exist_ok=True)

SRC_JSON = os.path.join(ROOT, "della_calculator_products.json")
SRC_XLSX = os.path.join(ROOT, "DELLA_Calculator_Product_Dataset_Final.xlsx")

CLIMATE_VALUE_SOURCE = "della_series_mapping_v1"
CLIMATE_MAPPING_VERSION = "1.0.0"
NEW_VERSION = "1.1.0"

with open(SRC_JSON, encoding="utf-8") as f:
    src = json.load(f)

products = src["products"]
assert len(products) == 438, "expected 438 eligible products"

# ---------------------------------------------------------------- migration
reactivated = []
for p in products:
    calc = p["calculator"]
    legacy_enabled = calc.pop("enabled")
    non_stock_warnings = [w for w in calc["warnings"] if w != "out_of_stock"]
    if legacy_enabled:
        recommendable = True
    else:
        # Re-evaluate without inventory: is there any independent exclusion?
        independent_exclusion = any(
            w not in ("heating_capacity_curve_unavailable", "voltage_check_product_page")
            for w in non_stock_warnings
        )
        recommendable = not independent_exclusion
        if recommendable:
            reactivated.append(p["handle"])
    # Recompute data quality without the stock deduction: the only deduction
    # in the v1.0.0 snapshot was out_of_stock (100 -> 90).
    if not legacy_enabled and calc["data_quality_score"] == 90 and recommendable:
        calc["data_quality_score"] = 100
    new_calc = {
        "eligible": calc["eligible"],
        "recommendable": recommendable,
        "merchandising_priority": calc.get("merchandising_priority", 50),
        "data_quality_score": calc["data_quality_score"],
        "warnings": calc["warnings"],  # out_of_stock kept as snapshot info only
    }
    p["calculator"] = new_calc
    p["climate"]["climate_value_source"] = CLIMATE_VALUE_SOURCE
    p["climate"]["climate_mapping_version"] = CLIMATE_MAPPING_VERSION

recommendable_count = sum(p["calculator"]["recommendable"] for p in products)
in_stock_count = sum(p["inventory"]["in_stock"] for p in products)

meta = src["metadata"]
meta["dataset_version"] = NEW_VERSION
meta["source_dataset_version"] = "1.0.0"
meta["regenerated_at_utc"] = datetime.now(timezone.utc).isoformat()
meta.pop("enabled_product_count", None)
meta["recommendable_product_count"] = recommendable_count
meta["in_stock_product_count"] = in_stock_count
meta["climate_mapping_version"] = CLIMATE_MAPPING_VERSION
meta["climate_value_source"] = CLIMATE_VALUE_SOURCE
meta["migration_notes"] = [
    "calculator.enabled removed; calculator.recommendable is canonical (PRD 16.2).",
    "recommendable derived without inventory; in-stock is a separate live filter.",
    f"Re-evaluated previously disabled out-of-stock products: {len(reactivated)} restored to recommendable=true.",
    "runtime_config removed; calculator_config.json (config_version 1.0.0) is the single engine-coefficient source.",
    "Prices and inventory in this file are snapshots, not storefront truth (PRD 15.4).",
]
src.pop("runtime_config", None)

out_json = os.path.join(OUT, "della_calculator_products_v1.1.0.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(src, f, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- Excel
xl = pd.ExcelFile(SRC_XLSX)

pf = xl.parse("Products Final")
assert list(pf["Handle"]) == [p["handle"] for p in products], "Excel/JSON handle order mismatch"
rec_map = {p["handle"]: p["calculator"] for p in products}
pf = pf.rename(columns={"Enabled": "Recommendable", "Priority": "Merchandising Priority"})
pf["Recommendable"] = [rec_map[h]["recommendable"] for h in pf["Handle"]]
pf["Data Quality"] = [rec_map[h]["data_quality_score"] for h in pf["Handle"]]
pf.insert(len(pf.columns) - 1, "In Stock (Snapshot)", [p["inventory"]["in_stock"] for p in products])
pf.insert(pf.columns.get_loc("Max Temp F") + 1, "Climate Value Source", CLIMATE_VALUE_SOURCE)
pf.insert(pf.columns.get_loc("Climate Value Source") + 1, "Climate Mapping Version", CLIMATE_MAPPING_VERSION)

variants = xl.parse("Variants Inventory")
mzm = xl.parse("Multi Zone Matrix").rename(columns={"Enabled": "Recommendable"})
mzm["Recommendable"] = [rec_map[h]["recommendable"] for h in mzm["Handle"]]

issues = pd.DataFrame(
    {
        "Handle": [p["handle"] for p in products if p["calculator"]["warnings"]],
        "Title": [p["title"] for p in products if p["calculator"]["warnings"]],
        "Series": [p["series"] for p in products if p["calculator"]["warnings"]],
        "System Type": [p["system_type"] for p in products if p["calculator"]["warnings"]],
        "Warnings": ["; ".join(p["calculator"]["warnings"]) for p in products if p["calculator"]["warnings"]],
        "Data Quality": [p["calculator"]["data_quality_score"] for p in products if p["calculator"]["warnings"]],
        "Recommendable": [p["calculator"]["recommendable"] for p in products if p["calculator"]["warnings"]],
    }
)

excluded = xl.parse("Excluded Products")
climate_rules = xl.parse("Climate Rules")
climate_rules["Value Source"] = CLIMATE_VALUE_SOURCE
climate_rules["Mapping Version"] = CLIMATE_MAPPING_VERSION
btu_rules = xl.parse("BTU Rules")
extra_rule = pd.DataFrame(
    [{"Rule": "Engine coefficients source", "Value": "calculator_config.json 1.0.0",
      "Description": "Values shown here are informational; the versioned config file is canonical."}]
)
btu_rules = pd.concat([btu_rules, extra_rule], ignore_index=True)

mfd = xl.parse("Metafield Definitions")
mfd.loc[mfd["Key"] == "enabled", ["Key", "Purpose", "Example"]] = [
    "recommendable",
    "Structural/commercial calculator eligibility; independent of stock",
    "true",
]
mfd.loc[mfd["Key"] == "priority_score", ["Key", "Purpose"]] = [
    "merchandising_priority",
    "Merchandising tie-break within valid candidates, 0-100, default 50",
]
mfd = mfd[mfd["Key"] != "head_vector"].reset_index(drop=True)  # PRD 16.1: key is canonical; json type unsupported in product CSV

summary_rows = [
    ["DELLA Calculator Product Dataset v1.1.0", None, None, None, None, None],
    [f"Regenerated {datetime.now(timezone.utc).date().isoformat()} from v1.0.0 via PRD 16.2 migration", None, None, None, None, None],
    [None, None, None, None, None, None],
    ["Eligible Products", "Recommendable", "In Stock (Snapshot)", "Variants", "Single Zone", "Multi Zone"],
    [len(products), recommendable_count, in_stock_count, int(variants.shape[0]), 69, 369],
    [None, None, None, None, None, None],
    ["Migration facts", None, None, None, None, None],
    ["calculator.enabled removed; calculator.recommendable canonical", None, None, None, None, None],
    [f"Out-of-stock products restored to recommendable: {len(reactivated)}", None, None, None, None, None],
    ["Inventory/prices are snapshots; live stock is a separate result-time filter", None, None, None, None, None],
    ["head_vector metafield dropped from import; head_vector_key is canonical", None, None, None, None, None],
]
summary = pd.DataFrame(summary_rows)

out_xlsx = os.path.join(OUT, "DELLA_Calculator_Product_Dataset_v1.1.0.xlsx")
with pd.ExcelWriter(out_xlsx, engine="openpyxl") as w:
    summary.to_excel(w, sheet_name="Summary", header=False, index=False)
    pf.to_excel(w, sheet_name="Products Final", index=False)
    variants.to_excel(w, sheet_name="Variants Inventory", index=False)
    mzm.to_excel(w, sheet_name="Multi Zone Matrix", index=False)
    issues.to_excel(w, sheet_name="Data Issues", index=False)
    excluded.to_excel(w, sheet_name="Excluded Products", index=False)
    climate_rules.to_excel(w, sheet_name="Climate Rules", index=False)
    btu_rules.to_excel(w, sheet_name="BTU Rules", index=False)
    mfd.to_excel(w, sheet_name="Metafield Definitions", index=False)

# ---------------------------------------------------------------- Shopify CSV
def csv_bool(v):
    return "TRUE" if v else "FALSE"

rows = []
for p in products:
    cap = p["capacity"]
    cl = p["climate"]
    eff = p["efficiency"]
    calc = p["calculator"]
    mz = p["system_type"] == "multi_zone"
    rows.append({
        "Handle": p["handle"],
        "Title": p["title"],
        "Recommendable (product.metafields.calculator.recommendable)": csv_bool(calc["recommendable"]),
        "System Type (product.metafields.calculator.system_type)": p["system_type"],
        "Zone Count (product.metafields.calculator.zone_count)": p["zone_count"],
        "Unit Type (product.metafields.calculator.unit_type)": p["unit_type"],
        "Series (product.metafields.calculator.series)": p["series"],
        "Nominal BTU (product.metafields.calculator.nominal_btu)": cap["nominal_btu"],
        "Outdoor Capacity BTU (product.metafields.calculator.outdoor_capacity_btu)": cap["outdoor_capacity_btu"],
        "Head Configuration (product.metafields.calculator.head_configuration)": cap["head_configuration_raw"] or "",
        "Head Vector Key (product.metafields.calculator.head_vector_key)": cap["head_vector_key"],
        "Connected Head Total BTU (product.metafields.calculator.connected_head_total_btu)": cap["connected_head_total_btu"] if mz else "",
        "Connected Capacity Ratio (product.metafields.calculator.connected_capacity_ratio)": cap["connected_capacity_ratio"] if mz else "",
        "Climate Min F (product.metafields.calculator.climate_min_f)": cl["min_operating_temp_f"],
        "Climate Max F (product.metafields.calculator.climate_max_f)": cl["max_operating_temp_f"],
        "Climate Tier (product.metafields.calculator.climate_tier)": cl["tier"],
        "SEER2 (product.metafields.calculator.seer2)": eff["seer2"] if eff["seer2"] is not None else "",
        "Refrigerant (product.metafields.calculator.refrigerant)": eff["refrigerant"] or "",
        "Merchandising Priority (product.metafields.calculator.merchandising_priority)": calc["merchandising_priority"],
        "Data Quality Score (product.metafields.calculator.data_quality_score)": calc["data_quality_score"],
        "Voltage Policy (product.metafields.calculator.voltage_policy)": "check_product_page",
        "Heating Sizing Supported (product.metafields.calculator.heating_sizing_supported)": "FALSE",
    })
csv_df = pd.DataFrame(rows)
out_csv = os.path.join(OUT, "Shopify_Calculator_Metafields_v1.1.0.csv")
csv_df.to_csv(out_csv, index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- reconciliation
report = []
jh = [p["handle"] for p in products]
report.append(("json products", len(jh)))
report.append(("json unique handles", len(set(jh))))
report.append(("excel rows", pf.shape[0]))
report.append(("csv rows", csv_df.shape[0]))
report.append(("handle sets identical", set(jh) == set(pf["Handle"]) == set(csv_df["Handle"])))
report.append(("recommendable count (all three)", (recommendable_count,
                int(pf["Recommendable"].sum()),
                int((csv_df.filter(like="Recommendable").iloc[:, 0] == "TRUE").sum()))))
report.append(("in-stock snapshot count", in_stock_count))
report.append(("restored products", reactivated))
idx_handles = set()
for group in src["indexes"].values():
    for lst in group.values():
        idx_handles.update(lst)
report.append(("index orphans", sorted(idx_handles - set(jh))))
dup_sku = variants["SKU"].duplicated().sum()
report.append(("duplicate SKUs in variants", int(dup_sku)))

print("=== v1.1.0 reconciliation ===")
for k, v in report:
    print(f"{k}: {v}")
print(f"\nwritten:\n  {out_json}\n  {out_xlsx}\n  {out_csv}")
