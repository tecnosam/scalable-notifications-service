import os

from dotenv import load_dotenv


load_dotenv()

HTTP_PORT        = os.getenv("PORT", 8000)


SMTP_SERVER       = os.getenv("SMTP_SERVER")
SMTP_PORT         = os.getenv("SMTP_PORT")
SMTP_USER         = os.getenv("SMTP_USER")
SMTP_PASSWORD     = os.getenv("SMTP_PASSWORD")
SMTP_SENDER_EMAIL = os.getenv("SMTP_SENDER_EMAIL")


KAFKA_BROKER_URL  = os.getenv("KAFKA_BROKER_URL", "localhost:9092")

