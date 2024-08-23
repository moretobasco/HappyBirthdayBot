from fastapi import APIRouter
from app.subscription.dao import SubscriptionsDAO

router = APIRouter(
    prefix='/Subscriptions',
)


@router.get('/{days}')
async def get_birthdays(days: int):
    return await SubscriptionsDAO.test_subs(5)