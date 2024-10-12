from src.providers.base import AbstractMessageProvider


class SMTPMailMessageProvider(AbstractMessageProvider):

    name: str = "SMTP"

    def send_message(self, log: MessageLog) -> MessageLog:
        """
        Send E-mail through SMTP
        """
        ...
        return log

