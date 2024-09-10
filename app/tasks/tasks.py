import asyncio
import aio_pika
from app.config import settings
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler
from app.tasks.taskiq_app import broker
from datetime import datetime

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
    # message_list = ['Hello-1', 'Hello-2', 'Hello-3']
    # time_list = [datetime.now().strftime('%H:%M:%S') for _ in range(3)]
    tasks = []
    for _ in range(3):
        time = datetime.now().strftime('%H:%M:%S')
        message = aio_pika.Message(body=time.encode())
        await asyncio.sleep(5)
        tasks.append(exchange.publish(message, routing_key='hbd'))
    # for m in time_list:
    #     message = aio_pika.Message(body=m.encode())
    #     tasks.append(exchange.publish(message, routing_key='hbd'))
    await asyncio.gather(*tasks)
    await connection.close()


@broker.task(schedule=[{'cron': '* * * * *'}])
async def publish():
    await send_message()