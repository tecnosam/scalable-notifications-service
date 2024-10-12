from fastapi import APIRouter
from src.schema import (
    SMSTrigger,
    MailTrigger,
    MailTemplateTrigger,
    PushNotificationTrigger
)

from src.logic import (
    MailMessageTransmitter
)

from src.providers.mail.smtp import SMTPMailMessageProvider


router = APIRouter(prefix="/notify", tags=["Manual Notification Trigger"])


@router.post("/sms")
async def trigger_sms_route(trigger: SMSTrigger):

    return {"status": "received"}


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

    return {"status": "received"}


@router.post("push")
async def trigger_push_notification_route(
    trigger: PushNotificationTrigger
):

    return {"status": "received"}

