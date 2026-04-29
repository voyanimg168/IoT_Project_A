# Test Plan - IoT QA Framework

## Objective
Validate IoT data pipeline reliability using automated QA testing.

---

## Scope
- API validation
- Data integrity checks
- Failure simulation
- Edge case handling

---

## Test Types

### 1. Functional Testing
- Valid sensor data ingestion
- API response correctness

### 2. Negative Testing
- Missing fields
- Invalid temperature range
- Corrupted payloads

### 3. Edge Case Testing
- Boundary values (-50, 150)
- High frequency requests
- Null values

---

## Tools
- Python
- Pytest
- Requests

---

## Entry Criteria
- API server running
- Dependencies installed

## Exit Criteria
- All critical tests passed
- No unhandled exceptions