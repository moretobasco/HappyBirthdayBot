from fastapi import FastAPI
from app.users.router import router as users_router
from app.subscription.router import router as subscription_router
from app.tasks.tasks import broker, add_one

app = FastAPI()

app.include_router(users_router)
app.include_router(subscription_router)

@app.on_event("startup")
async def app_startup():
    if not broker.is_worker_process:
        await broker.startup()
        await add_one.kiq()


@app.on_event("shutdown")
async def app_shutdown():
    if not broker.is_worker_process:
        await broker.shutdown()

# taskiq = InMemoryBroker()
#
#
# @taskiq.task
# async def send_birthday_notification(user_id: int, user_agent: str):
#     print(f"Sending birthday notification to user {user_id}")
#     await asyncio.sleep(10)
#     print('Я дальше работаю')
#     print(f"User-Agent: {user_agent}")
#
#
# @app.post("/send_notification/")
# async def send_notification(request: Request):
#     user_agent = request.headers.get("User-Agent")
#     user_id = 42  # Пример значения
#     await send_birthday_notification.kiq(user_id=user_id, user_agent=user_agent)



