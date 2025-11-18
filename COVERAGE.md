## Summary
- **Command:** `pytest --cov=src --cov-report=term-missing`
- **Overall coverage:** [e.g., 92%]
- **Per-file:**
  - `src/pricing.py`: [e.g., 94%]
  - `src/order_io.py`: [e.g., 88%]
  - (others…)

## Uncovered Lines / Functions
Copy from pytest-cov’s “missing” column (line numbers) and note what they are:

- `src/pricing.py`: lines [e.g., 78–80] — error/edge path in `parse_price` for malformed commas  
- `src/order_io.py`: line [e.g., 45] — exception branch when the output path is unwritable

## Analysis: Which gaps are acceptable?
- **Acceptable:**  
  - Rare OS/file I/O failures (e.g., permission errors) that are hard to simulate portably.  
- **Should improve:**  
  - Validation/edge cases in `parse_price` (malformed commas, empty string)  
  - Error branches in `add_tax` (negative rate) and `apply_discount` (negative percent)  
  - `bulk_total` behavior on corner inputs (empty list)

## Improvements made (after initial run)
- Added/expanded tests to cover:
  - `apply_discount` negative percent raises (regression + branch coverage)
  - `add_tax` negative rate raises
  - `parse_price` invalid inputs (“”, “abc”, “$12,34,56”)
  - `bulk_total` with empty list and rounding check

_Re-run results:_  
- Overall coverage increased from **[before]%** → **[after]%**  
- `src/pricing.py` increased from **[before]%** → **[after]%**  
- Remaining acceptable gaps: [briefly restate above]
