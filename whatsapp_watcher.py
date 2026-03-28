from twilio.rest import Client
from scripts.utils import log_message
from scripts.config import CONFIG
import time

class WhatsAppWatcher:
    def __init__(self, token_sid, auth_token, from_whatsapp="whatsapp:+14155238886", to_whatsapp=None, check_interval=60):
        self.token_sid = token_sid
        self.auth_token = auth_token
        self.from_whatsapp = from_whatsapp
        self.to_whatsapp = to_whatsapp
        self.check_interval = check_interval
        self.client = Client(self.token_sid, self.auth_token)

    def start(self):
        print("[WHATSAPP] Starting WhatsApp watcher...")
        try:
            while True:
                self.check_messages()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            print("[WHATSAPP] Stopped watching messages.")

    def check_messages(self):
        messages = self.client.messages.list(to=self.from_whatsapp, limit=10)
        for msg in messages:
            log_message("logs/ai_responses.log", f"WhatsApp from {msg.from_}: {msg.body}")
            print(f"[WHATSAPP] Logged message from {msg.from_}")
