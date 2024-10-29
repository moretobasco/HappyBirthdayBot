import asyncio
import json
from typing import Optional

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscription.models import Subscriptions
from app.users.models import Users
from sqlalchemy import select, func, cast, and_, or_, literal, update, delete
from sqlalchemy.orm import aliased
from sqlalchemy.dialects.postgresql import INTERVAL, JSONB, insert
from pprint import pprint
from app.subscription.schemas import SSubscriptions
from sqlalchemy.exc import IntegrityError
from asyncpg.exceptions import UniqueViolationError, ForeignKeyViolationError
from app.exceptions import DublicateSubscriptionError, UserNotFoundError
from pprint import pprint


class SubscriptionsDAO(BaseDAO):
    model = Subscriptions

    @classmethod
    async def update_subscriptions_table(cls, notify_before_days: Optional[list[int]] = None):
        if notify_before_days is None:
            notify_before_days = [0]
        async with async_session_maker() as session:
            notify_before_days = json.dumps(notify_before_days)
            u1 = aliased(Users)
            u2 = aliased(Users)

            all_users = select(
                u1.user_id.label('user_id'),
                u2.user_id.label('user_sub_id'),
                cast(literal(notify_before_days), JSONB),
                literal(True),
                literal(12)
            ).select_from(u1).join(u2, u1.user_id != u2.user_id)

            add_subscriptions = insert(Subscriptions).from_select(
                ['user_id', 'user_sub_id', 'notify_before_days', 'notify_on_day'], all_users
            ).on_conflict_do_nothing(index_elements=['user_id', 'user_sub_id'])

            await session.execute(add_subscriptions)
            await session.commit()

    @classmethod
    async def get_subscriptions_for_messages(cls):
        """
        SELECT *
        FROM subscriptions
        JOIN users ON users.user_id = subscriptions.user_sub_id
        WHERE subscriptions.notify_before_days::jsonb @> to_jsonb(CAST(concat(
        CAST(EXTRACT(year FROM CURRENT_DATE) AS VARCHAR),
        lpad(CAST(EXTRACT(month FROM users.birthday) AS VARCHAR), 2, '0'),
        lpad(CAST(EXTRACT(day FROM users.birthday) AS VARCHAR), 2, '0')) AS DATE) - CURRENT_DATE)
        OR (CURRENT_DATE = users.birthday AND subscriptions.notify_on_day = TRUE)
        """
        async with async_session_maker() as session:
            birthday_this_year = await BaseDAO.cast_birthday_to_current_year(Users.birthday)
            query = select(
                Subscriptions.__table__.columns,
                Users.__table__.columns
            ).join(Subscriptions, Users.user_id == Subscriptions.user_sub_id).where(
                or_(
                    Subscriptions.notify_before_days.contains(cast(func.to_jsonb(
                        birthday_this_year - func.current_date()), JSONB)),
                    and_(
                        Users.birthday == func.current_user(),
                        Subscriptions.notify_on_day == True)
                )
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_subscription(cls, user_id, user_sub_id, notify_before_days, notify_on_day):
        try:
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
        except IntegrityError as e:
            if e.orig.pgcode == UniqueViolationError.sqlstate:
                return DublicateSubscriptionError
            elif e.orig.sqlstate == ForeignKeyViolationError.sqlstate:
                return UserNotFoundError

    @classmethod
    async def subscribe_all_users(cls, user_id, notify_before_days):
        try:
            async with async_session_maker() as session:
                u1 = aliased(Users)
                u2 = aliased(Users)

                all_users = select(
                    u1.user_id.label('user_id'),
                    u2.user_id.label('user_sub_id'),
                    cast(literal(notify_before_days), JSONB),
                    literal(True)
                ).select_from(u1).join(u2, u1.user_id != u2.user_id).where(u1.user_id == user_id)

                add_subscriptions = insert(Subscriptions).from_select(
                    ['user_id', 'user_sub_id', 'notify_before_days', 'notify_on_day'], all_users
                )

                await session.execute(add_subscriptions)
                await session.commit()

        except IntegrityError as e:
            if e.orig.pgcode == UniqueViolationError.sqlstate:
                return DublicateSubscriptionError

    @classmethod
    async def update_subscription(cls, user_id, user_sub_id, notify_before_days, notify_on_day):
        async with async_session_maker() as session:
            updated_subscription = update(Subscriptions).filter_by(
                user_id=user_id, user_sub_id=user_sub_id
            ).values(notify_before_days=notify_before_days, notify_on_day=notify_on_day).execution_options(
                synchronize_session='fetch'
            )
            await session.execute(updated_subscription)
            await session.commit()

    @classmethod
    async def delete_subscription(cls, user_id, user_sub_id):
        async with async_session_maker() as session:
            deleted_subscription = delete(Subscriptions).filter_by(
                user_id=user_id, user_sub_id=user_sub_id
            )
            await session.execute(deleted_subscription)
            await session.commit()

# async def test_ser_model():
#     messages = await SubscriptionsDAO.get_subs_v2()
#     validated_messages = [SSubscriptions.model_validate(message) for message in messages]
#     for message in validated_messages:
#         print(message.model_dump_json())
#         print(type(message.model_dump()))


# async def main():
#     task = asyncio.create_task(SubscriptionsDAO.update_subscriptions_table())
#     await asyncio.gather(task)
#
# asyncio.get_event_loop().run_until_complete(main())
