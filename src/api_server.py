from flask import Flask, request, jsonify
from datetime import datetime
from typing import Dict, Any
# from src.utils import is_valid_temperature

app = Flask(__name__)

# Simple in-memory log (QA-friendly, no DB needed)
data_store: list[dict[str, Any]] = []

# -----------------------------
# Validation logic
# -----------------------------
def validate_payload(payload: Dict[str,Any]):
    required_fields = ["device_id", "temperature", "timestamp"]

    # Check missing fields
    for field in required_fields:
        if field not in payload or payload[field] is None:
            return False, f"Missing or null field: {field}"

    # Validate temperature range
    temp = payload["temperature"]
    if not isinstance(temp, (int, float)):
        return False, "Temperature must be numeric"

    if temp < -50 or temp > 150:
        return False, "Temperature out of valid range"

    # Validate timestamp format (basic ISO check)
    try:
        datetime.fromisoformat(payload["timestamp"].replace("Z", "+00:00"))
    except Exception:
        return False, "Invalid timestamp format"

    return True, "Valid"


# -----------------------------
# API endpoint
# -----------------------------
@app.route("/data", methods=["POST"])
def receive_data():
    try:
        payload = request.get_json(force=True)
        is_valid, message = validate_payload(payload)

        if not is_valid:
            return jsonify({
                "status": "rejected",
                "reason": message
            }), 400

        data_store.append(payload)

        return jsonify({
            "status": "accepted",
            "stored_count": len(data_store),
            "message": "Data stored successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400


# -----------------------------
# Health check
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200


if __name__ == "__main__":
    app.run(debug=True)

