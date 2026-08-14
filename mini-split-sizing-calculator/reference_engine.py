#!/usr/bin/env python3
"""Reference implementation of della-sizing-engine-1.1.0.

Purpose: deterministic oracle for Calculator_Test_Cases.xlsx and, later, for
verifying the production JavaScript engine. Implements PRD sections 9-17 on
top of calculator_config.json and the frozen v1.1.0 product dataset.

Sub-score formulas inside ranking (capacity-fit shape, SEER2 normalization)
are reference-engine policy v1 where the PRD leaves the detail open; they are
documented in the Versions sheet of the workbook and must be mirrored or
consciously replaced (with re-approval) by the production engine.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

with open(os.path.join(HERE, "calculator_config.json"), encoding="utf-8") as f:
    CFG = json.load(f)
with open(os.path.join(ROOT, "dataset_v1.2.0", "della_calculator_products_v1.2.0.json"), encoding="utf-8") as f:
    DATASET = json.load(f)

PRODUCTS = DATASET["products"]

# Frozen climate fixtures (fixture-1.0.0). Design temperatures are test
# fixtures pending the approved ZIP/climate dataset (PRD 28.1); they are NOT
# production data.
# Frozen copies of records from della_zip_climate_v1.0.0.json (exact-zip hits,
# except AZ-PHOENIX-85001 which exercises the prefix3 fallback path).
CLIMATE_FIXTURES = {
    "FL-MIAMI-33101":       {"zip": "33101", "climate": "hot_humid", "summer_design_temp_f": 91,  "winter_design_temp_f": 46},
    "KY-LOUISVILLE-40202":  {"zip": "40202", "climate": "mixed",     "summer_design_temp_f": 91,  "winter_design_temp_f": 12},
    "MN-MINNEAPOLIS-55411": {"zip": "55411", "climate": "cold",      "summer_design_temp_f": 87,  "winter_design_temp_f": -10},
    "ND-FARGO-58102":       {"zip": "58102", "climate": "cold",      "summer_design_temp_f": 84,  "winter_design_temp_f": -18},
    "AZ-PHOENIX-85001":     {"zip": "85001", "climate": "hot_dry",   "summer_design_temp_f": 106, "winter_design_temp_f": 34},
    "WA-SEATTLE-98101":     {"zip": "98101", "climate": "marine",    "summer_design_temp_f": 85,  "winter_design_temp_f": 24},
    "TX-ELPASO-79901":      {"zip": "79901", "climate": "hot_dry",   "summer_design_temp_f": 102, "winter_design_temp_f": 30},
    "ZIP-LOOKUP-FAIL":      {"zip": "00000", "climate": None,        "summer_design_temp_f": None, "winter_design_temp_f": None,
                             "manual_region_fallback": "mixed"},
}
CLIMATE_FIXTURE_VERSION = "1.0.0 (della_zip_climate)"


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def round_display(v):
    inc = CFG["display_policy"]["load_rounding_increment_btu"]
    return int(round(v / inc) * inc)


def round_review_display(v):
    inc = CFG["display_policy"]["review_load_rounding_increment_btu"]
    return int(round(v / inc) * inc)


def room_load(room, climate_type):
    """PRD 9.4-9.9. Returns the full factor breakdown."""
    f = CFG["factors"]
    area = room["square_feet"]
    base = max(CFG["minimum_base_load_btu"], area * CFG["base_btu_per_sqft"])

    ceil_cfg = f["ceiling"]
    ceiling_factor = clamp(room["ceiling_ft"] / ceil_cfg["reference_height_ft"],
                           ceil_cfg["minimum"], ceil_cfg["maximum"])
    climate_factor = f["climate"][climate_type]

    env = f["envelope"]
    ins = env["insulation_delta"][room.get("insulation", "standard")]
    air = env["airtightness_delta"][room.get("airtightness", "average")]
    glz = env["glazing_delta"][room.get("glazing", "average")]
    if room.get("sunroom"):
        glz = max(glz, f["special_space"]["sunroom_minimum_glazing_delta"])
    envelope_factor = clamp(1 + ins + air + glz, env["minimum"], env["maximum"])

    sun_factor = f["sun"][room.get("sun", "average")]

    ig = f["internal_gains"]
    people = max(0, room.get("occupants", 2) - ig["included_occupants"]) * ig["extra_occupant_btu"]
    kitchen = ig["kitchen_btu"] if room.get("kitchen") else 0
    watts = room.get("equipment_watts", 0)
    usage = ig["usage_factor"][room.get("equipment_usage", "intermittent")] if watts else 0
    equipment = watts * ig["watts_to_btu"] * usage

    point = base * ceiling_factor * climate_factor * envelope_factor * sun_factor + people + kitchen + equipment

    flags = []
    if room.get("sunroom"):
        flags.append("sunroom")
    if room["ceiling_ft"] > CFG["complexity_rules"]["ceiling_review_above_ft"]:
        flags.append("ceiling_over_12ft")
    if area > CFG["complexity_rules"]["single_room_review_area_sqft"]:
        flags.append("large_open_space")
    if room.get("glazing") == "glass_heavy":
        flags.append("glass_heavy")
    if room.get("garage_frequent_door"):
        flags.append("garage_frequent_door")
    if room.get("open_stairs"):
        flags.append("open_stairs")
    if room.get("irregular"):
        flags.append("irregular_plan")

    defaulted = room.get("defaulted_fields", [])
    if flags:
        confidence = "low"
    elif defaulted:
        confidence = "medium"
    else:
        confidence = "high"
    band = CFG["confidence_ranges"][confidence]

    return {
        "base_load": base,
        "ceiling_factor": round(ceiling_factor, 4),
        "climate_factor": climate_factor,
        "insulation_delta": ins,
        "airtightness_delta": air,
        "glazing_delta": glz,
        "envelope_factor": round(envelope_factor, 4),
        "sun_factor": sun_factor,
        "people_gain": people,
        "kitchen_gain": kitchen,
        "equipment_gain": round(equipment, 1),
        "point_load": round(point, 1),
        "lower_load": round(point * (1 - band), 1),
        "upper_load": round(point * (1 + band), 1),
        "confidence": confidence,
        "complexity_flags": flags,
        "defaulted_fields": defaulted,
    }


def capacity_bin(point):
    """PRD 11.1 consumer path label."""
    if point > CFG["complexity_rules"]["single_zone_automatic_max_btu"]:
        return "above_automatic_range"
    if point < CFG["complexity_rules"]["small_load_review_btu"]:
        return "below_9k_minimum"
    for b in CFG["capacity_bins_btu"]:
        if point <= b:
            return f"{b // 1000}K"
    return "above_automatic_range"


def climate_ok(product, fixture, heating_intent):
    cl = product["climate"]
    if fixture.get("summer_design_temp_f") is None:
        return True  # manual-region path: no design-temp confirmation (PRD 14.5)
    if cl["max_operating_temp_f"] < fixture["summer_design_temp_f"] + CFG["climate_margins"]["summer_safety_margin_f"]:
        return False
    if heating_intent == "primary":
        if cl["min_operating_temp_f"] > fixture["winter_design_temp_f"] - CFG["climate_margins"]["winter_safety_margin_f"]:
            return False
    return True


def single_zone_candidates(point, lower, upper, fixture, heating_intent="cooling", unit_type="wall_mounted"):
    """Eligible Product Layer + Engine Candidate Layer for one room."""
    preferred_max = CFG["fallback_thresholds"]["preferred_max_capacity_ratio"]
    conditional_max = CFG["fallback_thresholds"]["conditional_max_capacity_ratio"]
    w = CFG["ranking_weights"]
    candidates, rejected = [], []
    for p in PRODUCTS:
        reasons = []
        if p["system_type"] != "single_zone":
            continue  # not enumerated as rejections to keep output bounded
        if not p["calculator"]["recommendable"]:
            reasons.append("not_recommendable")
        if not p["inventory"]["in_stock"]:
            reasons.append("out_of_stock_snapshot")
        if unit_type and p["unit_type"] != unit_type:
            reasons.append("unit_type_mismatch")
        if not climate_ok(p, fixture, heating_intent):
            reasons.append("climate_range_insufficient")
        cap = p["capacity"]["nominal_btu"]
        ratio = cap / point
        if cap < point:
            reasons.append("below_point_load")
        elif ratio > conditional_max:
            reasons.append("capacity_ratio_exceeds_conditional_max")
        if reasons:
            rejected.append({"handle": p["handle"], "nominal_btu": cap, "reasons": reasons})
            continue
        status = "preferred" if ratio <= preferred_max else "acceptable_step_up"
        cap_fit = clamp(1 - (ratio - 1) / (conditional_max - 1), 0, 1)
        seer2 = p["efficiency"]["seer2"] or 0
        score = (w["capacity_fit"] * cap_fit
                 + w["zone_or_head_match"] * 1
                 + w["climate_fit"] * 1
                 + w["inventory"] * 1
                 + w["efficiency"] * clamp(seer2 / 25.0, 0, 1))
        candidates.append({
            "handle": p["handle"], "nominal_btu": cap, "series": p["series"],
            "seer2": seer2, "capacity_fit_ratio": round(ratio, 4),
            "capacity_fit_status": status, "engine_score": round(score, 2),
            "merchandising_priority": p["calculator"]["merchandising_priority"],
        })
    candidates.sort(key=lambda c: (-c["engine_score"], -c["merchandising_priority"], c["handle"]))
    return candidates, rejected


def assign_roles(candidates):
    """Merchandising Presentation Layer (PRD 17.3), reference policy.

    No-forced-upgrade rule (PRD experience principle 7): best_match is the
    highest-scoring candidate from the mildest climate tier that qualified.
    More cold-capable candidates become cold_climate_upgrade, not the default.
    Proxy for tier: min_operating_temp (higher = milder series).
    """
    roles = {}
    if not candidates:
        return roles
    by_handle = {c["handle"]: c for c in candidates}
    products = {p["handle"]: p for p in PRODUCTS}
    def min_f(c):
        return products[c["handle"]]["climate"]["min_operating_temp_f"]
    mildest = max(min_f(c) for c in candidates)
    best = next(c for c in candidates if min_f(c) == mildest)
    roles[best["handle"]] = "best_match"
    hi_eff = next((c for c in candidates if c["handle"] not in roles and c["seer2"] > best["seer2"]), None)
    if hi_eff:
        roles[hi_eff["handle"]] = "higher_efficiency"
    cold = next((c for c in candidates if c["handle"] not in roles and min_f(c) < min_f(best)), None)
    if cold:
        roles[cold["handle"]] = "cold_climate_upgrade"
    return roles


def single_zone_result(point, lower, upper, fixture, heating_intent="cooling",
                       unit_type="wall_mounted", room_area_sqft=None):
    """Fallback Matrix application for a single room (PRD 17.4)."""
    bin_label = capacity_bin(point)
    out = {"bin": bin_label, "borderline": False, "fallback_level": None,
           "fallback_reason": "", "candidates": [], "rejected": []}
    if (room_area_sqft is not None
            and room_area_sqft > CFG["complexity_rules"]["single_room_review_area_sqft"]):
        out["bin"] = "professional_review"
        out["fallback_level"] = 5
        out["fallback_reason"] = "single_room_area_exceeds_review_threshold"
        out["rough_planning_load"] = round_review_display(point)
        return out
    if bin_label == "above_automatic_range":
        out["fallback_level"] = 5
        out["fallback_reason"] = "point_load_above_single_zone_automatic_max"
        return out
    candidates, rejected = single_zone_candidates(point, lower, upper, fixture, heating_intent, unit_type)
    out["candidates"], out["rejected"] = candidates, rejected

    crosses = any(lower <= b < upper for b in CFG["capacity_bins_btu"])
    smaller_inside_range = any(
        r["nominal_btu"] < point and r["nominal_btu"] >= lower
        for r in rejected if "below_point_load" in r["reasons"]
    )
    if bin_label == "below_9k_minimum":
        # Informational path (PRD 11.4): show smallest option, never a
        # confirmed match. Not a numbered fallback level.
        out["fallback_level"] = None
        out["fallback_reason"] = "below_smallest_della_capacity"
        out["borderline"] = True
        return out
    if candidates:
        best = candidates[0]
        if best["capacity_fit_status"] == "preferred" and not crosses:
            out["fallback_level"] = 1
        else:
            out["fallback_level"] = 3 if best["capacity_fit_status"] == "acceptable_step_up" else 1
            out["borderline"] = crosses or best["capacity_fit_status"] == "acceptable_step_up"
        if upper > CFG["complexity_rules"]["single_zone_automatic_max_btu"]:
            out["borderline"] = True
    else:
        out["borderline"] = smaller_inside_range or crosses
        out["fallback_level"] = 5
        climate_only_blocked = any(
            set(r["reasons"]) == {"climate_range_insufficient"} for r in rejected
        )
        if climate_only_blocked:
            out["fallback_reason"] = "no_climate_qualified_candidate_backup_heat_review"
        else:
            out["fallback_reason"] = "no_candidate_within_conditional_ratio" + \
                ("_smaller_product_inside_range" if smaller_inside_range else "")
    return out


def head_for_room(point):
    """PRD 13.1: round each room to its indoor-head recommendation (9K minimum, locked)."""
    for b in CFG["capacity_bins_btu"][:-1]:  # 36K heads do not exist in bundles
        if point <= b:
            return b
    return None  # room too large for any published bundle head


def multi_room_result(rooms_points, fixture, heating_intent="cooling"):
    heads = [head_for_room(p) for p in rooms_points]
    out = {"heads": heads, "vector_key": None, "exact_matches": [],
           "fallback_level": None, "fallback_reason": ""}
    total = sum(rooms_points)
    if any(h is None for h in heads):
        out["fallback_level"] = 4
        out["fallback_reason"] = "room_load_exceeds_largest_bundle_head"
        return out
    if total > CFG["complexity_rules"]["multi_room_review_total_btu"]:
        out["fallback_level"] = 4
        out["fallback_reason"] = "total_load_exceeds_review_threshold_split_recommended"
        return out
    key = "-".join(str(h) for h in sorted(heads))
    out["vector_key"] = key
    matches = [p for p in PRODUCTS
               if p["system_type"] == "multi_zone"
               and p["calculator"]["recommendable"]
               and p["inventory"]["in_stock"]
               and p["capacity"]["head_vector_key"] == key
               and climate_ok(p, fixture, heating_intent)]
    matches.sort(key=lambda p: (-(p["efficiency"]["seer2"] or 0), p["handle"]))
    out["exact_matches"] = [p["handle"] for p in matches]
    if matches:
        out["fallback_level"] = 1
    else:
        any_vector = any(p["capacity"]["head_vector_key"] == key for p in PRODUCTS
                         if p["system_type"] == "multi_zone")
        out["fallback_level"] = 4
        out["fallback_reason"] = ("bundle_exists_but_fails_climate_or_stock"
                                  if any_vector else "no_published_bundle_for_vector")
    return out
