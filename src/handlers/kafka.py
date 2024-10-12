import structlog
from uuid import uuid4
import asyncio
from confluent_kafka import Consumer, KafkaException

from src.settings import KAFKA_BROKER_URL


logger = structlog.get_logger()
# logger = structlog.Logger("Notification Service Kafka Consumer")


async def consumer_handler():

    consumer_id = uuid4()

    # Kafka consumer configuration
    consumer_config = {
        'bootstrap.servers': KAFKA_BROKER_URL,
        "group.id": "notifications-consumer-group",
        'auto.offset.reset': 'earliest'
    }

    # Create a consumer instance
    consumer = Consumer(consumer_config)

    # Subscribe to multiple topics
    topics = {
        "sms-notifications": [],
        "email-notifications": [],
        "push-notifications": []
    }
    consumer.subscribe(list(topics.keys()))

    print(f"Subscribed to topics: {topics.keys()}")
    while True:
        try:
            await asyncio.sleep(0.1)

            # Poll for messages
            # Wait for message for 500ms
            message = consumer.poll(timeout=.5)

            if message is None:
                continue

            topic = message.topic()
            trigger_class, provider, transmitter = topics[topic]

            data = json.loads(message.value().decode("utf-8"))
            trigger = trigger_class(**data)

            response = await transmitter.transmit(
                trigger=trigger,
                provider=provider
            )

            logger.info(
                "KafkaConsumer {consumer_id}> Notification Sent",
                data=data,
                response=response.model_dump(),
                topic=topic
            )

        except KeyboardInterrupt:
            logger.info("KafkaConsumer> Interrupt from OS, Closing connection...")
            consumer.close()
            break
        except KafkaException as exc:
            logger.error(
                f"KafkaConsumer {consumer_id}> Error Polling Kafka",
                error=exc
            )
            continue
        except Exception as exc:
            logger.error(
                f"KafkaConsumer {consumer_id}> Error sending Notification",
                error=exc
            )
            continue

