from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "7933864358:AAFB4vne6e826oGw4i0zzXxh5oo917LhSC0"
TELEGRAM_CHAT_ID = "-1002611813975"
TG_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json

    message = data.get("message")
    chat_id = data.get("chat_id", TELEGRAM_CHAT_ID)  # default group

    if not message:
        return jsonify({"status": "error", "message": "message is required"}), 400

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        r = requests.post(TG_URL, json=payload, timeout=5)
        return jsonify({"status": "ok", "telegram_response": r.json()})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
