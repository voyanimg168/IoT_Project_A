import requests
import random
import time
from typing import Dict, Any
from datetime import datetime, timezone

API = "http://127.0.0.1:5000/data"


def generate(device: str) -> Dict[str, Any]:
    return {
        "device_id": device,
        "temperature": random.uniform(-70, 170),
        # "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    }


def run():
    devices = ["sensor_A", "sensor_B", "sensor_C"]

    for _ in range(20):
        for d in devices:
            payload = generate(d)

            # try:
            #     res = requests.post(API, json=payload)
            #     print(d, res.status_code, res.json())
            # except Exception as e:
            #     print("error:", e)

            try:
                res = requests.post(API, json=payload)
                print(d, res.status_code, res.json())
            except Exception as e:
                print("error:", e)

        time.sleep(1)

if __name__ == "__main__":
    run()