import asyncio
import aio_pika
from app.config import settings
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler
from app.tasks.taskiq_app import broker
from datetime import datetime
from app.subscription.dao import SubscriptionsDAO
import json
from app.subscription.schemas import SSubscriptions
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
    messages = await SubscriptionsDAO.get_subscriptions_for_messages()
    if messages:
        tasks = []
        for message in messages:
            validated_message = SSubscriptions.model_validate(message)
            serialized_message = validated_message.model_dump_json()
            message = aio_pika.Message(body=serialized_message.encode())
            tasks.append(exchange.publish(message, routing_key='hbd'))
        await asyncio.gather(*tasks)
        await connection.close()
    else:
        return None


# @broker.task(schedule=[{'cron': '* * * * *'}])
# async def publish():
#     await send_message()


@broker.task(schedule=[{'cron': '* * * * *'}])
async def update_sub_table():
    await SubscriptionsDAO.update_subscriptions_table()
