import asyncio
import base64

from taskiq import BrokerMessage
from taskiq_aio_pika import AioPikaBroker
from app.config import settings
from app.tasks.taskiq_app import broker
from app.tasks.tasks import send_message


# async def main() -> None:
#     await broker.startup()
#     # Send the task to the broker.
#     task = await add_one.kiq(1)
#     # Wait for the result.
#     result = await task.wait_result(timeout=2)
#     print(f"Task execution took: {result.execution_time} seconds.")
#     if not result.is_err:
#         print(f"Returned value: {result.return_value}")
#     else:
#         print("Error found while executing task.")
#     await broker.shutdown()


async def main() -> None:
    await broker.startup()
    await send_message.kiq()
    print('я отправил задачу')
    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

# asyncio.get_event_loop().run_until_complete(main())


