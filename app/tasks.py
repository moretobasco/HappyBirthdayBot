import asyncio

import aio_pika
from taskiq_aio_pika import AioPikaBroker
from app.config import settings
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler, BrokerMessage
from app.subscription.dao import SubscriptionsDAO
from aio_pika import ExchangeType

# broker = AioPikaBroker(
#     settings.RABBITMQ_URL,
#     declare_exchange=True,
#     exchange_name='mynewtaskiq',
#     exchange_type=ExchangeType.DIRECT,
#     routing_key='happy',
#     queue_name='mynewq'
# )


# scheduler = TaskiqScheduler(
#     broker=broker,
#     sources=[LabelScheduleSource(broker)],
# )


# @broker.task(schedule=[{'cron': '* * * * *'}])
# @broker.task(queue='mynewq')
# async def add_one():
#     await broker.startup()
#     mes: BrokerMessage = BrokerMessage(
#         task_name='add_one',
#         task_id='unique-task-id',
#         message='Hello'.encode(),
#         labels={'priority': 'high'}
#     )
#     await broker.kick(mes)


async def send_message():
    connection = await aio_pika.connect_robust(url=settings.RABBITMQ_URL)
    channel = await connection.channel()
    exchange = await channel.declare_exchange(name='happybirthday_exchange', type='direct')
    queue = await channel.declare_queue(name='happybirthday_queue')
    await queue.bind(exchange=exchange, routing_key='hbd')
    message_list = ['Hello-1', 'Hello-2', 'Hello-3']
    tasks = []
    for m in message_list:
        message = aio_pika.Message(body=m.encode())
        tasks.append(exchange.publish(message, routing_key='hbd'))
    await asyncio.gather(*tasks)
    await connection.close()


async def main():
    task = asyncio.create_task(send_message())
    await asyncio.gather(task)


asyncio.get_event_loop().run_until_complete(main())
