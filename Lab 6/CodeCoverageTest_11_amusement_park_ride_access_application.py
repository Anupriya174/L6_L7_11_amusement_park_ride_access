
import pytest
from amusement_park_ride_access import (
    process_ride_admissions,
    inspect_safety_restraints
)


def test_invalid_groups():
    with pytest.raises(ValueError):
        process_ride_admissions("invalid", 5.0)


def test_negative_express_fee():
    with pytest.raises(ValueError):
        process_ride_admissions([], -5.0)


def test_closed_and_unknown_rides():
    groups = [
        {"is_open": False, "ride_type": "family"},
        {"is_open": True, "ride_type": "unknown"}
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0


def test_all_ride_types_and_fast_lane():
    groups = [
        {
            "is_open": True,
            "ride_type": "roller_coaster",
            "has_fast_lane": True,
            "patrons": [
                {"height_cm": 150, "is_child": False}
            ]
        },
        {
            "is_open": True,
            "ride_type": "water_ride",
            "patrons": [
                {"height_cm": 130, "is_child": True}
            ]
        },
        {
            "is_open": True,
            "ride_type": "family",
            "patrons": [
                {"height_cm": 150, "is_child": False}
            ]
        }
    ]

    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 50.8
    assert result["status"] == "COMPLETED"


def test_patron_rejections_and_health_warning():
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "patrons": [
                {"height_cm": 0},
                {"height_cm": 100},
                {"height_cm": 150, "health_warning": True},
                {"height_cm": 150, "is_child": True}
            ]
        }
    ]

    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 6.0


def test_roller_coaster_health_warning():
    groups = [
        {
            "is_open": True,
            "ride_type": "roller_coaster",
            "has_fast_lane": True,
            "patrons": [
                {"height_cm": 150, "health_warning": True},
                {"height_cm": 150}
            ]
        }
    ]

    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 5.0


def test_safety_audit():
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "patrons": [
                {"height_cm": 0},
                {"height_cm": 0},
                {"height_cm": 0},
                {"height_cm": 0},
                {"height_cm": 0}
            ]
        }
    ]

    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "SAFETY_AUDIT"


def test_zero_admissions():
    result = process_ride_admissions([], 5.0)
    assert result["status"] == "ZERO_ADMISSIONS"


def test_no_restraint_data():
    assert inspect_safety_restraints([]) == "NO_DATA"


def test_emergency_lock():
    assert inspect_safety_restraints([[1, 0, 0]]) == "EMERGENCY_LOCK"


def test_safe_restraints_and_streak_reset():
    assert inspect_safety_restraints([[0, 1, 0, 1]]) == "SAFE"
