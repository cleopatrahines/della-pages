#!/usr/bin/env python3
"""Build the DELLA ZIP-to-climate dataset v1.0.0.

Sources:
1. DOE/PNNL Building America county climate assignments (climate_zones.csv):
   county FIPS -> IECC zone, moisture regime, BA climate zone.
2. Census 2020 ZCTA-to-county relationship file (tab20_zcta520_county20_natl.txt):
   each ZCTA is assigned the county with the largest overlapping land area.

Design temperatures are DELLA Engine V1 policy approximations keyed by
IECC zone + moisture regime (documented in the legend). They are NOT
ASHRAE-licensed station data; the engine's summer +3F / winter -5F safety
margins are calibrated for this coarseness. Replace with licensed data in a
future dataset version if station-level precision is ever needed.

Output: ../climate_dataset_v1.0.0/della_zip_climate_v1.0.0.json
Record format (compact): "zip": "6A" style zone code. The legend maps each
zone code to climate_type, winter_design_temp_f, summer_design_temp_f.
A 3-digit-prefix majority table provides the deterministic fallback for
ZIP codes that are not ZCTAs (PO boxes, unique ZIPs).

Usage: python3 build_zip_climate_v1_0_0.py <dir with climate_zones.csv and zcta_county.txt>
"""
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

SRC = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "climate_dataset_v1.0.0")
os.makedirs(OUT, exist_ok=True)

BA_TO_TYPE = {
    "Hot-Humid": "hot_humid",
    "Hot-Dry": "hot_dry",
    "Mixed-Humid": "mixed",
    "Mixed-Dry": "mixed",
    "Marine": "marine",
    "Cold": "cold",
    "Very Cold": "cold",
    "Subarctic": "cold",
}

# DELLA Engine V1 policy design temperatures by IECC zone + moisture regime.
# winter = approx 99% heating design F, summer = approx 1% cooling design F.
DESIGN = {
    "1A": (46, 91), "2A": (30, 93), "2B": (34, 106),
    "3A": (22, 94), "3B": (30, 102), "3C": (34, 83),
    "4A": (12, 91), "4B": (18, 96), "4C": (24, 85),
    "5A": (0, 89), "5B": (2, 93), "5C": (22, 82),
    "6A": (-10, 87), "6B": (-8, 90),
    "7": (-18, 84), "8": (-35, 78),
}

county = {}
with open(os.path.join(SRC, "climate_zones.csv"), encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        fips = r["State FIPS"].zfill(2) + r["County FIPS"].zfill(3)
        zone = r["IECC Climate Zone"].strip()
        moist = r["IECC Moisture Regime"].strip()
        code = zone if zone in ("7", "8") else zone + (moist if moist and moist != "N/A" else "A")
        if code not in DESIGN:
            code = {"5N": "5A"}.get(code, code)
        ba = r["BA Climate Zone"].strip()
        county[fips] = {"code": code, "type": BA_TO_TYPE[ba], "state": r["State"]}

# ZCTA -> dominant county by land overlap
best = {}
with open(os.path.join(SRC, "zcta_county.txt"), encoding="utf-8-sig") as f:
    rd = csv.DictReader(f, delimiter="|")
    for r in rd:
        z = r["GEOID_ZCTA5_20"].strip()
        c = r["GEOID_COUNTY_20"].strip()
        if not z or not c or c not in county:
            continue
        area = int(r["AREALAND_PART"] or 0)
        if z not in best or area > best[z][1]:
            best[z] = (c, area)

zips = {}
for z, (c, _a) in best.items():
    info = county[c]
    zips[z] = info["code"] + ":" + {"hot_humid": "HH", "hot_dry": "HD", "mixed": "MX",
                                    "marine": "MR", "cold": "CD"}[info["type"]]

# 3-digit prefix majority fallback
prefix = {}
byp = defaultdict(Counter)
for z, v in zips.items():
    byp[z[:3]][v] += 1
for p, cnt in byp.items():
    prefix[p] = cnt.most_common(1)[0][0]

legend = {}
for code, (w, s) in DESIGN.items():
    legend[code] = {"winter_design_temp_f": w, "summer_design_temp_f": s}

dataset = {
    "metadata": {
        "name": "DELLA ZIP Climate Dataset",
        "dataset_version": "1.0.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "record_format": "zip -> '<IECC zone code>:<climate type code>'; resolve temps via legend.zones, type via legend.types",
        "sources": [
            "DOE/PNNL Building America county climate assignments (climate_zones.csv)",
            "US Census 2020 ZCTA-to-county relationship file; dominant county by land overlap",
        ],
        "design_temp_provenance": "DELLA Engine V1 policy approximations by IECC zone+moisture; not ASHRAE station data. Engine climate margins (+3F summer / -5F winter) account for this coarseness.",
        "fallback_rule": "exact zip -> prefix3 majority -> null (manual region selection, PRD 14.5)",
        "zip_count": len(zips),
        "prefix_count": len(prefix),
    },
    "legend": {
        "types": {"HH": "hot_humid", "HD": "hot_dry", "MX": "mixed", "MR": "marine", "CD": "cold"},
        "zones": legend,
    },
    "zips": dict(sorted(zips.items())),
    "prefix3_fallback": dict(sorted(prefix.items())),
}

out = os.path.join(OUT, "della_zip_climate_v1.0.0.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, separators=(",", ":"))

print(f"zips: {len(zips)}  prefixes: {len(prefix)}  bytes: {os.path.getsize(out):,}")
tc = Counter(v.split(":")[1] for v in zips.values())
print("type distribution:", dict(tc))
for probe in ["33101", "43215", "40202", "55411", "58102", "85001", "98101", "79901", "95130", "10001", "60601", "77002", "02108"]:
    v = dataset["zips"].get(probe) or dataset["prefix3_fallback"].get(probe[:3])
    src = "exact" if probe in dataset["zips"] else "prefix"
    if v:
        code, t = v.split(":")
        lg = legend[code]
        print(f"  {probe}: {code} {dataset['legend']['types'][t]:>9}  winter {lg['winter_design_temp_f']:>4}F summer {lg['summer_design_temp_f']}F  ({src})")
    else:
        print(f"  {probe}: NOT FOUND")
