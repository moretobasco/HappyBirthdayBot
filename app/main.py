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
from app.admin.auth import authentication_backend
# from app.admin.router import router as admin_router

app = FastAPI(title='BirthdayADP', version='0.1.0', root_path='/api')

# app.include_router(admin_router)
app.include_router(auth_router)
app.include_router(birthdays_router)
app.include_router(subscription_router)


admin = Admin(app, engine, authentication_backend=authentication_backend, base_url='/pgadmin')

admin.add_view(UsersView)
admin.add_view(SubscriptionView)
admin.add_view(CorporateEmailsView)
