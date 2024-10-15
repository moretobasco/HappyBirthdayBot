from app.exceptions import UserAlreadyExistsException, CorporateEmailNotExists, ExpiredPasswordException, \
    IncorrectPasswordException
from app.users.dao import UsersDAO
from app.corporate_emails.dao import CorporateEmailDAO
from app.users.schemas import SUserAuth
from app.redis.redis_app import r


async def check_existing_user_and_corporate(user_data: SUserAuth) -> None:
    existing_user = await UsersDAO.find_one_or_none(telegram=user_data.telegram)
    if existing_user:
        raise UserAlreadyExistsException
    existing_corporate_email = await CorporateEmailDAO.find_one_or_none(email=user_data.email)
    if not existing_corporate_email:
        raise CorporateEmailNotExists


async def verify_password(user_data: SUserAuth) -> None:
    true_password = r.get(user_data.email)
    if not true_password:
        raise ExpiredPasswordException
    if true_password != user_data.permanent_password:
        raise IncorrectPasswordException
