from fastapi import APIRouter, Depends
from app.users.dao import UsersDAO
from app.users.birthdays.schemas import SBirthdays
from app.users.dependencies import get_current_user



router = APIRouter(
    prefix='/birthdays',
    tags=['Birthdays']
)


@router.get('/in_horizon/{horizon}', response_model=list[SBirthdays])
async def get_birthdays(horizon: int, user=Depends(get_current_user)):
    if user:
        return await UsersDAO.birthdays_in_horizon(duration=horizon)


@router.get('/this_month', response_model=list[SBirthdays])
async def get_birthdays(user=Depends(get_current_user)):
    if user:
        return await UsersDAO.birthdays_this_month()
