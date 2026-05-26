import smtplib
import os
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class EmailService:

    def __init__(self):
        self.sender_email = os.getenv("EMAIL_ADDRESS")
        self.sender_password = os.getenv("EMAIL_PASSWORD")
        self.receiver_email = os.getenv("EMAIL_ADDRESS")

    def send_intrusion_alert(self, image_path):

        if not self.sender_email or not self.sender_password:
            print("❌ Email non configuré (.env manquant)")
            return

        msg = EmailMessage()
        msg["Subject"] = "🚨 ALERTE INTRUS - Smart Surveillance"
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        msg.set_content(f"""
ALERTE INTRUS DETECTEE !

Date : {now}

Un individu inconnu a été détecté par le système.
        """)

        with open(image_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(image_path)

        msg.add_attachment(
            file_data,
            maintype="image",
            subtype="jpeg",
            filename=file_name
        )

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.sender_email, self.sender_password)
                smtp.send_message(msg)

            print("📧 Email d'alerte envoyé !")

        except Exception as e:
            print("❌ Erreur envoi email :", e)