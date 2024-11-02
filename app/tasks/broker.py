import asyncio

from app.tasks.taskiq_app import broker
from app.tasks.tasks import publish, update_sub_table, update_notification_table
# from app.tasks.tasks import update_sub_table
