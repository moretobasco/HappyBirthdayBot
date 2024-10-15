from fastapi import APIRouter
from app.subscription.dao import SubscriptionsDAO
from app.subscription.schemas import SSubscriptions
from app.exceptions import DublicateSubscriptionError, UserNotFoundError
from app.exceptions import UserIsNotFoundException, DublicatedSubscriptionException
import json

router = APIRouter(
    prefix='/subscriptions',
)


@router.get('/find_subscriptions')
async def get_subscriptions(
        user_id: int,
        user_sub_id: int,
):
    return await SubscriptionsDAO.find_all(user_id=user_id, user_sub_id=user_sub_id)


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
async def subscribe_all_users(
        user_id: int,
        notify_before_days: list[int]
):
    notify_before_days = json.dumps(notify_before_days)
    subscriptions = await SubscriptionsDAO.subscribe_all_users(user_id, notify_before_days)
    if subscriptions == DublicateSubscriptionError:
        raise DublicatedSubscriptionException
    return subscriptions


@router.put('/update_subscription/{user_id}/{user_sub_id}/')
async def update_subscription(
        user_id: int, sub_user_id: int,
        notify_before_days: list[int],
        notify_on_day: bool
):
    return await SubscriptionsDAO.update_subscription(user_id, sub_user_id, notify_before_days, notify_on_day)


@router.delete('/delete_subscription/{user_id}/{user_sub_id}')
async def delete_my_subscription(
        user_id: int,
        user_sub_id: int
):
    return await SubscriptionsDAO.delete_subscription(user_id=user_id, user_sub_id=user_sub_id)

