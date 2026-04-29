import requests
from typing import Dict, Any

BASE = "http://127.0.0.1:5000"
data_store: list[dict[str, Any]] = []

def test_invalid_temp_low():
    payload: Dict[str, Any] = {
        "device_id": "sensor_x",
        "temperature": -999,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    r = requests.post(f"{BASE}/data", json=payload)
    assert r.status_code == 400


def test_invalid_temp_high():
    payload: Dict[str, Any] = {
        "device_id": "sensor_x",
        "temperature": 999,
        "timestamp": "2026-04-29T10:00:00Z"
    }

    r = requests.post(f"{BASE}/data", json=payload)
    assert r.status_code == 400