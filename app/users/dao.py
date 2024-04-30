import asyncio
from datetime import datetime

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import Users
from sqlalchemy import select, func, Interval, cast
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
    async def test(cls):
        async with async_session_maker() as session:
            # query = select(func.extract('year', func.current_date())-func.extract('year', cls.model.birthday))
            # query = select(func.extract('year', func.current_date()))
            # query = select(func.lpad('1', 2, '0'))
            query = func.concat()
            result = await session.execute(query)
            # return result.mappings().all()
            print(result.mappings().all())


# async def test():
#     return await test()
#
#
# async def main():
#     task = asyncio.create_task(test())
#     await task
#
# asyncio.run(main())

