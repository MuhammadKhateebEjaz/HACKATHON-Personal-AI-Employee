from scripts.gmail_watcher import GmailWatcher
from scripts.whatsapp_watcher import WhatsAppWatcher
from scripts.scheduler import Scheduler
from scripts.config import CONFIG

def main():
    print("[SYSTEM] Starting Personal AI Employee System... 🚀")

    # Initialize watchers with secure config
    gmail = GmailWatcher(CONFIG['gmail_user'], CONFIG['gmail_pass'])
    whatsapp = WhatsAppWatcher(CONFIG['whatsapp_token'])

    gmail.start()
    whatsapp.start()

    scheduler = Scheduler()
    scheduler.start()

    print("[SYSTEM] All modules running successfully!")

if __name__ == "__main__":
    main()
