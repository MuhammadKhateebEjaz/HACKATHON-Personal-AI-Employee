import imaplib
import email
from email.header import decode_header
import time
from scripts.utils import log_message
from scripts.config import CONFIG

class GmailWatcher:
    def __init__(self, email_user, email_pass, check_interval=60):
        self.email_user = email_user
        self.email_pass = email_pass
        self.check_interval = check_interval
        self.imap_server = "imap.gmail.com"

    def start(self):
        print(f"[GMAIL] Starting Gmail watcher for {self.email_user}...")
        try:
            while True:
                self.check_emails()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            print("[GMAIL] Stopped watching emails.")

    def check_emails(self):
        try:
            # Connect to Gmail
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.email_user, self.email_pass)
            mail.select("inbox")

            # Search for unread emails
            status, messages = mail.search(None, '(UNSEEN)')
            email_ids = messages[0].split()
            print(f"[GMAIL] {len(email_ids)} new email(s) found.")

            for e_id in email_ids:
                status, msg_data = mail.fetch(e_id, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding if encoding else "utf-8")
                        from_ = msg.get("From")
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                                    break
                        else:
                            body = msg.get_payload(decode=True).decode()
                        
                        log_message("logs/ai_responses.log", f"Email from {from_}: {subject}\n{body}\n")
                        print(f"[GMAIL] Logged email: {subject}")
            mail.logout()
        except Exception as e:
            print(f"[GMAIL] Error: {e}")
