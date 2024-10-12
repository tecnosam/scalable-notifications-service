from src.providers.base import AbstractMessageProvider
from src.domain import MessageLog


class FirebasePushNotificationMessageProvider(AbstractMessageProvider):

    name: str = "firebase"

    def send_message(self, log: MessageLog, raw_message: dict) -> MessageLog:

        return log

