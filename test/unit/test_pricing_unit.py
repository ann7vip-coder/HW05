import pytest
from src.pricing import (
    parse_price,
    format_currency,
    apply_discount,
    add_tax,
    bulk_total,
)

# -----------------------------
# parse_price
# -----------------------------
@pytest.mark.parametrize("text, expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    (" $0.99 ", 0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == pytest.approx(expected, rel=1e-12)

@pytest.mark.parametrize("text", [
    "",           # empty string
    "abc",        # non-numeric
    "$12,34,56",  # malformed comma placement (should be invalid per spec)
])
def test_parse_price_invalid(text):
    with pytest.raises(Exception):
        parse_price(text)

# -----------------------------
# format_currency (rounding/format)
# -----------------------------
@pytest.mark.parametrize("value, expected", [
    (0, "$0.00"),
    (12, "$12.00"),
    (12.5, "$12.50"),
    (12.345, "$12.35"),  # verify rounding to 2 decimals
    (-3.1, "$-3.10"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected

# -----------------------------
# apply_discount (0%, large %, negative raises)
# -----------------------------
@pytest.mark.parametrize("price, percent, expected", [
    (100.0, 0, 100.0),    # 0% → no change
    (200.0, 90, 20.0),    # large % → big reduction
])
def test_apply_discount_basic(price, percent, expected):
    assert apply_discount(price, percent) == pytest.approx(expected, rel=1e-12)

def test_apply_discount_negative_raises():
    with pytest.raises(ValueError):
        apply_discount(100.0, -5)

# -----------------------------
# add_tax (default/custom, negative raises)
# -----------------------------
def test_add_tax_default():
    # default rate is 7%
    assert add_tax(100.0) == pytest.approx(107.0, rel=1e-12)

def test_add_tax_custom():
    assert add_tax(100.0, 0.10) == pytest.approx(110.0, rel=1e-12)

def test_add_tax_negative_raises():
    with pytest.raises(ValueError):
        add_tax(50.0, -0.01)

# -----------------------------
# bulk_total (simple list)
# -----------------------------
def test_bulk_total_simple_list():
    prices = [10, 20, 30]  # subtotal = 60
    # 10% discount → 54; then +7% tax → 57.78
    total = bulk_total(prices, discount_percent=10, tax_rate=0.07)
    assert total == pytest.approx(57.78, rel=1e-12)
