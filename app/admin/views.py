from sqladmin import ModelView

from app.users.models import Users
from app.subscription.models import Subscriptions
from app.corporate_emails.models import CorporateEmail


class UsersView(ModelView, model=Users):
    column_list = '__all__'
    can_delete = False
    name = 'user'
    name_plural = 'users'
    icon = 'fa-solid fa-user'
    page_size = 100


class SubscriptionView(ModelView, model=Subscriptions):
    column_list = '__all__'
    name = 'subscription'
    name_plural = 'subscriptions'
    icon = 'fa-solid fa-cake-candles'
    page_size = 100


class CorporateEmailsView(ModelView, model=CorporateEmail):
    column_list = '__all__'
    name = 'corporate_emails'
    name_plural = 'corporate_email'
    icon = 'fa-solid fa-envelope'
    page_size = 100
