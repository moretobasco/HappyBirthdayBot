from fastapi import APIRouter
from app.subscription.dao import SubscriptionsDAO
from app.subscription.schemas import SSubscriptions

router = APIRouter(
    prefix='/Subscriptions',
)


@router.get('/getsub')
async def get_subscriptions():
    return await SubscriptionsDAO.get_subs_v2()


@router.get('/getsubjson')
async def get_subscriptions() -> list[SSubscriptions]:
    return await SubscriptionsDAO.get_subs_v2()


