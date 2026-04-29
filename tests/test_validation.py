import requests
from typing import Dict, Any

BASE = "http://127.0.0.1:5000"
data_store: list[dict[str, Any]] = []

def test_valid_data():
    payload: Dict[str,Any] = {
        "device_id": "sensor_1",
        "temperature": 25,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    r = requests.post(f"{BASE}/data", json=payload)
    assert r.status_code == 200

def test_missing_device():
    payload: Dict[str, Any] = {
        "temperature": 25,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    r = requests.post(f"{BASE}/data", json=payload)
    assert r.status_code == 400