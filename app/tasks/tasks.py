import asyncio
import json

import aio_pika
from taskiq_aio_pika import AioPikaBroker
from app.config import settings
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler, BrokerMessage
from app.subscription.dao import SubscriptionsDAO
from aio_pika import ExchangeType
from app.tasks.taskiq_app import broker

# scheduler = TaskiqScheduler(
#     broker=broker,
#     sources=[LabelScheduleSource(broker=broker)],
# )



# @broker.task(schedule=[{'cron': '* * * * *'}])
@broker.task
async def send_message():
    await broker.startup()
    mes: BrokerMessage = BrokerMessage(
        task_name='hbd',
        task_id='unique-task-id',
        message='hi!'.encode(),
        labels={'priority': 'high'}
    )
    await broker.kick(mes)
    await broker.shutdown()




# @broker.task(schedule=[{'cron': '* * * * *'}])
# async def send_message():
#     connection = await aio_pika.connect_robust(url=settings.RABBITMQ_URL)
#     channel = await connection.channel()
#     exchange = await channel.declare_exchange(name='happybirthday_exchange', type='direct')
#     queue = await channel.declare_queue(name='happybirthday_queue')
#     await queue.bind(exchange=exchange, routing_key='hbd')
#     message_list = ['Hello-1', 'Hello-2', 'Hello-3']
#     tasks = []
#     for m in message_list:
#         message = aio_pika.Message(body=m.encode())
#         tasks.append(exchange.publish(message, routing_key='hbd'))
#     await asyncio.gather(*tasks)
#     await connection.close()


# async def main():
#     task = asyncio.create_task(send_message())
#     await asyncio.gather(task)
#
#
# asyncio.get_event_loop().run_until_complete(main())

