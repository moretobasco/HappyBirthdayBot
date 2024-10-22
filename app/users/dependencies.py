import jwt
from jwt.exceptions import PyJWTError, ExpiredSignatureError
from fastapi import Request, Depends
from app.users.dao import UsersDAO
from app.exceptions import UserNotExists, TokenExpiredException, IncorrectTokenFormatException, UserIsNotAdmin
from app.users.schemas import SUserRegister
from app.config import settings
from app.exceptions import TokenAbsentException


def get_telegram_id(request: Request) -> int:
    host = request.headers.get('Host')
    if host == settings.LOCALHOST:
        telegram_id = settings.ADMIN_TELEGRAM
    else:
        payload = request.json()
        telegram_id = payload['message']['from']['id']
    return telegram_id


async def get_current_user(telegram_id=Depends(get_telegram_id)) -> SUserRegister:
    user = await UsersDAO.find_one_or_none(telegram=telegram_id)
    if not user:
        raise UserNotExists
    return user




