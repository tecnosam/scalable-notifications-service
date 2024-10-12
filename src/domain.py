from uuid import UUID, uuid4
from typing import Optional

from enum import Enum

from pydantic import BaseModel, Field


class MessageChannel(Enum):

    EMAIL = "email"
    PUSH  = "push"
    SMS   = "sms"


class MessageContentType(Enum):

    TEXT      = "raw-text"
    TEMPLATED = "templated"
    JSON      = "json"
    XML       = "xml"


class MessageStatus(Enum):

    PENDING   = "pending"
    DELIVERED = "delivered"
    FAILED    = "failed"


class MessageLog(BaseModel):

    uid: UUID = Field(default_factory=uuid4)
    user_id: Optional[UUID] = Field(default=None)

    channel: MessageChannel
    content_type: MessageContentType
    status: MessageStatus = Field(
        default=MessageStatus.PENDING
    )

    destination: str
    content_hash: Optional[str] = Field(
        help="Message content hashed",
        default=None
    )

    template_id: Optional[str] = Field(default=None)
    metadata: dict = Field(default_factory=dict)

    provider: Optional[str] = Field(
        help="Third party service used",
        default=None
    )
    provider_id: Optional[str] = Field(
        help="ID from third party service used",
        default=None
    )

