from scripts.gmail_watcher import GmailWatcher
from scripts.whatsapp_watcher import WhatsAppWatcher
from scripts.scheduler import Scheduler
from scripts.config import CONFIG

def main():
    print("[SYSTEM] Starting Personal AI Employee System... 🚀")

    # Initialize Gmail watcher
    gmail = GmailWatcher(CONFIG['gmail_user'], CONFIG['gmail_pass'])
    
    # Initialize WhatsApp watcher
    whatsapp = WhatsAppWatcher(
        token_sid=CONFIG['twilio_sid'],
        auth_token=CONFIG['twilio_auth_token'],
        from_whatsapp=CONFIG['twilio_from'],
        to_whatsapp=CONFIG['twilio_to']
    )

    # Start watchers
    gmail.start()
    whatsapp.start()

    # Start scheduler
    scheduler = Scheduler()
    scheduler.start()

    print("[SYSTEM] All modules running successfully!")

if __name__ == "__main__":
    main()
