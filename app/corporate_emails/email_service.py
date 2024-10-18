import asyncio
import aiosmtplib
import smtplib
from email.message import EmailMessage
from app.config import settings
import string
import secrets
from app.config import settings
from app.exceptions import EmailSendError
from string import Template
import os


def generate_secret() -> str:
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(8))
    return password


def read_html_template(template_path: str) -> str:
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_email(addressee: str, password: str) -> EmailMessage:
    # template = read_html_template('./app/corporate_emails/email_template.html')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, 'email_template.html')
    template = read_html_template(template_path)

    template = Template(template)
    content = template.safe_substitute(password=password)

    email = EmailMessage()
    email['Subject'] = 'Verify your corporate_emails for a Birthdaybot'
    email['From'] = settings.SMTP_USER
    email['To'] = addressee

    # email.set_content(
    #     '<div>'
    #     '<h1 style="font-size: 24px;"> Hello! </h1>'
    #     '<p> This is your verification code: </p>'
    #     f'<p style="font-size: 48px; color: navy;"> {password} </p>'
    #     '</div>',
    #     subtype='html'
    # )

    email.set_content(content, subtype='html')
    return email


async def async_send_mail(email_address: str, password: str):
    message = write_email(addressee=email_address, password=password)
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
