from fastapi import APIRouter
from app.users.schemas import SUserAuth
from app.users.dao import UsersDAO
from app.exceptions import UserAlreadyExistsException, CorporateEmailNotExists
from app.corporate_emails.email_service import send_email, generate_secret
from app.corporate_emails.models import CorporateEmailRegistry
from app.corporate_emails.dao import CorporateEmailDAO


router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи']
)


@router.post('/get_temporary_password')
async def register_user(user_data: SUserAuth):
    existing_user = UsersDAO.find_one_or_none(telegram=user_data.telegram)
    if existing_user:
        raise UserAlreadyExistsException
    existing_corporate_email = CorporateEmailDAO.find_one_or_none(email=user_data.email)
    if existing_corporate_email:
        raise CorporateEmailNotExists
    password = generate_secret()
















