"""
app.py - Telegram Render Bot (Fixed Version)
--------------------------------------------
Compatible with Python 3.11.9 runtime on Render.
"""

import os
import requests
from flask import Flask, request, abort, jsonify

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/webhook")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is required. See README.md")

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
app = Flask(__name__)

def send_message(chat_id, text):
    payload = {"chat_id": chat_id, "text": text}
    requests.post(f"{API_URL}/sendMessage", json=payload, timeout=10)

@app.route("/")
def home():
    return "Render Telegram Bot is running successfully on Python 3.11!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        send_message(chat_id, f"आपने कहा: {text}")
    return "ok", 200

    if text == "/start":
        send_message(chat_id, "नमस्ते! मैं अब Python 3.11 पर चल रहा हूँ 🚀")
    else:
        send_message(chat_id, f"आपने कहा: {text}")
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    
