from flask import Blueprint, jsonify

health = Blueprint("health", __name__)

@health.route("/health")
def healthcheck():
    return jsonify({"status": "healthy"}), 200

@health.route("/ready")
def readiness():
    return jsonify({"status": "ready"}), 200
