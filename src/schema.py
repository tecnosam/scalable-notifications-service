from typing import Optional

from uuid import UUID
from pydantic import BaseModel


class Trigger(BaseModel):

    user_id: Optional[UUID]


class SMSTrigger(Trigger):
    
    phone: str
    content: str


class MailTrigger(Trigger):

    email: str
    content: str


class MailTemplateTrigger(Trigger):

    email: str
    template_id: str
    template_data: dict


class PushNotificationTrigger(Trigger):

    device_token: str
    content: dict

