from typing import Union
from sqladmin import Admin, ModelView

from fastapi import FastAPI

from app.admin.views import UsersView, SubscriptionView, CorporateEmailsView
from app.users.models import Users
from app.users.router import router as auth_router
from app.subscription.router import router as subscription_router
from app.users.birthdays.router import router as birthdays_router
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from app.database import engine

app = FastAPI()

app.include_router(auth_router)
app.include_router(birthdays_router)
app.include_router(subscription_router)

admin = Admin(app, engine)

admin.add_view(UsersView)
admin.add_view(SubscriptionView)
admin.add_view(CorporateEmailsView)
