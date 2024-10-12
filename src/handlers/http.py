from fastapi import APIRouter
from src.schema import (
    SMSTrigger,
    MailTrigger,
    MailTemplateTrigger,
    PushNotificationTrigger
)

from src.logic import (
    MailMessageTransmitter,
    SMSMessageTransmitter,
    PushNotificationMessageTransmitter
)

from src.providers.mail.smtp import SMTPMailMessageProvider
from src.providers.sms.twilio import TwilioSMSMessageProvider
from src.providers.push.firebase import FirebasePushNotificationMessageProvider


router = APIRouter(prefix="/notify", tags=["Manual Notification Trigger"])


@router.post("/sms")
async def trigger_sms_route(trigger: SMSTrigger):

    provider = TwilioSMSMessageProvider()
    transmitter = SMSMessageTransmitter()

    return await transmitter.transmit(
        trigger=trigger,
        provider=provider
    )


@router.post("/email")
async def trigger_email_route(trigger: MailTrigger):

    provider = SMTPMailMessageProvider()
    transmitter = MailMessageTransmitter()
    return await transmitter.transmit(
        trigger=trigger,
        provider=provider
    )


@router.post("/templated-email")
async def trigger_templated_email_route(
    trigger: MailTemplateTrigger
):

    return "Not Yet supported"


@router.post("/push")
async def trigger_push_notification_route(
    trigger: PushNotificationTrigger
):

    provider = FirebasePushNotificationMessageProvider()
    transmitter = PushNotificationMessageTransmitter()

    return await transmitter.transmit(
        trigger=trigger,
        provider=provider
    )

