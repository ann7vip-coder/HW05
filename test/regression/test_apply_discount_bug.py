from src.pricing import apply_discount

def test_apply_discount_regression():
    """
    Regression test for apply_discount() percentage bug.
    The bug: percent was treated as a raw fraction (10 → 1000%).
    Expected correct behavior: 10 means 10%.
    """
    result = apply_discount(100.0, 10)
    # The correct discounted price should be 90.0 (10% off)
    assert result == 90.0
