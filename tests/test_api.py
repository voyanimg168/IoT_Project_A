import requests
from typing import Dict, Any

BASE_URL = "http://127.0.0.1:5000"
data_store: list[dict[str, Any]] = []
payload = Dict[str,Any]
# -----------------------------
# POSITIVE TEST CASES
# -----------------------------

def test_valid_temperature_data():
    payload: Dict[str, Any] = {
        "device_id": "sensor_1",
        "temperature": 25,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "accepted"


def test_boundary_low_temperature():
    payload: Dict[str, Any] = {
        "device_id": "sensor_2",
        "temperature": -50,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 200


def test_boundary_high_temperature():
    payload: Dict[str, Any] = {
        "device_id": "sensor_3",
        "temperature": 150,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 200


# -----------------------------
# NEGATIVE TEST CASES
# -----------------------------

def test_temperature_below_minimum():
    payload: Dict[str, Any] = {
        "device_id": "sensor_4",
        "temperature": -100,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 400


def test_temperature_above_maximum():
    payload: Dict[str, Any] = {
        "device_id": "sensor_5",
        "temperature": 200,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 400


def test_missing_device_id():
    payload: Dict[str, Any] = {
        "temperature": 25,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 400


def test_missing_temperature():
    payload = {
        "device_id": "sensor_6",
        "timestamp": "2026-04-29T10:00:00Z"
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 400


def test_invalid_json():
    response = requests.post(f"{BASE_URL}/data", data="not-a-json")
    assert response.status_code == 400


# -----------------------------
# FAILURE / EDGE CASE TESTS
# -----------------------------

def test_high_frequency_requests():
    payload: Dict[str, Any] = {
        "device_id": "sensor_load",
        "temperature": 30,
        "timestamp": "2026-04-29T10:00:00Z"
    }
    response = None
    for _ in range(50):
        response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response is not None
    assert response.status_code in [200, 429];


def test_random_null_values():
    payload = {
        "device_id": None,
        "temperature": None,
        "timestamp": None
    }

    response = requests.post(f"{BASE_URL}/data", json=payload)
    assert response.status_code == 400