from fastapi import APIRouter
from app.users.dao import UsersDAO

router = APIRouter(
    prefix='/birthdays',
)


@router.get('in_horizon')
async def get_birthdays(horizon: int):
    return await UsersDAO.birthdays_in_horizon(duration=horizon)


@router.get('this_month')
async def get_birthdays():
    return await UsersDAO.birthdays_this_month()
