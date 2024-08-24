from fastapi import APIRouter
from app.subscription.dao import SubscriptionsDAO

router = APIRouter(
    prefix='/Subscriptions',
)


@router.get('/getsub')
async def get_subscriptions():
    return await SubscriptionsDAO.test_subs()
