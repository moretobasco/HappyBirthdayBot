import asyncio
from datetime import datetime, date

from sqlalchemy.orm import aliased

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, Interval, cast, String, text, Date, column, VARCHAR, Select, Insert, and_, literal
from sqlalchemy.dialects.postgresql import insert, JSONB


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def birthdays_this_month(cls):
        """
        SELECT *
        FROM users
        WHERE lpad(CAST(EXTRACT(month FROM birthday) AS VARCHAR), 2, '0') =
        lpad(CAST(EXTRACT(month FROM CURRENT_DATE) AS VARCHAR), 2, '0')
        ORDER BY EXTRACT(day FROM birthday)
        """
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).where(
                func.lpad(cast(func.extract('month', cls.model.birthday), VARCHAR), 2, "0") ==
                func.lpad(cast(func.extract('month', func.current_date()), VARCHAR), 2, "0")
            ).order_by(func.extract('day', cls.model.birthday))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def birthdays_in_horizon(cls, duration):
        """
        SELECT *
        FROM users
        WHERE
        CAST(concat(
            CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR),
            lpad(CAST(EXTRACT(month FROM users.birthday) AS VARCHAR), 2, '0'),
            lpad(CAST(EXTRACT(day FROM users.birthday) AS VARCHAR), 2, '0')
        ) AS DATE) - CURRENT_DATE <= 15
        AND CAST(concat(
            CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR),
            lpad(CAST(EXTRACT(month FROM users.birthday) AS VARCHAR), 2, '0'),
            lpad(CAST(EXTRACT(day FROM users.birthday) AS VARCHAR), 2, '0')
        ) AS DATE) - CURRENT_DATE >= 0
        ORDER BY CAST(
            concat(
                CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR),
                lpad(CAST(EXTRACT(month FROM users.birthday) AS VARCHAR), 2, '0'),
                lpad(CAST(EXTRACT(day FROM users.birthday) AS VARCHAR), 2, '0')) AS DATE) - CURRENT_DATE
        """
        async with (async_session_maker() as session):
            query = select(
                cls.model.__table__.columns
            ).where(
                and_(
                    cls.cast_birthday_to_current_year(cls.model.birthday) - func.current_date() <= duration,
                    cls.cast_birthday_to_current_year(cls.model.birthday) - func.current_date() >= 0)
            ).order_by(cls.cast_birthday_to_current_year(cls.model.birthday) - func.current_date())

            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_user(cls, **data):
        async with async_session_maker() as session:
            query = Insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
