from fastapi import APIRouter, Depends
from app.subscription.dao import SubscriptionsDAO
from app.exceptions import DublicateSubscriptionError, UserNotFoundError
from app.exceptions import UserIsNotFoundException, DublicatedSubscriptionException
from app.users.dependencies import get_current_user
from app.users.models import Users
import json
from app.subscription.schemas import SSubscriptions
from typing import Optional

router = APIRouter(
    prefix='/subscriptions',
    tags=['Subscriptions']
)


@router.get('/find_subscriptions', response_model=list[SSubscriptions])
async def get_subscriptions(
        user_sub_id: int, user: Users = Depends(get_current_user)
):
    return await SubscriptionsDAO.find_all(user_id=user.user_id, user_sub_id=user_sub_id)


@router.post('/subscribe')
async def subscribe(
        user_sub_id: int,
        notify_before_days: list[int],
        notify_on_day: Optional[bool] = True,
        user: Users = Depends(get_current_user)
):
    subscription = await SubscriptionsDAO.add_subscription(
        user_id=user.user_id,
        user_sub_id=user_sub_id,
        notify_before_days=notify_before_days,
        notify_on_day=notify_on_day,
    )
    if subscription == DublicateSubscriptionError:
        raise DublicatedSubscriptionException
    elif subscription == UserNotFoundError:
        raise UserIsNotFoundException


@router.post('/subscribe_all_users')
async def subscribe_all_users(
        notify_before_days: Optional[list[int]] = 0,
        user: Users = Depends(get_current_user)
):
    notify_before_days = json.dumps(notify_before_days)
    subscriptions = await SubscriptionsDAO.subscribe_all_users(
        user_id=user.user_id,
        notify_before_days=notify_before_days)
    if subscriptions == DublicateSubscriptionError:
        raise DublicatedSubscriptionException


@router.put('/update_subscription/{user_id}/{user_sub_id}/')
async def update_subscription(
        user_sub_id: int,
        notify_before_days: list[int],
        notify_on_day: Optional[bool] = True,
        user: Users = Depends(get_current_user)
):
    return await SubscriptionsDAO.update_subscription(
        user_id=user.user_id,
        user_sub_id=user_sub_id,
        notify_before_days=notify_before_days,
        notify_on_day=notify_on_day
    )


@router.delete('/delete_subscription/{user_id}/{user_sub_id}')
async def delete_my_subscription(
        user_sub_id: int,
        user: Users = Depends(get_current_user)
):
    return await SubscriptionsDAO.delete_subscription(
        user_id=user.user_id,
        user_sub_id=user_sub_id
    )
