# from dotenv import load_dotenv
# import os
from email.message import EmailMessage
import ssl
import smtplib

# load_dotenv()
email_sender = "Sender's Gmail Passward"
email_password = "Your Password"
# email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = "Receviers Email"

subject = "Reminder"

body = """
I hope you are doing well this is just a reminder for joining out class on time.
Thank You
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    