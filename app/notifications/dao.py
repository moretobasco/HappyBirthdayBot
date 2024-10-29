import asyncio
import json
from typing import Optional

import pytz
from pytz import timezone, UTC
from datetime import datetime, timedelta, date, time


from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, cast, and_, or_, literal, update, delete, VARCHAR, Date
from sqlalchemy.orm import aliased
from sqlalchemy.dialects.postgresql import INTERVAL, JSONB, insert
from pprint import pprint
from app.subscription.schemas import SSubscriptions
from sqlalchemy.exc import IntegrityError
from asyncpg.exceptions import UniqueViolationError, ForeignKeyViolationError
from app.exceptions import DublicateSubscriptionError, UserNotFoundError
from pprint import pprint
from app.notifications.models import Notifications
from fastapi import Depends
from app.notifications.localize_utc_service import localize_utc

class NotificationsDao(BaseDAO):
    model = Notifications

    @classmethod
    async def create_notifications(cls):
        async with async_session_maker() as session:
            current_date = func.current_date()
            u1 = aliased(Users)
            u2 = aliased(Users)
            s = aliased(Subscriptions)

            query = select(
                s.subscription_id,
                s.user_id,
                s.user_sub_id,
                s.notification_hour,
                u2.birthday.label('notification_date'),
                u1.time_zone
            ).select_from(s).join(u1, u1.user_id == s.user_id).join(u2, u2.user_id == s.user_sub_id).where(
                or_(
                    s.notify_before_days.contains(cast(func.to_jsonb(
                        cast(func.concat(
                            cast(func.extract('year', func.current_date()), VARCHAR),
                            func.lpad(cast(func.extract('month', u2.birthday), VARCHAR), 2, "0"),
                            func.lpad(cast(func.extract('day', u2.birthday), VARCHAR), 2, "0")),
                            Date
                        ) - func.current_date()), JSONB)),
                    and_(
                        u2.birthday == current_date,
                        s.notify_on_day == True)
                )
            )
            result = await session.execute(query)
            pprint(result.mappings().all())

            # notifications = []
            # for row in result:
            #     subscription_id = row.subscription_id
            #     user_id = row.user_id
            #     user_sub_id = row.user_sub_id
            #     birthday = row.birthday
            #     time_zone = row.time_zone
            #     notification_hour = row.notification_hour
            #
            #     local_birthday = cast(func.concat(
            #         cast(func.extract('year', func.current_date()), VARCHAR),
            #         func.lpad(cast(func.extract('month', row.birthday), VARCHAR), 2, "0"),
            #         func.lpad(cast(func.extract('day', row.birthday), VARCHAR), 2, "0")),
            #         Date
            #     )
            #     notification_time = local_birthday + timedelta(hours=notification_hour)
            #     notification_time_utc = pytz.timezone('UTC').localize(notification_time)
            #
            # add_notifications = insert(Notifications).from_select(
            #     [
            #         'subscription_id',
            #         'user_id',
            #         'user_sub_id',
            #         'created_at',
            #         'notification_date',
            #         'notification_time',
            #         'status',
            #         'notify_before_days',
            #         'notify_on_day'
            #     ], query
            # ).on_conflict_do_nothing(index_elements=['user_id', 'user_sub_id', 'notification_date'])
            #
            # await session.execute(add_notifications)
            # await session.commit()



async def main():
    task = asyncio.create_task(NotificationsDao.create_notifications())
    await asyncio.gather(task)


asyncio.get_event_loop().run_until_complete(main())
