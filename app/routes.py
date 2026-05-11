from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({
        "project": "InfraGuard",
        "version": "1.0.0",
        "status": "running"
    })

@main.route("/api/info")
def info():
    return jsonify({
        "app": "InfraGuard DevSecOps Platform",
        "author": "Ahmad"
    })
