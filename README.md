# Ticket Validator

A Python package that reads AMC/service tickets from a CSV file and validates each ticket using Pydantic.

## Features
- Validates ticket data using Pydantic models.
- Reads ticket records from CSV files.
- Identifies valid and invalid records.
- Handles missing fields, invalid dates, and invalid values.
- Uses Python logging to display validation results.
- Includes automated tests using pytest.

## Project Structure
```text
ticket-validator/
├── src/
│   └── tickets/
│       ├── __init__.py
│       ├── models.py
│       ├── loader.py
│       └── validator.py
├── tests/
│   └── test_tickets.py
├── data/
│   └── tickets.csv
├── reports/
│   └── test-report.txt
└── README.md
```

## Requirements
- Python 3.12+
- Pydantic
- Pytest

## Installation
```bash
uv sync
```

## Run the Validator
```bash
uv run python -m tickets.validator
```

## Run Tests
```bash
uv run pytest -v
```

## Test Results
All 5 test cases pass:
- Valid ticket
- Missing required field
- Invalid date
- Invalid enum value
- Empty CSV

## Validation Output

The validator logs the number of valid and invalid tickets.
Invalid records include the row number and validation error.

Test reports are saved in the reports folder.