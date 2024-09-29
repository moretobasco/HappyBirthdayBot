import asyncio
import aio_pika
from app.config import settings
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler
from app.tasks.taskiq_app import broker
from datetime import datetime
from app.subscription.dao import SubscriptionsDAO

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker=broker)],
)


async def send_message():
    connection = await aio_pika.connect_robust(url=settings.RABBITMQ_URL)
    channel = await connection.channel()
    exchange = await channel.declare_exchange(name='happybirthday_exchange', type='direct')
    queue = await channel.declare_queue(name='happybirthday_queue')
    await queue.bind(exchange=exchange, routing_key='hbd')
    messages = await SubscriptionsDAO.get_subs_v2()
    if messages:
        tasks = []
        for _ in messages:
            message = aio_pika.Message(body=messages.encode())
            tasks.append(exchange.publish(message, routing_key='hbd'))
        await asyncio.gather(*tasks)
        await connection.close()
    else:
        return None

@broker.task(schedule=[{'cron': '* * * * *'}])
async def publish():
    await send_message()
