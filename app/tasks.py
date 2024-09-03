from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend
from app.config import settings

broker = AioPikaBroker(settings.RABBITMQ_URL).with_result_backend(RedisAsyncResultBackend('redis://localhost'))


@broker.task
async def add_one(value: int) -> int:
    return value + 1
