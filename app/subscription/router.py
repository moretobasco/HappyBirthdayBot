from fastapi import APIRouter
from app.subscription.dao import SubscriptionsDAO
from app.subscription.schemas import SSubscriptions

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
    return subscription




