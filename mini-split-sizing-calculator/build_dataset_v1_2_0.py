#!/usr/bin/env python3
"""Build dataset v1.2.0: v1.1.0 plus the 121 published 55K multi-zone systems.

Background (catalog_coverage_report.md section 5): the 2026-07-22 admin export
recorded 121 55,000 BTU multi-zone products as draft/unpublished, but a live
storefront crawl the same day found all of them published and available. This
script rebuilds the four-artifact package with those products included.

Provenance rules:
- Product fields come from the admin export metafields (same sources as the
  original pipeline): Indoor Config, Series, Outdoor Capacity Btu, SEER2,
  Refrigerant type, Type.
- Published status for the 121 is overridden from the live crawl; each such
  product carries the warning `status_overridden_from_storefront`.
- Inventory joins the admin inventory export by SKU. SKUs absent from that
  export (products were draft at export time) fall back to the storefront
  `available` flag with `inventory_source = "storefront_available_flag"` and
  null quantity totals.

Inputs: ../products_export_1.csv, ../inventory_export_1.csv,
        ../dataset_v1.1.0/della_calculator_products_v1.1.0.json,
        storefront crawl JSON (scratchpad, passed as argv[1])
Outputs: ../dataset_v1.2.0/  (JSON, Excel, Shopify CSV, logic doc is authored separately)
"""
import glob
import json
import math
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "dataset_v1.2.0")
os.makedirs(OUT, exist_ok=True)
CRAWL_DIR = sys.argv[1] if len(sys.argv) > 1 else None

NEW_VERSION = "1.2.0"
CLIMATE_VALUE_SOURCE = "della_series_mapping_v1"
CLIMATE_MAPPING_VERSION = "1.0.0"
LOCS = ["CA", "NJ", "SC", "TX"]

base = json.load(open(os.path.join(ROOT, "dataset_v1.1.0", "della_calculator_products_v1.1.0.json"), encoding="utf-8"))
climate_series = base["climate_series"]

df = pd.read_csv(os.path.join(ROOT, "products_export_1.csv"), low_memory=False)
inv = pd.read_csv(os.path.join(ROOT, "inventory_export_1.csv"), low_memory=False)

# storefront crawl: availability + images for the new products
store = {}
if CRAWL_DIR:
    for f in glob.glob(os.path.join(CRAWL_DIR, "products_p*.json")):
        for p in json.load(open(f)).get("products", []):
            store[p["handle"]] = p

# inventory pivot by SKU
inv_by_sku = defaultdict(lambda: {l: {"available": 0, "on_hand": 0} for l in LOCS})
for _, r in inv.iterrows():
    sku, loc = r["SKU"], r["Location"]
    if pd.isna(sku) or loc not in LOCS:
        continue
    inv_by_sku[sku][loc]["available"] += int(r["Available (not editable)"] or 0)
    inv_by_sku[sku][loc]["on_hand"] += int(r["On hand (current)"] or 0)

M = {
    "indoor_config": "Indoor Config (product.metafields.custom.indoor_config)",
    "series": "Series (product.metafields.custom.series)",
    "outdoor_btu": "Outdoor Capacity Btu (product.metafields.custom.outdoor_capacity_btu)",
    "seer2": "SEER2 (product.metafields.custom.seer2)",
    "refrigerant": "Refrigerant type (product.metafields.custom.refrigerant_type)",
    "unit_type": "Unit Type (product.metafields.custom.unit_type)",
}

UNIT_TYPE_MAP = {
    "Mini Split": "wall_mounted",
    "Ceiling Cassette Mini Split": "ceiling_cassette",
    "Concealed Ducted Mini Split": "concealed_ducted",
    "Floor Mounted Mini Split": "floor_mounted",
    "Ceiling Cassette": "ceiling_cassette",
    "Concealed Ducted": "concealed_ducted",
    "Wall Mount": "wall_mounted",
    "Wall Mounted": "wall_mounted",
}

def parse_heads(cfg):
    return sorted(int(float(x.strip().rstrip("Kk")) * 1000) for x in str(cfg).split("+"))

def parse_title_heads(title):
    m = re.search(r"[（(]\s*([0-9.]+[Kk](?:\s*\+\s*[0-9.]+[Kk])+)\s*[）)]", title)
    return parse_heads(m.group(1)) if m else None

def parse_sqft(title):
    m = re.search(r"Up to\s*([\d,]+)\s*Sq", title, re.I)
    return int(m.group(1).replace(",", "")) if m else None

existing = {p["handle"] for p in base["products"]}
h55 = [h for h in df[df["Handle"].str.contains("55000", na=False)]["Handle"].unique() if h not in existing]
assert len(h55) == 121, f"expected 121 new handles, got {len(h55)}"

new_products = []
issues = []
for handle in sorted(h55):
    rows = df[df["Handle"] == handle]
    head = rows.iloc[0]
    title = head["Title"]
    warnings = ["status_overridden_from_storefront", "heating_capacity_curve_unavailable", "voltage_check_product_page"]

    series = str(head[M["series"]]).strip()
    if series not in climate_series:
        issues.append((handle, f"series '{series}' not in climate mapping"))
        continue
    cl = climate_series[series]

    vec = parse_heads(head[M["indoor_config"]])
    tvec = parse_title_heads(title)
    if tvec and tvec != vec:
        warnings.append("head_config_title_mismatch")
        issues.append((handle, f"indoor_config {vec} != title {tvec}"))

    outdoor = int(float(head[M["outdoor_btu"]]))
    seer2 = None if pd.isna(head[M["seer2"]]) else float(head[M["seer2"]])
    if seer2 is None:
        warnings.append("seer2_missing")

    sp = store.get(handle)
    live_available = bool(sp and any(v.get("available") for v in sp["variants"]))
    image = sp["images"][0]["src"] if sp and sp.get("images") else None

    variants = []
    total_av = total_oh = 0
    any_inv_data = False
    vrows = rows[rows["Variant SKU"].notna()]
    for _, vr in vrows.iterrows():
        sku = vr["Variant SKU"]
        opts = {}
        for i in (1, 2, 3):
            n, v = vr.get(f"Option{i} Name"), vr.get(f"Option{i} Value")
            if pd.notna(n) and pd.notna(v) and str(n) != "Title":
                opts[str(n)] = str(v)
        if sku in inv_by_sku:
            any_inv_data = True
            by_loc = inv_by_sku[sku]
            av = sum(x["available"] for x in by_loc.values())
            oh = sum(x["on_hand"] for x in by_loc.values())
            variants.append({
                "sku": sku, "options": opts,
                "price": float(vr["Variant Price"]) if pd.notna(vr["Variant Price"]) else None,
                "compare_at_price": float(vr["Variant Compare At Price"]) if pd.notna(vr["Variant Compare At Price"]) else 0.0,
                "available_by_location": {l: by_loc[l]["available"] for l in LOCS},
                "on_hand_by_location": {l: by_loc[l]["on_hand"] for l in LOCS},
                "available_total": av, "on_hand_total": oh, "in_stock": av > 0,
                "inventory_source": "inventory_export",
            })
            total_av += av
            total_oh += oh
        else:
            variants.append({
                "sku": sku, "options": opts,
                "price": float(vr["Variant Price"]) if pd.notna(vr["Variant Price"]) else None,
                "compare_at_price": float(vr["Variant Compare At Price"]) if pd.notna(vr["Variant Compare At Price"]) else 0.0,
                "available_by_location": None, "on_hand_by_location": None,
                "available_total": None, "on_hand_total": None,
                "in_stock": live_available,
                "inventory_source": "storefront_available_flag",
            })
    if not any_inv_data:
        warnings.append("inventory_quantities_unavailable_at_snapshot")

    in_stock = (total_av > 0) if any_inv_data else live_available
    unit_raw = head[M["unit_type"]] if pd.notna(head[M["unit_type"]]) else head["Type"]
    unit_type = UNIT_TYPE_MAP.get(str(unit_raw).strip())
    if unit_type is None:
        issues.append((handle, f"unmapped unit type '{unit_raw}'"))
        continue

    adv_max = parse_sqft(title)
    new_products.append({
        "handle": handle,
        "title": title,
        "product_url": f"https://dellahome.com/products/{handle}",
        "featured_image_url": image,
        "source_product_type": head["Type"],
        "unit_type": unit_type,
        "system_type": "multi_zone",
        "zone_count": len(vec),
        "series": series,
        "capacity": {
            "nominal_btu": outdoor,
            "outdoor_capacity_btu": outdoor,
            "head_configuration_raw": str(head[M["indoor_config"]]),
            "head_vector_btu": vec,
            "head_vector_key": "-".join(str(v) for v in vec),
            "connected_head_total_btu": sum(vec),
            "connected_capacity_ratio": round(sum(vec) / outdoor, 4),
        },
        "coverage": {
            "advertised_sqft_min": 0,
            "advertised_sqft_max": adv_max,
            "source_label": f"0 - {adv_max}" if adv_max else None,
            "room_labels": [],
        },
        "climate": {
            "min_operating_temp_f": cl["min_temp_f"],
            "max_operating_temp_f": cl["max_temp_f"],
            "tier": cl["tier"],
            "heating_sizing_supported": False,
            "climate_value_source": CLIMATE_VALUE_SOURCE,
            "climate_mapping_version": CLIMATE_MAPPING_VERSION,
        },
        "efficiency": {"seer2": seer2, "refrigerant": str(head[M["refrigerant"]])},
        "electrical": {"known_voltage_values": [], "policy": "check_product_page"},
        "inventory": {
            "available_total": total_av if any_inv_data else None,
            "on_hand_total": total_oh if any_inv_data else None,
            "in_stock": in_stock,
            "locations": ({l: sum(inv_by_sku[v["sku"]][l]["available"] for v in variants if v["sku"] in inv_by_sku) for l in LOCS}
                          if any_inv_data else None),
            "inventory_source": "inventory_export" if any_inv_data else "storefront_available_flag",
        },
        "variants": variants,
        "calculator": {
            "eligible": True,
            "recommendable": True,
            "merchandising_priority": 50,
            "data_quality_score": 100,
            "warnings": warnings,
        },
    })

print(f"built {len(new_products)} new products; issues: {len(issues)}")
for h, msg in issues[:10]:
    print("  ISSUE:", h[:60], "->", msg)

# ---------------------------------------------------------------- merge
products = base["products"] + new_products
products.sort(key=lambda p: p["handle"])
handles = [p["handle"] for p in products]
assert len(handles) == len(set(handles)) == 438 + len(new_products)

indexes = {"by_system_type": defaultdict(list), "by_zone_count": defaultdict(list),
           "by_unit_type": defaultdict(list), "by_series": defaultdict(list),
           "by_climate_tier": defaultdict(list), "by_head_vector_key": defaultdict(list)}
for p in products:
    indexes["by_system_type"][p["system_type"]].append(p["handle"])
    indexes["by_zone_count"][str(p["zone_count"])].append(p["handle"])
    indexes["by_unit_type"][p["unit_type"]].append(p["handle"])
    indexes["by_series"][p["series"]].append(p["handle"])
    indexes["by_climate_tier"][p["climate"]["tier"]].append(p["handle"])
    indexes["by_head_vector_key"][p["capacity"]["head_vector_key"]].append(p["handle"])

meta = dict(base["metadata"])
meta.update({
    "dataset_version": NEW_VERSION,
    "source_dataset_version": "1.1.0",
    "regenerated_at_utc": datetime.now(timezone.utc).isoformat(),
    "eligible_product_count": len(products),
    "recommendable_product_count": sum(p["calculator"]["recommendable"] for p in products),
    "in_stock_product_count": sum(bool(p["inventory"]["in_stock"]) for p in products),
    "variant_count": sum(len(p["variants"]) for p in products),
    "excluded_handle_count": base["metadata"]["excluded_handle_count"] - len(new_products),
})
meta["migration_notes"] = base["metadata"].get("migration_notes", []) + [
    f"v1.2.0: added {len(new_products)} 55,000 BTU multi-zone products that the 2026-07-22 admin export "
    "recorded as draft but the same-day storefront crawl verified as published and purchasable "
    "(warning: status_overridden_from_storefront).",
    "Products lacking SKU rows in the inventory export carry inventory_source=storefront_available_flag "
    "with null quantity totals; live stock checks at result time are unaffected.",
]
dataset = {"metadata": meta, "climate_series": climate_series,
           "indexes": {k: dict(v) for k, v in indexes.items()}, "products": products}

out_json = os.path.join(OUT, f"della_calculator_products_v{NEW_VERSION}.json")
json.dump(dataset, open(out_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- Excel
xl11 = pd.ExcelFile(os.path.join(ROOT, "dataset_v1.1.0", "DELLA_Calculator_Product_Dataset_v1.1.0.xlsx"))

def product_row(p):
    c, cl2, e, calc, invn = p["capacity"], p["climate"], p["efficiency"], p["calculator"], p["inventory"]
    locs = invn["locations"] or {}
    return {
        "Handle": p["handle"], "Title": p["title"], "Recommendable": calc["recommendable"],
        "Unit Type": p["unit_type"], "System Type": p["system_type"], "Zone Count": p["zone_count"],
        "Series": p["series"], "Nominal BTU": c["nominal_btu"], "Outdoor BTU": c["outdoor_capacity_btu"],
        "Head Configuration": c["head_configuration_raw"], "Head Vector Key": c["head_vector_key"],
        "Connected Head Total BTU": c["connected_head_total_btu"], "Connected Capacity Ratio": c["connected_capacity_ratio"],
        "Climate Tier": cl2["tier"], "Min Temp F": cl2["min_operating_temp_f"], "Max Temp F": cl2["max_operating_temp_f"],
        "Climate Value Source": CLIMATE_VALUE_SOURCE, "Climate Mapping Version": CLIMATE_MAPPING_VERSION,
        "SEER2": e["seer2"], "Refrigerant": e["refrigerant"],
        "Advertised Sq Ft Min": p["coverage"]["advertised_sqft_min"], "Advertised Sq Ft Max": p["coverage"]["advertised_sqft_max"],
        "Available Total": invn["available_total"], "Available CA": locs.get("CA"), "Available NJ": locs.get("NJ"),
        "Available SC": locs.get("SC"), "Available TX": locs.get("TX"),
        "Merchandising Priority": calc["merchandising_priority"], "Data Quality": calc["data_quality_score"],
        "Warnings": "; ".join(calc["warnings"]), "In Stock (Snapshot)": bool(invn["in_stock"]),
        "Inventory Source": invn.get("inventory_source", "inventory_export"), "Product URL": p["product_url"],
    }

pf = pd.DataFrame([product_row(p) for p in products])

var_rows = []
for p in products:
    for v in p["variants"]:
        ab = v.get("available_by_location") or {}
        var_rows.append({
            "Handle": p["handle"], "Title": p["title"], "SKU": v["sku"],
            "Options JSON": json.dumps(v["options"]), "Price": v["price"], "Compare At Price": v["compare_at_price"],
            "Available CA": ab.get("CA"), "Available NJ": ab.get("NJ"), "Available SC": ab.get("SC"), "Available TX": ab.get("TX"),
            "Available Total": v["available_total"], "On Hand Total": v["on_hand_total"], "In Stock": bool(v["in_stock"]),
            "Inventory Source": v.get("inventory_source", "inventory_export"),
        })
variants_df = pd.DataFrame(var_rows)

mz = [p for p in products if p["system_type"] == "multi_zone"]
mzm = pd.DataFrame([{
    "Handle": p["handle"], "Title": p["title"], "Zone Count": p["zone_count"], "Series": p["series"],
    "Unit Type": p["unit_type"], "Outdoor BTU": p["capacity"]["outdoor_capacity_btu"],
    "Head Configuration": p["capacity"]["head_configuration_raw"],
    "Head Vector JSON": json.dumps(p["capacity"]["head_vector_btu"]), "Head Vector Key": p["capacity"]["head_vector_key"],
    "Connected Total BTU": p["capacity"]["connected_head_total_btu"], "Capacity Ratio": p["capacity"]["connected_capacity_ratio"],
    "Climate Tier": p["climate"]["tier"], "Available Total": p["inventory"]["available_total"],
    "Recommendable": p["calculator"]["recommendable"],
} for p in mz])

issues_df = pd.DataFrame([{
    "Handle": p["handle"], "Title": p["title"], "Series": p["series"], "System Type": p["system_type"],
    "Warnings": "; ".join(p["calculator"]["warnings"]), "Data Quality": p["calculator"]["data_quality_score"],
    "Recommendable": p["calculator"]["recommendable"],
} for p in products if p["calculator"]["warnings"]])

excluded = xl11.parse("Excluded Products")
excluded = excluded[~excluded["Handle"].isin({p["handle"] for p in new_products})]
climate_rules = xl11.parse("Climate Rules")
btu_rules = xl11.parse("BTU Rules")
btu_rules.loc[btu_rules["Rule"] == "Engine coefficients source", "Value"] = "calculator_config.json 1.1.0"
mfd = xl11.parse("Metafield Definitions")

summary = pd.DataFrame([
    [f"DELLA Calculator Product Dataset v{NEW_VERSION}", None, None, None, None, None],
    [f"Regenerated {datetime.now(timezone.utc).date().isoformat()}: v1.1.0 plus {len(new_products)} published 55K multi-zone systems", None, None, None, None, None],
    [None, None, None, None, None, None],
    ["Eligible Products", "Recommendable", "In Stock (Snapshot)", "Variants", "Single Zone", "Multi Zone"],
    [len(products), meta["recommendable_product_count"], meta["in_stock_product_count"], meta["variant_count"], 69, len(mz)],
    [None, None, None, None, None, None],
    ["Status of the added 121: draft in the admin export, published+available on the storefront the same day.", None, None, None, None, None],
    ["Their published state is storefront-verified (warning status_overridden_from_storefront).", None, None, None, None, None],
    ["93 of 121 lack inventory-export SKU rows; those use the storefront available flag (null totals).", None, None, None, None, None],
    ["Next admin export should confirm status and refresh quantities for the 121.", None, None, None, None, None],
])

out_xlsx = os.path.join(OUT, f"DELLA_Calculator_Product_Dataset_v{NEW_VERSION}.xlsx")
with pd.ExcelWriter(out_xlsx, engine="openpyxl") as w:
    summary.to_excel(w, sheet_name="Summary", header=False, index=False)
    pf.to_excel(w, sheet_name="Products Final", index=False)
    variants_df.to_excel(w, sheet_name="Variants Inventory", index=False)
    mzm.to_excel(w, sheet_name="Multi Zone Matrix", index=False)
    issues_df.to_excel(w, sheet_name="Data Issues", index=False)
    excluded.to_excel(w, sheet_name="Excluded Products", index=False)
    climate_rules.to_excel(w, sheet_name="Climate Rules", index=False)
    btu_rules.to_excel(w, sheet_name="BTU Rules", index=False)
    mfd.to_excel(w, sheet_name="Metafield Definitions", index=False)

# ---------------------------------------------------------------- Shopify CSV
def csv_bool(v):
    return "TRUE" if v else "FALSE"

csv_rows = []
for p in products:
    cap, cl2, e, calc = p["capacity"], p["climate"], p["efficiency"], p["calculator"]
    mzflag = p["system_type"] == "multi_zone"
    csv_rows.append({
        "Handle": p["handle"], "Title": p["title"],
        "Recommendable (product.metafields.calculator.recommendable)": csv_bool(calc["recommendable"]),
        "System Type (product.metafields.calculator.system_type)": p["system_type"],
        "Zone Count (product.metafields.calculator.zone_count)": p["zone_count"],
        "Unit Type (product.metafields.calculator.unit_type)": p["unit_type"],
        "Series (product.metafields.calculator.series)": p["series"],
        "Nominal BTU (product.metafields.calculator.nominal_btu)": cap["nominal_btu"],
        "Outdoor Capacity BTU (product.metafields.calculator.outdoor_capacity_btu)": cap["outdoor_capacity_btu"],
        "Head Configuration (product.metafields.calculator.head_configuration)": cap["head_configuration_raw"] or "",
        "Head Vector Key (product.metafields.calculator.head_vector_key)": cap["head_vector_key"],
        "Connected Head Total BTU (product.metafields.calculator.connected_head_total_btu)": cap["connected_head_total_btu"] if mzflag else "",
        "Connected Capacity Ratio (product.metafields.calculator.connected_capacity_ratio)": cap["connected_capacity_ratio"] if mzflag else "",
        "Climate Min F (product.metafields.calculator.climate_min_f)": cl2["min_operating_temp_f"],
        "Climate Max F (product.metafields.calculator.climate_max_f)": cl2["max_operating_temp_f"],
        "Climate Tier (product.metafields.calculator.climate_tier)": cl2["tier"],
        "SEER2 (product.metafields.calculator.seer2)": e["seer2"] if e["seer2"] is not None else "",
        "Refrigerant (product.metafields.calculator.refrigerant)": e["refrigerant"] or "",
        "Merchandising Priority (product.metafields.calculator.merchandising_priority)": calc["merchandising_priority"],
        "Data Quality Score (product.metafields.calculator.data_quality_score)": calc["data_quality_score"],
        "Voltage Policy (product.metafields.calculator.voltage_policy)": "check_product_page",
        "Heating Sizing Supported (product.metafields.calculator.heating_sizing_supported)": "FALSE",
    })
out_csv = os.path.join(OUT, f"Shopify_Calculator_Metafields_v{NEW_VERSION}.csv")
pd.DataFrame(csv_rows).to_csv(out_csv, index=False, encoding="utf-8-sig")

# ---------------------------------------------------------------- report
print("\n=== v1.2.0 reconciliation ===")
print("products:", len(products), "| recommendable:", meta["recommendable_product_count"],
      "| in-stock snapshot:", meta["in_stock_product_count"], "| variants:", meta["variant_count"])
print("handle sets identical:", set(handles) == set(pf["Handle"]) == {r["Handle"] for r in csv_rows})
print("multi-zone:", len(mz), "| unique vectors:", len(indexes["by_head_vector_key"]))
zc = defaultdict(int)
for p in mz:
    zc[p["zone_count"]] += 1
print("zone counts:", dict(sorted(zc.items())))
print("55K systems added:", len(new_products), "| with quantity data:", sum(1 for p in new_products if p["inventory"]["inventory_source"] == "inventory_export"))
print(f"\nwritten:\n  {out_json}\n  {out_xlsx}\n  {out_csv}")
