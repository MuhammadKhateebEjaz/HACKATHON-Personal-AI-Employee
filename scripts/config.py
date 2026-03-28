from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "gmail_user": os.getenv("GMAIL_USER"),
    "gmail_pass": os.getenv("GMAIL_PASS"),
    "twilio_sid": os.getenv("TWILIO_SID"),
    "twilio_auth_token": os.getenv("TWILIO_AUTH_TOKEN"),
    "twilio_from": os.getenv("TWILIO_FROM"),
    "twilio_to": os.getenv("TWILIO_TO")
}
