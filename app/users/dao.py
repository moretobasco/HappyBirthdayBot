from datetime import datetime

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import Users
from sqlalchemy import select, func


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
            # query = select(func.extract('year', cls.model.birthday)) - select(func.extract('year', func.current_date()))
            query = select(func.extract('year', func.current_date()))
            result = await session.execute(query)
            # return result.mappings().all()
            print(result.mappings().all())