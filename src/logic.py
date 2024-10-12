from abc import ABC, abstractmethod
from hashlib import sha256

from src.schema import (
    Trigger,
    SMSTrigger,
    MailTrigger,
    MailTemplateTrigger,
    PushNotificationTrigger
)

from src.providers.base import AbstractMessageProvider

from src.domain import (
    MessageChannel,
    MessageContentType,
    MessageLog
)


class MessageTransmitter(ABC):

    @abstractmethod
    async def transmit(
        self,
        trigger: Trigger,
        provider: AbstractMessageProvider
    ) -> MessageLog:

        ...

    @staticmethod
    def hash_message(msg: str) -> str:

        return sha256(msg.encode()).hexdigest()


class SMSMessageTransmitter(MessageTransmitter):

    async def transmit(
        self,
        trigger: SMSTrigger,
        provider: AbstractMessageProvider
    ):

        log = MessageLog(
            user_id=trigger.user_id,
            channel=MessageChannel.SMS,
            content_type=MessageContentType.TEXT,
            destination=trigger.phone,
            content_hash=self.hash_message(
                trigger.content
            ),
            provider=provider.name,
            provider_id=provider_id
        )

        log = provider.send_message(log)
        # TODO: persist log
        return log


class MailMessageTransmitter(MessageTransmitter):

    async def transmit(
        self,
        trigger: MailTrigger,
        provider: AbstractMessageProvider
    ):

        log = MessageLog(
            user_id=trigger.user_id,
            channel=MessageChannel.EMAIL,
            content_type=MessageContentType.TEXT,
            destination=trigger.email,
            content_hash=self.hash_message(
                trigger.content
            ),
            provider=provider.name,
            provider_id=provider_id
        )

        log = provider.send_message(log)
        # TODO: persist log
        return log 


class TemplatedMailMessageTransmitter(MessageTransmitter):

    async def transmit(
        self,
        trigger: SMSTrigger,
        provider: AbstractMessageProvider
    ):

        log = MessageLog(
            user_id=trigger.user_id,
            channel=MessageChannel.EMAIL,
            content_type=MessageContentType.TEMPLATED,
            destination=trigger.email,
            provider=provider.name,
            provider_id=provider_id,
            template_id=trigger.template_id,
            template_data=trigger.template_data
        )

        log = provider.send_message(log)

        # TODO: persist log
        return log


class SMSMessageTransmitter(MessageTransmitter):

    async def transmit(
        self,
        trigger: SMSTrigger,
        provider: AbstractMessageProvider
    ):

        log = MessageLog(
            user_id=trigger.user_id,
            channel=MessageChannel.PUSH,
            content_type=MessageContentType.JSON,
            destination=trigger.device_token,
            provider=provider.name,
            provider_id=provider_id,
            metadata=trigger.content
        )

        log = provider.send_message(log)
        # TODO: persist log
        return log 

