#!/usr/bin/env python3
"""Validate calculator_config.json against the PRD 9.3 contract.

Usage:
    python3 validate_calculator_config.py [config_path] [--dataset dataset_json_path]

Exit code 0 = valid, 1 = invalid. Prints every violation found.
This is the "equally explicit runtime validator" allowed by PRD 9.3.
The JavaScript engine must implement the same checks before initializing;
if any check fails the calculator must fail closed (no product
recommendations, neutral unavailable message, log the failure).
"""
import json
import re
import sys

ERRORS = []


def err(msg):
    ERRORS.append(msg)


def require(obj, path, keys):
    for k in keys:
        if k not in obj:
            err(f"missing required key: {path}.{k}")
    return all(k in obj for k in keys)


def num(obj, path, key, lo=None, hi=None, exclusive_lo=False):
    v = obj.get(key)
    if not isinstance(v, (int, float)) or isinstance(v, bool):
        err(f"{path}.{key} must be a number, got {type(v).__name__}")
        return None
    if lo is not None and (v <= lo if exclusive_lo else v < lo):
        err(f"{path}.{key}={v} below allowed minimum {lo}")
    if hi is not None and v > hi:
        err(f"{path}.{key}={v} above allowed maximum {hi}")
    return v


def main():
    args = sys.argv[1:]
    config_path = "calculator_config.json"
    dataset_path = None
    if args:
        if args[0] != "--dataset":
            config_path = args[0]
            args = args[1:]
        if len(args) == 2 and args[0] == "--dataset":
            dataset_path = args[1]

    try:
        with open(config_path, encoding="utf-8") as f:
            cfg = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL: cannot load {config_path}: {e}")
        return 1

    semver = re.compile(r"^\d+\.\d+\.\d+$")
    engine_re = re.compile(r"^della-sizing-engine-\d+\.\d+\.\d+$")

    require(cfg, "config", [
        "config_version", "engine_version", "compatible_engine_versions",
        "compatible_product_dataset_versions", "base_btu_per_sqft",
        "minimum_base_load_btu", "factors", "confidence_ranges",
        "capacity_bins_btu", "complexity_rules", "fallback_thresholds",
        "climate_margins", "ranking_weights", "merchandising",
        "display_policy", "input_validation",
    ])

    if not semver.match(str(cfg.get("config_version", ""))):
        err("config_version must be semver x.y.z")
    if not engine_re.match(str(cfg.get("engine_version", ""))):
        err("engine_version must match della-sizing-engine-x.y.z")
    if cfg.get("engine_version") not in cfg.get("compatible_engine_versions", []):
        err("engine_version must be listed in compatible_engine_versions")

    num(cfg, "config", "base_btu_per_sqft", lo=0, exclusive_lo=True)
    num(cfg, "config", "minimum_base_load_btu", lo=0, exclusive_lo=True)

    f = cfg.get("factors", {})
    if require(f, "factors", ["ceiling", "climate", "envelope", "sun", "internal_gains", "special_space"]):
        c = f["ceiling"]
        require(c, "factors.ceiling", ["mode", "reference_height_ft", "minimum", "maximum", "complexity_flag_above_ft"])
        if c.get("mode") != "average_height_divided_by_8":
            err("factors.ceiling.mode has unknown value")
        cmin = num(c, "factors.ceiling", "minimum", lo=0, exclusive_lo=True)
        cmax = num(c, "factors.ceiling", "maximum", lo=0, exclusive_lo=True)
        if cmin is not None and cmax is not None and cmin >= cmax:
            err("factors.ceiling minimum must be < maximum")

        cl = f["climate"]
        for k in ["cold", "marine", "mixed", "hot_dry", "hot_humid"]:
            num(cl, "factors.climate", k, lo=0, exclusive_lo=True)
        for k in cl:
            if k not in ["cold", "marine", "mixed", "hot_dry", "hot_humid"]:
                err(f"factors.climate contains unknown enum value: {k}")

        env = f["envelope"]
        require(env, "factors.envelope", ["minimum", "maximum", "insulation_delta", "airtightness_delta", "glazing_delta"])
        emin = num(env, "factors.envelope", "minimum", lo=0, exclusive_lo=True)
        emax = num(env, "factors.envelope", "maximum", lo=0, exclusive_lo=True)
        if emin is not None and emax is not None and emin >= emax:
            err("factors.envelope minimum must be < maximum")
        enums = {
            "insulation_delta": ["excellent", "good", "standard", "poor", "very_poor"],
            "airtightness_delta": ["very_tight", "average", "drafty", "very_drafty"],
            "glazing_delta": ["low", "average", "high", "glass_heavy"],
        }
        for group, keys in enums.items():
            g = env.get(group, {})
            if not isinstance(g, dict) or not g:
                err(f"factors.envelope.{group} must be a non-empty object (empty objects are not valid production values)")
                continue
            for k in keys:
                if k not in g:
                    err(f"factors.envelope.{group} missing enum value: {k}")
                elif not isinstance(g[k], (int, float)) or isinstance(g[k], bool):
                    err(f"factors.envelope.{group}.{k} must be a number")
            for k in g:
                if k not in keys:
                    err(f"factors.envelope.{group} contains unknown enum value: {k}")

        sun = f["sun"]
        for k in ["shaded", "average", "high_western"]:
            num(sun, "factors.sun", k, lo=0, exclusive_lo=True)
        for k in sun:
            if k not in ["shaded", "average", "high_western"]:
                err(f"factors.sun contains unknown enum value: {k}")

        ig = f["internal_gains"]
        require(ig, "factors.internal_gains", ["included_occupants", "extra_occupant_btu", "kitchen_btu", "watts_to_btu", "usage_factor"])
        num(ig, "factors.internal_gains", "extra_occupant_btu", lo=0)
        num(ig, "factors.internal_gains", "kitchen_btu", lo=0)
        num(ig, "factors.internal_gains", "watts_to_btu", lo=0, exclusive_lo=True)
        uf = ig.get("usage_factor", {})
        for k in ["continuous", "frequent", "intermittent"]:
            num(uf, "factors.internal_gains.usage_factor", k, lo=0, hi=1, exclusive_lo=True)
        for k in uf:
            if k not in ["continuous", "frequent", "intermittent"]:
                err(f"usage_factor contains unknown enum value: {k}")

        num(f["special_space"], "factors.special_space", "sunroom_minimum_glazing_delta", lo=0, hi=1)

    cr = cfg.get("confidence_ranges", {})
    for k in ["high", "medium", "low"]:
        num(cr, "confidence_ranges", k, lo=0, hi=1, exclusive_lo=True)
    if all(isinstance(cr.get(k), (int, float)) for k in ["high", "medium", "low"]):
        if not (cr["high"] <= cr["medium"] <= cr["low"]):
            err("confidence_ranges must satisfy high <= medium <= low")

    bins = cfg.get("capacity_bins_btu", [])
    if not isinstance(bins, list) or len(bins) < 2:
        err("capacity_bins_btu must be a list with at least 2 bins")
    else:
        if any(not isinstance(b, int) or b <= 0 for b in bins):
            err("capacity_bins_btu entries must be positive integers")
        if bins != sorted(bins):
            err("capacity_bins_btu must be sorted ascending")
        if len(set(bins)) != len(bins):
            err("capacity_bins_btu must not contain duplicates")

    rules = cfg.get("complexity_rules", {})
    if require(rules, "complexity_rules", [
        "standard_max_rooms", "advanced_min_rooms", "absolute_max_rooms",
        "single_room_review_area_sqft", "single_zone_automatic_max_btu",
        "multi_room_review_total_btu", "small_load_review_btu", "ceiling_review_above_ft",
    ]):
        for k in rules:
            num(rules, "complexity_rules", k, lo=0, exclusive_lo=True)
        if rules["standard_max_rooms"] >= rules["advanced_min_rooms"]:
            err("standard_max_rooms must be < advanced_min_rooms")
        if rules["advanced_min_rooms"] > rules["absolute_max_rooms"]:
            err("advanced_min_rooms must be <= absolute_max_rooms")
        if bins and isinstance(bins[-1], int) and rules.get("single_zone_automatic_max_btu") != bins[-1]:
            err("single_zone_automatic_max_btu must equal the largest capacity bin")

    fb = cfg.get("fallback_thresholds", {})
    if require(fb, "fallback_thresholds", ["preferred_min_capacity_ratio", "preferred_max_capacity_ratio", "conditional_max_capacity_ratio"]):
        if not (1.0 <= fb["preferred_min_capacity_ratio"] <= fb["preferred_max_capacity_ratio"] <= fb["conditional_max_capacity_ratio"]):
            err("fallback ratios must satisfy 1.0 <= preferred_min <= preferred_max <= conditional_max")

    for k in ["winter_safety_margin_f", "summer_safety_margin_f"]:
        num(cfg.get("climate_margins", {}), "climate_margins", k, lo=0)

    rw = cfg.get("ranking_weights", {})
    if require(rw, "ranking_weights", ["capacity_fit", "zone_or_head_match", "climate_fit", "inventory", "efficiency"]):
        total = sum(v for v in rw.values() if isinstance(v, (int, float)))
        if total != 100:
            err(f"ranking_weights must total 100, got {total}")

    m = cfg.get("merchandising", {})
    if require(m, "merchandising", ["default_merchandising_priority", "allowed_roles"]):
        num(m, "merchandising", "default_merchandising_priority", lo=0, hi=100)
        allowed = {"best_match", "higher_efficiency", "value_choice", "cold_climate_upgrade"}
        for role in m.get("allowed_roles", []):
            if role not in allowed:
                err(f"merchandising.allowed_roles contains unknown role: {role}")

    dp = cfg.get("display_policy", {})
    require(dp, "display_policy", ["maximum_product_cards", "mobile_cards_per_row", "allow_dynamic_roles", "load_rounding_increment_btu", "review_load_rounding_increment_btu"])
    num(dp, "display_policy", "maximum_product_cards", lo=1, hi=8)
    num(dp, "display_policy", "load_rounding_increment_btu", lo=1)
    num(dp, "display_policy", "review_load_rounding_increment_btu", lo=1000)
    if "allow_dynamic_roles" in dp and not isinstance(dp["allow_dynamic_roles"], bool):
        err("display_policy.allow_dynamic_roles must be boolean")

    iv = cfg.get("input_validation", {})
    require(iv, "input_validation", [
        "minimum_area_sqft", "confirm_area_above_sqft", "minimum_ceiling_ft",
        "maximum_ceiling_ft", "confirm_occupants_above", "maximum_occupants",
        "confirm_equipment_watts_above", "maximum_equipment_watts", "zip_code_pattern",
    ])
    if "zip_code_pattern" in iv:
        try:
            re.compile(iv["zip_code_pattern"])
        except re.error:
            err("input_validation.zip_code_pattern is not a valid regex")

    if dataset_path:
        try:
            with open(dataset_path, encoding="utf-8") as fdata:
                ds = json.load(fdata)
            dv = ds.get("metadata", {}).get("dataset_version")
            if dv not in cfg.get("compatible_product_dataset_versions", []):
                err(f"product dataset version {dv} is not in compatible_product_dataset_versions")
        except (OSError, json.JSONDecodeError) as e:
            err(f"cannot load dataset {dataset_path}: {e}")

    if ERRORS:
        print(f"FAIL: {len(ERRORS)} violation(s) in {config_path}")
        for e in ERRORS:
            print(f"  - {e}")
        return 1
    print(f"PASS: {config_path} satisfies the PRD 9.3 contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
