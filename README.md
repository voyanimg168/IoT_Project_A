# 🚀 IoT Data Validation & Automation Testing Framework

## 📌 Overview

This project simulates a real-world **IoT data ingestion system** and demonstrates how automated testing ensures **data integrity, reliability, and robustness**.

It includes:

- A REST API for ingesting IoT sensor data
- A device simulator generating realistic and faulty inputs
- A comprehensive automated test suite using Pytest

The focus is on **QA automation and validation**, making this project highly relevant for **QA Engineer / SDET roles in IoT and backend systems**.

---

## 🏗️ Architecture

```
Device Simulator → API Server → Validation Layer → Response (200 / 400)
                         ↑
                     Pytest Suite
```

### Components

- **API Server (`src/api_server.py`)**
  - Accepts sensor data via HTTP POST
  - Validates payload structure and values
  - Returns appropriate status codes

- **Device Simulator (`src/device_simulator.py`)**
  - Simulates multiple IoT devices
  - Generates both valid and invalid data
  - Mimics real-world edge cases

- **Test Suite (`tests/`)**
  - Automated validation using Pytest
  - Covers functional, boundary, and negative scenarios

---

## 🧪 Test Coverage

The test suite includes **14 automated test cases**, covering:

### ✅ Functional Tests

- Valid sensor data ingestion
- Correct API responses (HTTP 200)

### ⚠️ Negative Tests

- Missing required fields
- Invalid JSON payloads
- Null values

### 📉 Boundary Tests

- Minimum temperature (-50°C)
- Maximum temperature (150°C)

### ❌ Failure Scenarios

- Out-of-range temperature values
- Invalid timestamp formats

### 🔁 Stress / Behavior Tests

- High-frequency requests
- Randomized invalid inputs

---

## 📊 Test Results

```
==================== 14 passed in 0.13s ====================
```

### Key Metrics

- ✔ **Total Tests:** 14
- ✔ **Pass Rate:** 100%
- ✔ **Execution Time:** 0.13 seconds
- ✔ **Throughput:** ~108 tests/second

### Interpretation

- The API correctly:
  - Accepts valid data (HTTP 200)
  - Rejects invalid data (HTTP 400)

- Validation rules are consistently enforced
- System behaves predictably under both normal and failure conditions

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd IoT-Project
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Start API Server

```bash
python src/api_server.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### Run Device Simulator

```bash
python src/device_simulator.py
```

This will generate continuous IoT-like traffic including:

- Valid sensor readings
- Invalid timestamps
- Out-of-range values

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

Optional:

```bash
pytest tests/ --tb=short
```

---

## 📂 Project Structure

```
IoT Project/
│
├── src/
│   ├── api_server.py
│   ├── device_simulator.py
│   └── utils.py
│
├── tests/
│   ├── test_api.py
│   ├── test_validation.py
│   └── test_failures.py
│
├── test_data/
│   ├── valid_data.json
│   └── invalid_data.json
│
├── docs/
│   ├── test_plan.md
│   ├── test_cases.md
│   └── test_results.md
│
├── logs/
│   └── test_results.log
│
├── requirements.txt
└── README.md
```

---

## 🎯 Key Skills Demonstrated

- ✅ API Testing (REST)
- ✅ Test Automation with Pytest
- ✅ Input Validation & Error Handling
- ✅ Boundary Value Analysis
- ✅ Negative Testing Strategies
- ✅ IoT Simulation & Data Modeling
- ✅ Debugging & Root Cause Analysis

---

## 🧠 Design Decisions

- **Strict validation layer**
  - Ensures only clean, structured data is accepted

- **Simulator-driven testing**
  - Mimics real-world unpredictable IoT environments

- **Fast test execution**
  - Suitable for CI/CD pipelines

---

## 🚧 Known Limitations

- Uses Flask development server (not production-grade)
- No authentication layer implemented
- Timestamp validation may reject loosely formatted ISO strings

---

## 🔮 Future Improvements

- Add authentication (API keys / JWT)
- Integrate CI/CD pipeline (GitHub Actions)
- Add performance/load testing (Locust, k6)
- Store valid data in database
- Add monitoring & logging dashboard

---

## 💬 How to Explain This Project (Interview Ready)

> “I built an IoT data ingestion system with an automated test suite that validates both valid and invalid device inputs.
> The tests cover functional, boundary, and failure scenarios, and all 14 test cases pass consistently.
> This demonstrates that the system enforces data integrity and behaves reliably under real-world conditions.”

---

## 📌 Conclusion

This project demonstrates how **QA automation ensures reliability in IoT systems**, where data quality is critical.
It showcases a practical approach to testing **real-time, unpredictable data pipelines**.

---
