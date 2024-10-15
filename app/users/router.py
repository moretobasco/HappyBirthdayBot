from fastapi import APIRouter, Depends
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth, SUserRegister
from app.exceptions import UserAlreadyExistsException, CorporateEmailNotExists, IncorrectPasswordException, \
    ExpiredPasswordException
from app.corporate_emails.email_service import send_email, generate_secret
from app.corporate_emails.dao import CorporateEmailDAO
from app.redis.redis_app import r

router_birthdays = APIRouter(
    prefix='/birthdays',
)

router_auth = APIRouter(
    prefix='/auth',
    tags=['Auth & Users']
)


@router_birthdays.get('/in_horizon/{horizon}')
async def get_birthdays(horizon: int):
    return await UsersDAO.birthdays_in_horizon(duration=horizon)


@router_birthdays.get('/this_month')
async def get_birthdays():
    return await UsersDAO.birthdays_this_month()


@router_auth.post('/get_temporary_password')
async def get_temporary_password(user_data: SUserAuth, password=Depends(generate_secret)) -> None:
    existing_user = await UsersDAO.find_one_or_none(telegram=user_data.telegram)
    if existing_user:
        raise UserAlreadyExistsException
    existing_corporate_email = await CorporateEmailDAO.find_one_or_none(email=user_data.email)
    if not existing_corporate_email:
        raise CorporateEmailNotExists
    r.set(user_data.email, password)
    r.expire(user_data.email, 300)
    send_email(email_address=user_data.email, password=password)


@router_auth.post('/register')
async def register_user(user_data: SUserRegister) -> None:
    existing_user = await UsersDAO.find_one_or_none(telegram=user_data.telegram)
    if existing_user:
        raise UserAlreadyExistsException
    existing_corporate_email = await CorporateEmailDAO.find_one_or_none(email=user_data.email)
    if not existing_corporate_email:
        raise CorporateEmailNotExists
    true_password = r.get(user_data.email)
    if not true_password:
        raise ExpiredPasswordException
    if true_password != user_data.permanent_password:
        raise IncorrectPasswordException
    await UsersDAO.add_user(
        user_name=user_data.user_name,
        email=user_data.email,
        birthday=user_data.birthday,
        telegram=user_data.telegram,
    )
