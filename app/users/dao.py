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
    async def test(cls, duration):
        async with (async_session_maker() as session):
            # query = select(func.extract('year', func.current_date())-func.extract('year', cls.model.birthday))
            # query = select(func.extract('year', func.current_date()))
            # query = select(func.lpad('1', 2, '0'))
            # query = select(cast(func.extract('months', func.current_date())), String)
            # query = select(cast(func.extract('day', cls.model.birthday), VARCHAR))
            # query = select(func.lpad(cast(func.extract('day', cls.model.birthday), String)), 2, '0')
            # query = select(func.extract('months', func.current_date()))
            # query = select(cast(func.concat('2024', '05', '05'), Date))
            # query = select(cls.model.user_id, cls.model.user_name, cast(
            #     func.concat(
            #         cast(func.extract('year', func.current_date()), VARCHAR),
            #         cls.model.b_month, cls.model.b_day), Date)-func.current_date())


            """
            SELECT *
            FROM users
            WHERE
            CAST(concat(CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR), users.b_month, users.b_day) AS DATE)
            - CURRENT_DATE >= 0 AND CAST(concat(CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR), users.b_month, users.b_day) AS DATE)
            - CURRENT_DATE <=15
            """
            query = select(cls.model.user_name).where(
                and_(
                    cast(func.concat(cast(func.extract('year', func.current_date()), VARCHAR),
                                     cls.model.b_month,
                                     cls.model.b_day), Date)-func.current_date() <= duration,
                    cast(func.concat(cast(func.extract('year', func.current_date()), VARCHAR),
                                     cls.model.b_month,
                                     cls.model.b_day), Date) - func.current_date() >= 0)
                     )

            result = await session.execute(query)
            # return result.mappings().all()
            print(result.mappings().all())

    @classmethod
    async def add_user(cls, **data):
        async with async_session_maker() as session:
            query = Insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()



# async def test123():
#     return await UsersDAO.test()


async def main():
    task = asyncio.create_task(UsersDAO.test(30))
    await asyncio.gather(task)
    # coro1 = UsersDAO.test()
    # await coro1

asyncio.get_event_loop().run_until_complete(main())

