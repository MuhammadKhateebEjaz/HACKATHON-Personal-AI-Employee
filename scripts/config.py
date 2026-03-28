from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

CONFIG = {
    "gmail_user": os.getenv("GMAIL_USER"),
    "gmail_pass": os.getenv("GMAIL_PASS"),
    "whatsapp_token": os.getenv("WHATSAPP_TOKEN")
}
