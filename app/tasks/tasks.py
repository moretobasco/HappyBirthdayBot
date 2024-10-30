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
from app.notifications.dao import NotificationsDao
from app.notifications.schemas import SNotifications

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
    messages = await NotificationsDao.get_notifications_for_messages()
    if messages:
        tasks = []
        for message in messages:
            validated_message = SNotifications.model_validate(message)
            serialized_message = validated_message.model_dump_json()
            encoded_message = aio_pika.Message(body=serialized_message.encode())
            tasks.append(exchange.publish(encoded_message, routing_key='hbd'))
            await NotificationsDao.change_notification_status(
                notification_id=message.notification_id, status=2
            )
        await asyncio.gather(*tasks)
        await connection.close()
    else:
        return None


@broker.task(schedule=[{'cron': '* * * * *'}])
async def publish():
    await send_message()


# @broker.task(schedule=[{'cron': '* * * * *'}])
# async def update_sub_table():
#     await SubscriptionsDAO.create_subscriptions()
#
#
# @broker.task(schedule=[{'cron': '* * * * *'}])
# async def update_notification_table():
#     await NotificationsDao.create_notifications()
