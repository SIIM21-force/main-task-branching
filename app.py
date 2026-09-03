import os
import platform
from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify({
        "service": "DevOps Health & Monitoring API",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV","development"),
        "status": "operational"
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "uptime": "active",
    }), 200

@app.route("/system", methods=["GET"])
def system_info():
    return jsonify({
        "operating_system": platform.system(),
        "platform_release": platform.release(),
        "python_version": platform.python_version()
    }), 200

if __name__=="__main__":
    port=int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
