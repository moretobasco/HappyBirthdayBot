from typing import Union

from fastapi import FastAPI
from app.users.router import router as auth_router
from app.subscription.router import router as subscription_router
from app.users.birthdays.router import router as birthdays_router
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

app.include_router(auth_router)
app.include_router(birthdays_router)
app.include_router(subscription_router)



