import asyncio
from datetime import datetime

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, Interval, cast, String, text, Date, column, VARCHAR, Select, Insert, and_
from sqlalchemy.dialects.postgresql import INTERVAL


class SubscriptionsDAO(BaseDAO):
    model = Subscriptions

    @classmethod
    async def birthdays_this_month(cls):
        async with async_session_maker() as session:
            query = select(Users).join(Subscriptions, Users.user_id == Subscriptions.user_id).where(



            )
            result = await session.execute(query)
            return result.mappings().all()