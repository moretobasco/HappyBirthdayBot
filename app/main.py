from typing import Union

from fastapi import FastAPI
from app.users.router import router_auth as auth_router, router_birthdays as birth_router
from app.subscription.router import router as subscription_router
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

app.include_router(auth_router)
app.include_router(birth_router)
app.include_router(subscription_router)



