from fastapi import FastAPI
from app.users.router import router as users_router
from app.subscription.router import router as subscription_router

app = FastAPI()

app.include_router(users_router)
app.include_router(subscription_router)