import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.providers.base import AbstractMessageProvider

from src.domain import MessageLog, MessageStatus
from src.settings import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASSWORD,
    SMTP_SENDER_EMAIL
)


class SMTPMailMessageProvider(AbstractMessageProvider):

    name: str = "SMTP"

    def send_message(self, log: MessageLog, raw_message: str) -> MessageLog:
        """
        Send E-mail through SMTP
        """
        # Extract information from the log
        recipient = log.destination
        subject = log.metadata.get('subject', 'No Subject')
        body = raw_message

        # Creating the email message
        msg = MIMEMultipart()
        msg['From'] = SMTP_SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Upgrade to a secure TLS connection
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_SENDER_EMAIL, recipient, msg.as_string())

            # Update log status to sent
            log.status = MessageStatus.SENT

        except Exception as exc:
            # Handle any exceptions that occur and mark the status as failed
            log.metadata['error'] = str(exc)
            log.status = MessageStatus.FAILED

        # Return the updated log
        return log

