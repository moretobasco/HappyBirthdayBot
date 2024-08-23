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
    async def test_subs(cls, days: int):
        '''
        SELECT *
        FROM subscriptions
        JOIN users ON users.user_id = subscriptions.user_id
        WHERE subscriptions.notify_before_days::jsonb @> '[5]';
        '''
        async with async_session_maker() as session:
            query = select(Users.__tablename__.columns, Subscriptions.__tablename__.columns).join(Subscriptions, Users.user_id == Subscriptions.user_id).where(
                Subscriptions.notify_before_days.contains([days])
            )
            result = await session.execute(query)
            return result.mappings().all()
