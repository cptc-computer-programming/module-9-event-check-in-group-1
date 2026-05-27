"""Whole-flow tests for the completed Event Check-In Operations app.

These tests fail until the class integrates the approved team functions in
process_reservation().
"""

from app import process_reservation


def test_student_reservation_can_check_in():
    results = process_reservation(
        20,
        True,
        False,
        6,
        True,
        90,
        100,
        12,
        45,
        False,
    )

    assert results is not None
    assert results["ticket_rate"] == 12.00
    assert results["subtotal"] == 72.00
    assert round(results["discount"], 2) == 7.20
    assert round(results["service_fee"], 2) == 3.60
    assert results["capacity_percent"] == 90.0
    assert results["check_in_permission"] is True
    assert results["wait_minutes"] == 9
    assert results["lane"] == "Standard"
    assert round(results["quoted_amount"], 2) == 68.40
    assert results["status"] == "PAYMENT_REQUIRED"


def test_senior_reservation_is_denied_for_capacity():
    results = process_reservation(
        70,
        False,
        False,
        10,
        False,
        95,
        100,
        25,
        45,
        False,
    )

    assert results is not None
    assert results["ticket_rate"] == 10.00
    assert results["subtotal"] == 100.00
    assert round(results["discount"], 2) == 15.00
    assert round(results["service_fee"], 2) == 0.00
    assert results["capacity_percent"] == 95.0
    assert results["check_in_permission"] is False
    assert results["wait_minutes"] == 19
    assert results["lane"] == "Priority"
    assert round(results["quoted_amount"], 2) == 85.00
    assert results["status"] == "DENIED_CAPACITY"
