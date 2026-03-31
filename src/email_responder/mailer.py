import smtplib
from email.message import EmailMessage
from email_responder import settings
from email_responder.logger import get_logger

log = get_logger(__name__)


def send_email(to: str, subject: str, body: str) -> bool:
    if not all([settings.smtp_user, settings.smtp_pass]):
        log.warning("SMTP not configured — email not sent")
        return False
    msg = EmailMessage()
    msg["From"] = settings.smtp_user
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    try:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as s:
            s.starttls()
            s.login(settings.smtp_user, settings.smtp_pass)
            s.send_message(msg)
        log.info(f"Email sent to {to}")
        return True
    except Exception as exc:
        log.error(f"Email failed: {exc}")
        return False