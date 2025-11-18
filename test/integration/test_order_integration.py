from src.order_io import load_order, write_receipt
from src.pricing import bulk_total, format_currency

def test_order_integration_basic(tmp_path):
    # 1) Create a small CSV order file
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    # 2) Read items and compute total
    items = load_order(input_file)          # -> list of (name, price_float)
    prices = [p for _, p in items]
    discount_percent = 10
    tax_rate = 0.10
    expected_total = bulk_total(prices, discount_percent, tax_rate)

    # 3) Write receipt
    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent, tax_rate)

    # 4) Verify receipt contents
    output_text = output_file.read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert f"TOTAL: {format_currency(expected_total)}" in output_text


def test_order_integration_rounding_and_spacing(tmp_path):
    # Prices chosen to exercise formatting/rounding in the final total
    input_file = tmp_path / "order.csv"
    input_file.write_text("thing,$1.05\nother,2.045\n", encoding="utf-8")

    items = load_order(input_file)
    prices = [p for _, p in items]
    discount_percent = 5     # small discount
    tax_rate = 0.07          # default-like tax rate

    expected_total = bulk_total(prices, discount_percent, tax_rate)
    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent, tax_rate)

    output_text = output_file.read_text(encoding="utf-8")
    # Each item line should appear as written by write_receipt
    assert "thing: $1.05" in output_text
    # 2.045 formatted should be $2.05 (to two decimals, rounded)
    assert "other: $2.05" in output_text
    # TOTAL line should be correctly formatted
    assert f"TOTAL: {format_currency(expected_total)}" in output_text
