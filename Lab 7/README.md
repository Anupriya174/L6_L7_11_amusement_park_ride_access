
# L6_L7_11 — Amusement Park Ride Access

## Lab 7: Fuzz Testing with Hypothesis

## About

This lab explores property-based fuzz testing using Hypothesis to identify input validation bugs and improve the robustness of an amusement park ride access application.

The application contains three functions that process rider specifications, calculate ride dispatch throughput, and identify safety restraint types. Hypothesis generates a wide range of inputs to expose unexpected failures and edge cases.

## Functions Tested

| Function | Description |
|---|---|
| `validate_height_and_fastpass()` | Validates rider height and FastPass information. |
| `compute_dispatch_throughput()` | Calculates dispatch throughput from rider count and cycle time. |
| `resolve_safety_restraint_code()` | Identifies the safety restraint based on the ride zone code. |

## Files

| File | Description |
|---|---|
| `processor.py` | Application with improved input validation and error handling. |
| `test_processor.py` | Property-based fuzz tests implemented using Hypothesis. |

## Bugs Identified and Fixes

- Invalid and missing input values.
- Incorrect rider specification and throughput formats.
- Invalid height and FastPass values.
- Zero, negative, NaN, and infinite throughput values.
- Empty and unknown safety restraint codes.
- Unexpected input types such as `None`.

The application was updated to reject invalid inputs using meaningful `ValueError` messages.

## Technologies Used

- Python
- Hypothesis
- pytest

## How to Run

Install the required packages:

```bash
python -m pip install hypothesis pytest
```

Run the application:

```bash
python processor.py
```

Run the fuzz tests:

```bash
python -m pytest test_processor.py -v
```

## Test Results

All three Hypothesis test functions passed successfully after the application was updated.
