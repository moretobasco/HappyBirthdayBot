import asyncio


from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, cast, or_
from sqlalchemy.dialects.postgresql import INTERVAL, JSONB
from app.users.dao import cast_birthday_to_current_year


class SubscriptionsDAO(BaseDAO):
    model = Subscriptions

    @classmethod
    async def get_subs_v2(cls):
        """
        SELECT *
        FROM subscriptions
        JOIN users ON users.user_id = subscriptions.user_sub_id
        WHERE subscriptions.notify_before_days::jsonb @> to_jsonb(CAST(concat(
        CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR),
        lpad(CAST(EXTRACT(month FROM users.birthday) AS VARCHAR), 2, '0'),
        lpad(CAST(EXTRACT(day FROM users.birthday) AS VARCHAR), 2, '0')) AS DATE) - CURRENT_DATE)
        OR subscriptions.notify_on_day = TRUE
        """
        async with async_session_maker() as session:
            birthday_this_year = await cast_birthday_to_current_year(Users.birthday)
            query = select(
                Subscriptions.__table__.columns,
                Users.__table__.columns
            ).join(Subscriptions, Users.user_id == Subscriptions.user_sub_id).where(
                or_(
                Subscriptions.notify_before_days.contains(cast(func.to_jsonb(
                    birthday_this_year - func.current_date()), JSONB)),
                Subscriptions.notify_on_day == True
                )
            )
            result = await session.execute(query)
            # print(result.mappings().all())
            return result.mappings().all()

# async def main():
#     task = asyncio.create_task(SubscriptionsDAO.get_subs_v2())
#     await asyncio.gather(task)
#     # coro1 = UsersDAO.test()
#     # await coro1
#
#
# asyncio.get_event_loop().run_until_complete(main())
