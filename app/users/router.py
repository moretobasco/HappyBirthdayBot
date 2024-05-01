from fastapi import APIRouter
from app.users.dao import UsersDAO

router = APIRouter(
    prefix='/birthdays',
)


@router.get('get_birthdays')
async def get_birthdays(duration: int):
    return await UsersDAO.test(duration=duration)
