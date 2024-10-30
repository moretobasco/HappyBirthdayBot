from datetime import date

from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy import select, func, Interval, cast, String, text, Date, column, VARCHAR, Select, Insert, and_


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    def cast_birthday_to_current_year(cls, birthday: date):
        query = cast(func.concat(
            cast(func.extract('year', func.current_date()), VARCHAR),
            func.lpad(cast(func.extract('month', birthday), VARCHAR), 2, "0"),
            func.lpad(cast(func.extract('day', birthday), VARCHAR), 2, "0")),
            Date)
        return query
