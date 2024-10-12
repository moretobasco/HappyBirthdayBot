from fastapi import APIRouter
from app.subscription.dao import SubscriptionsDAO
from app.subscription.schemas import SSubscriptions
from app.exceptions import DublicateSubscriptionError, UserNotFoundError
from app.exceptions import UserIsNotFoundException, DublicatedSubscriptionException
import json

router = APIRouter(
    prefix='/Subscriptions',
)


@router.get('/getsub')
async def get_subscriptions():
    return await SubscriptionsDAO.get_subs_v2()


@router.post('/subscribe')
async def subscribe(
        user_id: int,
        user_sub_id: int,
        notify_before_days: list[int],
        notify_on_day: bool
):
    subscription = await SubscriptionsDAO.add_subscription(user_id, user_sub_id, notify_before_days, notify_on_day)
    if subscription == DublicateSubscriptionError:
        raise DublicatedSubscriptionException
    elif subscription == UserNotFoundError:
        raise UserIsNotFoundException
    return subscription


@router.post('/subscribe_all_users')
async def subscribe_all_users(user_id: int, notify_before_days: list[int]):
    notify_before_days = json.dumps(notify_before_days)
    subscriptions = await SubscriptionsDAO.subscribe_all_users(user_id, notify_before_days)
    if subscriptions == DublicateSubscriptionError:
        raise DublicatedSubscriptionException
    return subscriptions





