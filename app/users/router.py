from fastapi import APIRouter
from app.users.dao import UsersDAO

router = APIRouter(
    prefix='/birthdays',
)


@router.get('get_birthdays')
async def get_birthdays():
    return await UsersDAO.test()
