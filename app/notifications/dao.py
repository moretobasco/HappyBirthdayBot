import asyncio
import json
from typing import Optional, Tuple, List

import pytz
from pytz import timezone, UTC
from datetime import datetime, timedelta, date, time
from typing import Optional

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
                        cls.cast_birthday_to_current_year(u2.birthday) - func.current_date()), JSONB)),
                    and_(
                        u2.birthday == current_date,
                        s.notify_on_day == True)
                )
            )
            result = await session.execute(query)

            notifications = []
            for row in result:
                subscription_id = row.subscription_id
                user_id = row.user_id
                user_sub_id = row.user_sub_id
                notification_date = row.notification_date
                time_zone = row.time_zone
                notification_hour = row.notification_hour

                local_birthday = notification_date.replace(year=datetime.now().year)

                notification_utc_time = localize_utc(
                    time_zone=time_zone,
                    local_birthday=local_birthday,
                    notification_hour=notification_hour
                )

                if not all([subscription_id, user_id, user_sub_id, notification_date, notification_utc_time]):
                    print(f'Skipping row {subscription_id} with missing data')
                    continue

                notifications.append(
                    {
                        'subscription_id': subscription_id,
                        'user_id': user_id,
                        'user_sub_id': user_sub_id,
                        'notification_date': notification_date,
                        'notification_time': notification_utc_time,
                    }
                )

            add_notifications = insert(Notifications).values(
                notifications
            ).on_conflict_do_nothing(index_elements=['user_id', 'user_sub_id', 'notification_date'])

            await session.execute(add_notifications)
            await session.commit()

    @classmethod
    async def get_notifications_for_messages(cls):
        async with async_session_maker() as session:
            u1 = aliased(Users)
            u2 = aliased(Users)
            current_time = datetime.utcnow()
            query = select(
                Notifications.__table__.columns,
                u1.telegram,
                u1.email,
                u2.birthday,
                u2.user_name.label('user_sub_name'),
            ).select_from(Notifications).join(
                u1, u1.user_id == Notifications.user_id
            ).join(
                u2, u2.user_id == Notifications.user_sub_id
            ).where(
                and_(
                    current_time >= Notifications.notification_time,
                    Notifications.status == 1
                )
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def change_notification_status(cls, notifications: List[Tuple[int, int, Optional[datetime]]]):
        async with async_session_maker() as session:
            for notification_id, status, sent_at in notifications:
                updated_status = update(Notifications).where(
                    Notifications.notification_id == notification_id).values(
                    status=status, sent_at=sent_at
                ).execution_options(synchronize_session='fetch')
                await session.execute(updated_status)
            await session.commit()

# async def main():
#     task = asyncio.create_task(NotificationsDao.get_notifications_for_messages())
#     await asyncio.gather(task)
#
#
# asyncio.get_event_loop().run_until_complete(main())
