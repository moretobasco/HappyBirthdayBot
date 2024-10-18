import asyncio
import aiosmtplib
import smtplib
from email.message import EmailMessage
from app.config import settings
import string
import secrets
from app.config import settings
from app.exceptions import EmailSendError


def generate_secret() -> str:
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(8))
    return password


def write_email(addressee: str, password: str) -> EmailMessage:
    email = EmailMessage()
    email['Subject'] = 'Verify your corporate_emails for a Birthdaybot'
    email['From'] = settings.SMTP_USER
    email['To'] = addressee

    email.set_content(
        '<div>'
        '<h1 style="font-size: 24px;"> Hello! </h1>'
        '<p> This is your verification code: </p>'
        f'<p style="font-size: 48px; color: navy;"> {password} </p>'
        '</div>',
        subtype='html'
    )
    return email


async def async_send_mail(email_address: str, password: str):
    message = write_email(email_address, password)
    try:
        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            username=settings.SMTP_USER,
            password=settings.SMTP_PASS,
            use_tls=True
        )
    except Exception:
        raise EmailSendError







# def send_email(email_address: str, password: str) -> None:
#     with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
#         server.login(settings.SMTP_USER, settings.SMTP_PASS)
#         server.send_message(write_email(email_address, password))
