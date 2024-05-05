import smtplib
from email.message import EmailMessage
from app.config import settings
import string
import secrets

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465


def generate_secret():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(8))
    return password


def write_email(addressee: str):
    email = EmailMessage()
    email['Subject'] = 'Verify your email'
    email['From'] = settings.SMTP_USER
    email['To'] = addressee

    email.set_content(
        '<div>'
        '<h1 style="font-size: 24px;"> Hello! </h1>'
        '<p> This is your verification code: </p>'
        f'<p style="font-size: 48px; color: navy;"> {generate_secret()} </p>'
        '</div>',
        subtype='html'
    )
    return email


def send_email():
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(write_email('Alexey.Lisanskiy@advncd.com'))


send_email()
