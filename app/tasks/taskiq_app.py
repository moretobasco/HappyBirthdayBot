from taskiq_aio_pika import AioPikaBroker
from app.config import settings

broker = AioPikaBroker(
    url=settings.RABBITMQ_URL,
    # exchange_name='happybirthday_exchange',
    # queue_name='happybirthday_queue',
    # exchange_type=aio_pika.ExchangeType.DIRECT,
    # routing_key='hbd'
)



