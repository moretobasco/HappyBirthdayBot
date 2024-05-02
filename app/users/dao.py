import asyncio
from datetime import datetime

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import Users
from sqlalchemy import select, func, Interval, cast, String, text, Date, column, VARCHAR, Select, Insert, and_
from sqlalchemy.dialects.postgresql import INTERVAL


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()


    @classmethod
    async def birthdays_this_month(cls):
        async with async_session_maker() as session:
            query = select(cls.model).where(
                cast(func.extract('month', func.current_date()), VARCHAR) == func.lpad(cls.model.b_month, 2, "0")
            )
            result = await session.execute(query)
            print(result.mappings().all())
            # return result.mappings().all()




    @classmethod
    async def birthdays_in_horizon(cls, duration):
        async with (async_session_maker() as session):
            """
            SELECT *
            FROM users
            WHERE
            CAST(concat(CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR), users.b_month, users.b_day) AS DATE)
            - CURRENT_DATE >= 0 AND CAST(concat(CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR), users.b_month, users.b_day) AS DATE)
            - CURRENT_DATE <=30
            ORDER BY CAST(concat(CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR), users.b_month, users.b_day) AS DATE)
            - CURRENT_DATE
            """

            query = select(
                cls.model.__table__.columns
            ).where(
                and_(
                    cast(func.concat(cast(func.extract('year', func.current_date()), VARCHAR),
                                     cls.model.b_month,
                                     cls.model.b_day), Date)-func.current_date() <= duration,
                    cast(func.concat(cast(func.extract('year', func.current_date()), VARCHAR),
                                     cls.model.b_month,
                                     cls.model.b_day), Date) - func.current_date() >= 0)
                     ).order_by((cast(func.concat(cast(func.extract('year', func.current_date()), VARCHAR),
                                 cls.model.b_month,
                                 cls.model.b_day), Date) - func.current_date()))

            result = await session.execute(query)
            return result.mappings().all()
            # print(result.mappings().all())

    @classmethod
    async def add_user(cls, **data):
        async with async_session_maker() as session:
            query = Insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()



async def test123():
    return await UsersDAO.birthdays_this_month()


async def main():
    task = asyncio.create_task(UsersDAO.birthdays_this_month())
    await asyncio.gather(task)
    # coro1 = UsersDAO.test()
    # await coro1

asyncio.get_event_loop().run_until_complete(main())

