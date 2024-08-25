import asyncio
from datetime import datetime

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, Interval, cast, String, text, Date, column, VARCHAR, Select, Insert, and_
from sqlalchemy.dialects.postgresql import INTERVAL, JSONB


class SubscriptionsDAO(BaseDAO):
    model = Subscriptions

    @classmethod
    async def test_subs(cls):
        '''
        SELECT *
FROM subscriptions
JOIN users ON users.user_id = subscriptions.user_sub_id
WHERE subscriptions.notify_before_days::jsonb @> to_jsonb(CAST(concat(
CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR),
lpad(CAST(EXTRACT(month FROM users.birthday) AS VARCHAR), 2, '0'),
lpad(CAST(EXTRACT(day FROM users.birthday) AS VARCHAR), 2, '0')) AS DATE) - CURRENT_DATE)
        '''
        async with async_session_maker() as session:
            query = select(
                Subscriptions.__table__.columns,
                Users.__table__.columns
            ).join(Subscriptions, Users.user_id == Subscriptions.user_sub_id).where(
                Subscriptions.notify_before_days.contains(cast(func.to_jsonb(cast(func.concat(
                        cast(func.extract('year', func.current_date()), VARCHAR),
                        func.lpad(cast(func.extract('month', Users.birthday), VARCHAR), 2, "0"),
                        func.lpad(cast(func.extract('day', Users.birthday), VARCHAR), 2, "0")),
                         Date) - func.current_date()), JSONB))
            )
            result = await session.execute(query)
            return result.mappings().all()



# async def main():
#     task = asyncio.create_task(SubscriptionsDAO.test_subs())
#     await asyncio.gather(task)
#     # coro1 = UsersDAO.test()
#     # await coro1
#
#
# asyncio.get_event_loop().run_until_complete(main())
