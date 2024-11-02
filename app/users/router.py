from fastapi import APIRouter, Depends

from app.admin.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth, SUserRegister
from app.corporate_emails.email_service import async_send_mail, generate_secret
from app.redis.redis_app import r
from app.users.auth import check_existing_user_and_corporate, verify_password
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Users']
)


@router.post('/get_temporary_password')
async def get_temporary_password(user_data: SUserAuth, password=Depends(generate_secret)) -> None:
    await check_existing_user_and_corporate(user_data=user_data)
    r.set(user_data.email, password)
    r.expire(user_data.email, 300)
    await async_send_mail(email_address=user_data.email, password=password)


@router.post('/register')
async def register_user(user_data: SUserRegister) -> None:
    await check_existing_user_and_corporate(user_data=user_data)
    await verify_password(user_data=user_data)
    hashed_password = get_password_hash(user_data.admin_password)
    await UsersDAO.add_user(
        user_name=user_data.user_name,
        email=user_data.email,
        birthday=user_data.birthday,
        telegram=user_data.telegram,
        hashed_password=hashed_password
    )


@router.get('/me')
async def read_my_user(current_user=Depends(get_current_user)):
    return current_user
