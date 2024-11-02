import asyncio
from typing import List, Tuple, Optional

import aio_pika
from aio_pika import Message

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


async def send_message() -> None:
    messages = await NotificationsDao.get_notifications_for_messages()
    if messages:
        connection = await aio_pika.connect_robust(url=settings.RABBITMQ_URL)
        channel = await connection.channel()
        exchange = await channel.declare_exchange(name='happybirthday_exchange', type='direct')
        queue = await channel.declare_queue(name='happybirthday_queue')
        await queue.bind(exchange=exchange, routing_key='hbd')
        tasks = []
        notifications_to_update: List[Tuple[int, int, Optional[datetime]]] = []
        for message in messages:
            validated_message: SNotifications = SNotifications.model_validate(message)
            serialized_message: str = validated_message.model_dump_json()
            encoded_message: Message = aio_pika.Message(body=serialized_message.encode())
            tasks.append(exchange.publish(encoded_message, routing_key='hbd'))
            notification_id: int = message.notification_id
            notification = (notification_id, 2, None)
            notifications_to_update.append(notification)
        await NotificationsDao.change_notification_status(notifications=notifications_to_update)
        await asyncio.gather(*tasks)
        await connection.close()
    else:
        return None


@broker.task(schedule=[{'cron': '*/5 * * * *'}])
async def update_sub_table():
    await SubscriptionsDAO.create_subscriptions()


@broker.task(schedule=[{'cron': '*/5 * * * *'}])
async def update_notification_table():
    await NotificationsDao.create_notifications()


@broker.task(schedule=[{'cron': '*/5 * * * *'}])
async def publish():
    await send_message()

