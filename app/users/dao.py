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
            birthday_this_year = await BaseDAO.cast_birthday_to_current_year(cls.model.birthday)
            query = select(
                cls.model.__table__.columns
            ).where(
                and_(
                    birthday_this_year - func.current_date() <= duration,
                    birthday_this_year - func.current_date() >= 0)
            ).order_by(birthday_this_year - func.current_date())

            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_user(cls, **data):
        async with async_session_maker() as session:
            query = Insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def add_user_and_create_subscriptions(cls, user_name, birthday, email, telegram, hashed_password,
                                                notify_before_days):
        async with async_session_maker() as session:
            # add_user = Insert(Users).values(
            #     user_name=user_name,
            #     birthday=birthday,
            #     email=email,
            #     telegram=telegram,
            #     hashed_password=password
            # )
            new_user = Users(
                user_name=user_name,
                birthday=birthday,
                email=email,
                telegram=telegram,
                hashed_password=hashed_password
            )
            session.add(new_user)
            await session.flush()

            u1 = aliased(Users)
            u2 = aliased(Users)

            all_users = select(
                u1.user_id.label('user_id'),
                u2.user_id.label('user_sub_id'),
                cast(literal(notify_before_days), JSONB),
                literal(True)
            ).select_from(u1).join(u2, u1.user_id != u2.user_id)

            add_subscriptions = insert(Subscriptions).from_select(
                ['user_id', 'user_sub_id', 'notify_before_days', 'notify_on_day'], all_users
            ).on_conflict_do_nothing(index_elements=['user_id', 'user_sub_id'])

            await session.execute(add_subscriptions)
            await session.commit()

# async def main():
#     task = asyncio.create_task(UsersDAO.birthdays_in_horizon_v3(5))
#     await asyncio.gather(task)
#     # coro1 = UsersDAO.test()
#     # await coro1
#
#
# asyncio.get_event_loop().run_until_complete(main())
