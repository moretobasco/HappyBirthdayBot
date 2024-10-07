import asyncio

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, cast, or_, Insert, insert
from sqlalchemy.dialects.postgresql import INTERVAL, JSONB
from app.users.dao import cast_birthday_to_current_year
from pprint import pprint
from app.subscription.schemas import SSubscriptions


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
            return result.mappings().all()

    @classmethod
    async def add_subscription(cls, user_id, user_sub_id, notify_before_days, notify_on_day):
        async with async_session_maker() as session:
            add_subscription = insert(Subscriptions).values(
                user_id=user_id,
                user_sub_id=user_sub_id,
                notify_before_days=notify_before_days,
                notify_on_day=notify_on_day
            )
            new_subscription = await session.execute(add_subscription)
            await session.commit()
            return new_subscription




# async def test_ser_model():
#     messages = await SubscriptionsDAO.get_subs_v2()
#     validated_messages = [SSubscriptions.model_validate(message) for message in messages]
#     for message in validated_messages:
#         print(message.model_dump_json())
#         print(type(message.model_dump()))


# async def main():
#     # task = asyncio.create_task(SubscriptionsDAO.get_subs_v2())
#     task = asyncio.create_task(test_ser_model())
#     await asyncio.gather(task)
#     # coro1 = UsersDAO.test()
#     # await coro1
#
#
# asyncio.get_event_loop().run_until_complete(main())
