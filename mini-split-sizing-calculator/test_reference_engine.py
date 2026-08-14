import unittest

import reference_engine as eng


class SunroomAndLargeRoomRegressionTests(unittest.TestCase):
    def test_glass_heavy_sunroom_applies_one_fifteen_percent_adjustment(self):
        room = {
            "square_feet": 400,
            "ceiling_ft": 8,
            "glazing": "glass_heavy",
            "sunroom": True,
        }

        result = eng.room_load(room, "mixed")

        self.assertEqual(result["glazing_delta"], 0.15)
        self.assertEqual(result["point_load"], 9200.0)
        self.assertIn("sunroom", result["complexity_flags"])
        self.assertIn("glass_heavy", result["complexity_flags"])

    def test_large_warm_sunroom_requires_review_without_candidates(self):
        room = {
            "square_feet": 4000,
            "ceiling_ft": 12,
            "glazing": "glass_heavy",
            "sunroom": True,
        }
        fixture = eng.CLIMATE_FIXTURES["AZ-PHOENIX-85001"]

        load = eng.room_load(room, fixture["climate"])
        result = eng.single_zone_result(
            load["point_load"],
            load["lower_load"],
            load["upper_load"],
            fixture,
            room_area_sqft=room["square_feet"],
        )

        self.assertEqual(load["point_load"], 144900.0)
        self.assertEqual(result["bin"], "professional_review")
        self.assertEqual(result["rough_planning_load"], 145000)
        self.assertEqual(result["candidates"], [])
        self.assertEqual(result["fallback_reason"], "single_room_area_exceeds_review_threshold")


if __name__ == "__main__":
    unittest.main()
