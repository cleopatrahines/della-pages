#!/usr/bin/env python3
"""Generate Calculator_Test_Cases.xlsx (PRD section 26).

Expected values are computed by reference_engine.py against
calculator_config.json and the frozen product dataset, never written
from intuition (PRD 26.3). Failure-mode cases carry behavioral expectations
instead of computed loads.
"""
import json
import os

import pandas as pd

import reference_engine as eng

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Calculator_Test_Cases.xlsx")

R = dict  # room shorthand

PROHIBIT_ALWAYS = "Manual J result; exact load; code-compliant; guaranteed coverage; guaranteed heating at extreme temperature; confirmed electrical compatibility"
VOLTAGE_COPY = "Voltage varies by model. Confirm electrical requirements on the product page before purchasing."
DISCLAIMER = "pre-purchase sizing estimate ... does not replace a professional Manual J calculation"

CASES = [
    # --- standard ---
    dict(id="TC-STD-01", cat="standard", fixture="FL-MIAMI-33101", intent="cooling",
         rooms=[R(square_feet=300, ceiling_ft=8)],
         purpose="PRD 26.2 required: Florida hot-humid small bedroom; below-7K path",
         required_copy="Estimated requirement: below 9,000 BTU; Smallest DELLA option: 9,000 BTU",
         prohibited_copy="confirmed match for 9K; unconditional Serena assertion"),
    dict(id="TC-STD-02", cat="standard", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=450, ceiling_ft=8)],
         purpose="Exact 9K boundary; preferred ratio 1.00; High confidence",
         required_copy="Why This Size explanation; " + VOLTAGE_COPY),
    dict(id="TC-STD-03", cat="standard", fixture="MN-MINNEAPOLIS-55411", intent="primary",
         rooms=[R(square_feet=700, ceiling_ft=9)],
         purpose="PRD 26.2 required: Minnesota very-cold living room (point 14,175). Verified frozen-data outcome: winter -11F needs min temp <= -16F, so only Optima Pro qualifies on climate, but its 18K unit is 1.27x the load (over the 1.25 limit) and the 17K unit is an Econo. No safe candidate exists: Support Review (L5), sizing preserved. Optima Pro appears only via climate rules, never as an unconditional expectation",
         required_copy="Suitable for your climate range",
         prohibited_copy="fully sized to heat; heating capacity guarantee"),
    # --- boundary ---
    dict(id="TC-BND-04", cat="boundary", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=600, ceiling_ft=8)], purpose="Exact 12K boundary"),
    dict(id="TC-BND-05", cat="boundary", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=900, ceiling_ft=8)], purpose="Exact 18K boundary"),
    dict(id="TC-BND-06", cat="boundary", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=1200, ceiling_ft=8)], purpose="Exact 24K boundary"),
    dict(id="TC-BND-07", cat="boundary", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=1440, ceiling_ft=10)],
         purpose="Exact 36K via ceiling factor; upper estimate exceeds 36K so result is 36K Borderline (PRD 11.5)",
         required_copy="36K Borderline; professional review recommended",
         prohibited_copy="Confirmed Match on any 36K product"),
    dict(id="TC-BND-08", cat="boundary", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=460, ceiling_ft=8)],
         purpose="Just above 9K: bin label is 12K but nearest real capacity (9.8K) is the preferred match; bin label must not override actual capacity match (PRD 11.1)"),
    dict(id="TC-BND-09", cat="boundary", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=575, ceiling_ft=8, airtightness="average", glazing="average",
                  defaulted_fields=["airtightness", "glazing"])],
         purpose="Medium confidence via defaults; range crosses the 12K bin edge; borderline dual-path (PRD 11.3)",
         required_copy="two explained capacity paths"),
    # --- fallback / catalog gaps ---
    dict(id="TC-FBK-10", cat="fallback", fixture="TX-ELPASO-79901", intent="cooling",
         rooms=[R(square_feet=650, ceiling_ft=8)],
         purpose="Conditional step-up accepted just below the 1.25 limit (17K on 13,650 load = 1.245)",
         required_copy="Capacity step-up due to available equipment sizes"),
    dict(id="TC-FBK-11", cat="fallback", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=650, ceiling_ft=8)],
         purpose="Catalog gap 12,001-13,599: no product inside 1.25; smaller 12K sits inside the estimated range so result is borderline dual-path, never silent oversizing",
         prohibited_copy="automatic 17K/18K recommendation as confirmed match"),
    dict(id="TC-FBK-12", cat="fallback", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=1300, ceiling_ft=8)],
         purpose="Catalog gap 24,001-27,999: 35K exceeds 1.25; 24K inside range; borderline dual-path or review"),
    # --- complex spaces ---
    dict(id="TC-CPX-13", cat="complex", fixture="WA-SEATTLE-98101", intent="cooling",
         rooms=[R(square_feet=400, ceiling_ft=8, glazing="glass_heavy", sunroom=True)],
         purpose="Glass-heavy + Sunroom regression: effective glazing delta remains +15% (single adjustment, no duplicate multiplier); Low confidence, +/-25%, review message (PRD 12)",
         required_copy="solar gain can be materially higher than in a standard room"),
    dict(id="TC-CPX-14", cat="complex", fixture="TX-ELPASO-79901", intent="cooling",
         rooms=[R(square_feet=500, ceiling_ft=9, insulation="poor", garage_frequent_door=True)],
         purpose="Garage with frequent door opening: Low confidence, wider range"),
    dict(id="TC-CPX-15", cat="complex", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=800, ceiling_ft=13)],
         purpose="Ceiling over 12 ft: factor clamps at 1.50, provisional result, Low confidence, no unique confirmed product"),
    dict(id="TC-CPX-16", cat="complex", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=2000, ceiling_ft=8)],
         purpose="PRD 26.2 required: 2,000 sq ft open room; area threshold takes priority over capacity matching",
         required_copy="Professional review required; Low confidence; not an equipment-sizing recommendation; room-by-room Manual J calculation",
         prohibited_copy="recommended equipment capacity; Find Matching Products; any confirmed capacity recommendation"),
    dict(id="TC-CPX-35", cat="complex", fixture="AZ-PHOENIX-85001", intent="cooling",
         rooms=[R(square_feet=4000, ceiling_ft=12, glazing="glass_heavy", sunroom=True)],
         purpose="Large warm-climate sunroom regression: raw planning load 144,900 BTU/h because Glass-heavy and Sunroom apply one +15% glazing adjustment; area threshold forces review before equipment matching",
         required_copy="Professional review required; Rough planning load: approximately 145,000 BTU/h; Low confidence; not an equipment-sizing recommendation",
         prohibited_copy="166,600 BTU/h; recommended equipment capacity; Find Matching Products; specific DELLA equipment recommendation"),
    dict(id="TC-CPX-17", cat="complex", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=400, ceiling_ft=8, equipment_watts=5000, equipment_usage="continuous")],
         purpose="Extreme equipment wattage: exceeds confirm threshold (3,000W) so UI requires confirmation; load lands in the 24-28K catalog gap",
         required_copy="confirmation prompt for unusually high equipment wattage"),
    # --- climate ---
    dict(id="TC-CLM-18", cat="climate", fixture="ND-FARGO-58102", intent="primary",
         rooms=[R(square_feet=600, ceiling_ft=8)],
         purpose="Winter design -18F needs min temp <= -23F; below the most cold-capable series: professional review + backup heat discussion, no sizing claim (PRD 14.3)",
         required_copy="professional review; backup heat discussion",
         prohibited_copy="suitable for your climate range; any heating-capacity claim"),
    dict(id="TC-CLM-19", cat="climate", fixture="AZ-PHOENIX-85001", intent="cooling",
         rooms=[R(square_feet=550, ceiling_ft=8)],
         purpose="Summer margin check: 108F + 3F = 111F; all series max temps qualify; normal result"),
    dict(id="TC-CLM-20", cat="climate", fixture="MN-MINNEAPOLIS-55411", intent="primary",
         rooms=[R(square_feet=600, ceiling_ft=8)],
         purpose="12K-class load with primary heating in cold climate: only Optima Pro (min -22F) passes the -16F requirement and a 12K Optima Pro wall unit exists in stock, so the result is a clean L1 with a climate-filtered candidate set; verifies no milder series leaks in"),
    # --- multi-room ---
    dict(id="TC-MR-21", cat="multi_room", fixture="FL-MIAMI-33101", intent="cooling",
         rooms=[R(square_feet=300, ceiling_ft=8), R(square_feet=450, ceiling_ft=8)],
         purpose="2-room exact bundle: heads 9K+12K, published vector in stock"),
    dict(id="TC-MR-22", cat="multi_room", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=450, ceiling_ft=8), R(square_feet=450, ceiling_ft=8),
                R(square_feet=550, ceiling_ft=8), R(square_feet=600, ceiling_ft=8)],
         purpose="4-room Standard-path exact bundle: 9-9-12-12"),
    dict(id="TC-MR-23", cat="multi_room", fixture="ND-FARGO-58102", intent="primary",
         rooms=[R(square_feet=300, ceiling_ft=8), R(square_feet=450, ceiling_ft=8)],
         purpose="Bundle exists but fails climate: vector 9000-9000 is published and in stock, but Fargo primary heating (-18F, needs min <= -23F) disqualifies every series. Alternative System Architecture / support; climate must never trigger a capacity change",
         prohibited_copy="invented bundle; diversity-factor sizing; capacity upsizing due to climate"),
    dict(id="TC-MR-24", cat="multi_room", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=450, ceiling_ft=8)] * 4 + [R(square_feet=550, ceiling_ft=8)],
         purpose="Fifth room triggers Advanced acknowledgement (PRD 8.5); 5-room vector 9-9-9-9-12 exists in stock",
         required_copy="Advanced-project prompt on adding the fifth room"),
    dict(id="TC-MR-25", cat="multi_room", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=450, ceiling_ft=8)] * 6,
         purpose="6-room project, heads 9K x 6 = 54K total: within the 55K threshold (config 1.1.0) and matched by live 55K six-zone systems (dataset 1.2.0). Under the previous 48K rule this case was a guaranteed split; it now verifies the fifth-room Advanced prompt plus a real 6-zone exact match",
         required_copy="Advanced-project prompt acknowledged before rooms five and six"),
    dict(id="TC-MR-26", cat="multi_room", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=1200, ceiling_ft=8)] * 3,
         purpose="Total load 72K exceeds the 55K threshold: split-system paths and support review (PRD 13.3)"),
    dict(id="TC-MR-34", cat="multi_room", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=900, ceiling_ft=8)] * 3,
         purpose="18K x 3 = 54K total: sits in the 48-55K window that the old rule rejected; must now match live 55K bundles (vector 18000-18000-18000). Regression guard for the threshold change"),
    dict(id="TC-MR-27", cat="multi_room", fixture="KY-LOUISVILLE-40202", intent="cooling",
         rooms=[R(square_feet=500, ceiling_ft=8), R(square_feet=1400, ceiling_ft=8)],
         purpose="Room load above 24K in a multi-room project: no published bundle head exists above 24K; multiple-system architecture required"),
    # --- flow / failure ---
    dict(id="TC-FLW-28", cat="flow", fixture="ZIP-LOOKUP-FAIL", intent="cooling",
         rooms=[R(square_feet=500, ceiling_ft=8, defaulted_fields=["climate_region_manual"])],
         purpose="ZIP lookup failure: manual climate-region fallback; products shown without climate-confirmed labels (PRD 14.5)",
         required_copy="neutral climate-review message",
         prohibited_copy="climate-confirmed match"),
    dict(id="TC-ERR-29", cat="failure", fixture=None, intent=None, rooms=None,
         purpose="Missing required configuration key (e.g. capacity_bins_btu): engine fails closed; neutral unavailable message; no product recommendations; validation failure logged (PRD 9.3)",
         behavior="fail_closed"),
    dict(id="TC-ERR-30", cat="failure", fixture=None, intent=None, rooms=None,
         purpose="Unsorted capacity bins in config: validator rejects; engine does not initialize",
         behavior="fail_closed"),
    dict(id="TC-ERR-31", cat="failure", fixture=None, intent=None, rooms=None,
         purpose="Engine/config version incompatibility: engine_version not in compatible_engine_versions; fail closed",
         behavior="fail_closed"),
    dict(id="TC-ERR-32", cat="failure", fixture=None, intent=None, rooms=None,
         purpose="Product catalog request failure: room-load calculation still works; result shows sizing plus collection/support fallback, never generic bestsellers (PRD 22)",
         behavior="degraded_sizing_only",
         required_copy="sizing result preserved; collection/support fallback",
         prohibited_copy="generic bestsellers grid"),
    dict(id="TC-ERR-33", cat="failure", fixture=None, intent=None, rooms=None,
         purpose="Seventh room attempt: rejected at UI level; absolute_max_rooms = 6; engine never called",
         behavior="ui_rejected"),
]


def defaults_of(room):
    return room.get("defaulted_fields", [])


def main():
    test_rows, calc_rows, cand_rows, rej_rows, copy_rows = [], [], [], [], []

    for case in CASES:
        cid = case["id"]
        fixture = eng.CLIMATE_FIXTURES.get(case["fixture"]) if case["fixture"] else None
        expected_status = case.get("behavior", "")
        room_results = []
        mr = None

        if case["rooms"]:
            climate_type = (fixture["climate"] or fixture.get("manual_region_fallback"))
            for i, room in enumerate(case["rooms"], 1):
                res = eng.room_load(room, climate_type)
                room_results.append((i, room, res))
                calc_rows.append({
                    "case_id": cid, "room": i,
                    "base_load": res["base_load"],
                    "ceiling_factor": res["ceiling_factor"],
                    "climate_factor": res["climate_factor"],
                    "insulation_delta": res["insulation_delta"],
                    "airtightness_delta": res["airtightness_delta"],
                    "glazing_delta": res["glazing_delta"],
                    "envelope_factor": res["envelope_factor"],
                    "sun_factor": res["sun_factor"],
                    "people_gain": res["people_gain"],
                    "kitchen_gain": res["kitchen_gain"],
                    "equipment_gain": res["equipment_gain"],
                    "point_load": res["point_load"],
                    "lower_load": res["lower_load"],
                    "upper_load": res["upper_load"],
                    "display_point_load": eng.round_display(res["point_load"]),
                    "display_lower_load": eng.round_display(res["lower_load"]),
                    "display_upper_load": eng.round_display(res["upper_load"]),
                    "confidence": res["confidence"],
                    "capacity_bin": eng.capacity_bin(res["point_load"]),
                    "complexity_flags": ";".join(res["complexity_flags"]),
                    "defaulted_fields": ";".join(res["defaulted_fields"]),
                })

            if len(case["rooms"]) == 1:
                _, room, res = room_results[0]
                sz = eng.single_zone_result(res["point_load"], res["lower_load"],
                                            res["upper_load"], fixture,
                                            heating_intent=case["intent"],
                                            room_area_sqft=room["square_feet"])
                expected_status = sz["bin"]
                if sz["borderline"]:
                    expected_status += " (borderline)"
                fb = sz["fallback_level"]
                roles = eng.assign_roles(sz["candidates"])
                for rank, c in enumerate(sz["candidates"][:5], 1):
                    cand_rows.append({
                        "case_id": cid, "rank": rank, "handle": c["handle"],
                        "nominal_btu": c["nominal_btu"], "series": c["series"],
                        "seer2": c["seer2"], "capacity_fit_ratio": c["capacity_fit_ratio"],
                        "capacity_fit_status": c["capacity_fit_status"],
                        "engine_score": c["engine_score"],
                        "expected_role": roles.get(c["handle"], ""),
                    })
                point = res["point_load"]
                for r in sorted(sz["rejected"], key=lambda r: abs(r["nominal_btu"] - point))[:8]:
                    rej_rows.append({"case_id": cid, "handle": r["handle"],
                                     "nominal_btu": r["nominal_btu"],
                                     "rejection_reasons": ";".join(r["reasons"])})
                fallback = fb if fb is not None else "below_min_info"
                fallback_reason = sz["fallback_reason"]
            else:
                points = [r[2]["point_load"] for r in room_results]
                mr = eng.multi_room_result(points, fixture, heating_intent=case["intent"])
                expected_status = f"multi_room vector={mr['vector_key'] or 'n/a'}"
                fallback = mr["fallback_level"]
                fallback_reason = mr["fallback_reason"]
                for rank, h in enumerate(mr["exact_matches"][:5], 1):
                    cand_rows.append({"case_id": cid, "rank": rank, "handle": h,
                                      "nominal_btu": "", "series": "", "seer2": "",
                                      "capacity_fit_ratio": "", "capacity_fit_status": "exact_bundle",
                                      "engine_score": "", "expected_role": "best_match" if rank == 1 else ""})
        else:
            fallback = ""
            fallback_reason = case.get("behavior", "")

        test_rows.append({
            "case_id": cid,
            "case_category": case["cat"],
            "project_type": ("multi_room" if case["rooms"] and len(case["rooms"]) > 1
                             else "one_room" if case["rooms"] else "n/a"),
            "room_count": len(case["rooms"]) if case["rooms"] else 0,
            "zip_or_climate_fixture": case["fixture"] or "n/a",
            "climate_type": (fixture["climate"] if fixture else ""),
            "summer_design_temp_f": (fixture["summer_design_temp_f"] if fixture else ""),
            "winter_design_temp_f": (fixture["winter_design_temp_f"] if fixture else ""),
            "primary_heating_intent": case["intent"] or "",
            "room_inputs_json": json.dumps(case["rooms"]) if case["rooms"] else "",
            "defaulted_fields": ";".join(sorted({d for r in (case["rooms"] or []) for d in defaults_of(r)})),
            "scenario_purpose": case["purpose"],
            "expected_status": expected_status,
            "expected_fallback_level": fallback,
            "expected_fallback_reason": fallback_reason,
        })

        copy_rows.append({
            "case_id": cid,
            "required_copy": case.get("required_copy", "") + ("; " + DISCLAIMER if case["rooms"] else ""),
            "prohibited_copy": (case.get("prohibited_copy", "") + "; " + PROHIBIT_ALWAYS).lstrip("; "),
        })

    versions = pd.DataFrame([
        {"key": "engine_version", "value": eng.CFG["engine_version"]},
        {"key": "config_version", "value": eng.CFG["config_version"] + " (calculator_config.json)"},
        {"key": "product_dataset_version", "value": "1.2.0 (della_calculator_products_v1.2.0.json, frozen snapshot incl. inventory/prices; 121 products carry storefront-verified status)"},
        {"key": "climate_dataset_version", "value": eng.CLIMATE_FIXTURE_VERSION + " — fixtures are frozen records from climate_dataset_v1.0.0/della_zip_climate_v1.0.0.json"},
        {"key": "climate_mapping_version", "value": "1.0.0 (della_series_mapping_v1)"},
        {"key": "reference_policy_note_1", "value": "capacity_fit sub-score = 1 - (ratio-1)/0.25 clamped to 0..1; SEER2 normalized by fixed 25.0"},
        {"key": "reference_policy_note_2", "value": "Tie-break: engine_score desc, merchandising_priority desc, handle asc. best_match = highest-scoring candidate from the mildest qualifying series tier (no forced upgrade, PRD principle 7); colder-capable candidates become cold_climate_upgrade"},
        {"key": "reference_policy_note_3", "value": "Candidate tests use the frozen snapshot; live price/stock behavior needs separate integration tests (PRD 26.1)"},
        {"key": "governance", "value": "Expected values computed by reference_engine.py; golden cases still require human HVAC/product approval before launch (PRD 26.3)"},
    ])

    with pd.ExcelWriter(OUT, engine="openpyxl") as w:
        pd.DataFrame(test_rows).to_excel(w, sheet_name="Test Cases", index=False)
        pd.DataFrame(calc_rows).to_excel(w, sheet_name="Expected Calculation", index=False)
        pd.DataFrame(cand_rows).to_excel(w, sheet_name="Expected Candidates", index=False)
        pd.DataFrame(rej_rows).to_excel(w, sheet_name="Rejected Candidates", index=False)
        pd.DataFrame(copy_rows).to_excel(w, sheet_name="Copy Assertions", index=False)
        versions.to_excel(w, sheet_name="Versions", index=False)

    print(f"written {OUT}")
    print(f"cases: {len(test_rows)}  calc rows: {len(calc_rows)}  candidate rows: {len(cand_rows)}  rejected rows: {len(rej_rows)}")
    for t in test_rows:
        print(f"{t['case_id']:>10}  {t['expected_status']:<40} fb={t['expected_fallback_level']} {t['expected_fallback_reason']}")


if __name__ == "__main__":
    main()
