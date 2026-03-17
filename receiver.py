"""
receiver.py — Raspberry Pi Remote Command Receiver
Day 7 Mission: The Remote Command Center

Listens for messages and commands sent from the Replit dashboard,
then prints them to the Pi's terminal in style.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ─── ASCII banner so you know it's running ───────────────────────────────────
BANNER = """
╔══════════════════════════════════════════════╗
║   🍓  PI RECEIVER  —  ONLINE & LISTENING    ║
║   Waiting for commands from the cloud...    ║
╚══════════════════════════════════════════════╝
"""

# ─── Route 1: Health check ────────────────────────────────────────────────────
@app.route("/ping", methods=["GET"])
def ping():
    """Replit dashboard uses this to confirm the Pi is alive."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"\n[{timestamp}] 📡 SYSTEM CHECK received from dashboard")
    print(f"  → Pi status: ALL SYSTEMS GO 🟢\n")
    return jsonify({
        "status": "online",
        "message": "Pi is alive and listening!",
        "timestamp": timestamp
    })


# ─── Route 2: Message of the Day ─────────────────────────────────────────────
@app.route("/message", methods=["POST"])
def receive_message():
    """Receives a message from the Replit dashboard and prints it big."""
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message field in request"}), 400

    msg = data["message"]
    sender = data.get("sender", "Dashboard")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print it dramatically to the terminal
    print("\n" + "═" * 50)
    print(f"  📨  MESSAGE RECEIVED  —  {timestamp}")
    print(f"  From : {sender}")
    print(f"  Text : {msg}")
    print("═" * 50 + "\n")

    return jsonify({
        "status": "delivered",
        "received": msg,
        "timestamp": timestamp
    })


# ─── Route 3: Run a canned system command ────────────────────────────────────
@app.route("/system", methods=["GET"])
def system_info():
    """Returns basic Pi system info when 'Check System' is pressed."""
    import subprocess

    timestamp = datetime.now().strftime("%H:%M:%S")

    # Grab CPU temp (Pi-specific) and uptime safely
    try:
        temp_raw = subprocess.check_output(
            ["vcgencmd", "measure_temp"], text=True
        ).strip()          # e.g. "temp=42.8'C"
        temp = temp_raw.replace("temp=", "")
    except Exception:
        temp = "N/A (vcgencmd not found)"

    try:
        uptime_raw = subprocess.check_output(["uptime", "-p"], text=True).strip()
    except Exception:
        uptime_raw = "N/A"

    print(f"\n[{timestamp}] 🖥️  SYSTEM INFO requested")
    print(f"  → CPU Temp : {temp}")
    print(f"  → Uptime   : {uptime_raw}\n")

    return jsonify({
        "status": "ok",
        "cpu_temp": temp,
        "uptime": uptime_raw,
        "timestamp": timestamp
    })


# ─── Start the server ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(BANNER)
    print("  Running on  → http://0.0.0.0:5000")
    print("  Endpoints   → GET  /ping")
    print("              → POST /message   (JSON: {\"message\": \"...\"})")
    print("              → GET  /system")
    print("\n  Press Ctrl+C to stop.\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
