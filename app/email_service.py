import smtplib
from email.message import EmailMessage
from app.config import settings


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465


def test_email():
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.sendmail('moretobasco@gmail.com', 'moretobasco@gmail.com', 'THIS IS TEST')


test_email()