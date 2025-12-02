# 📡 Telegram Message Sender

A lightweight relay server that forwards messages to the Telegram Bot API.  
Useful when your main backend **cannot access Telegram directly** (e.g., Telegram blocked in the region).

Backend → Relay Server → Telegram.

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/tg-message-sender.git
cd tg-message-sender

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
source venv/bin/activate
python3 app.py


## Production (systemd + Gunicorn)Create service:

Create service: /etc/systemd/system/tg-message-sender.service

[Unit]
Description=Telegram Message Sender
After=network.target

[Service]
User=root
WorkingDirectory=/opt/tg-message-sender
ExecStart=/opt/tg-message-sender/venv/bin/gunicorn -b 0.0.0.0:7000 app:app --workers=4 --threads=4
Restart=always

[Install]
WantedBy=multi-user.target

Enable:
systemctl daemon-reload
systemctl enable tg-message-sender
systemctl restart tg-message-sender

