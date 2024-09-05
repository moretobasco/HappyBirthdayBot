from taskiq_aio_pika import AioPikaBroker
from app.config import settings
from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler, BrokerMessage
from app.subscription.dao import SubscriptionsDAO

broker = AioPikaBroker(settings.RABBITMQ_URL)

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


@broker.task(schedule=[{'cron': '1 * * * *'}])
async def add_one():
    print('Я начал работать')
    result = 'Hello!'
    message = BrokerMessage(
        task_name='add_one',
        task_id='unique-task-id',
        message=result.encode('utf-8'),
        labels={'priority': 'high'}
    )
    await broker.kick(message)



