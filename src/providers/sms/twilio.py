from src.providers.base import AbstractMessageProvider
from src.domain import MessageLog


class TwilioSMSMessageProvider(AbstractMessageProvider):

    name: str = "twilio"

    def send_message(self, log: MessageLog, raw_message: str) -> MessageLog:

        return log

