import asyncio

from app.tasks.taskiq_app import broker
from app.tasks.tasks import publish


# async def main():
#     await broker.startup()
#     await publish.kiq()
#     await broker.shutdown()
#
# if __name__ == '__main__':
#     asyncio.run(main())
