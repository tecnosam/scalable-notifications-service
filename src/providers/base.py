from abc import ABC, abstractmethod

from src.domain import MessageLog


class AbstractMessageProvider(ABC):

    name: str

    @abstractmethod
    def send_message(self, log: MessageLog, *args, **kwargs) -> MessageLog:
        ...

