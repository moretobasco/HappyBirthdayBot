import jwt
from jwt.exceptions import PyJWTError, ExpiredSignatureError
from fastapi import Request, Depends
from app.users.dao import UsersDAO
from app.exceptions import UserNotExists, TokenExpiredException, IncorrectTokenFormatException, UserIsNotAdmin
from app.users.schemas import SUserRegister
from app.config import settings
from app.exceptions import TokenAbsentException


def get_token(request: Request):
    token = request.cookies.get('birthday_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_admin(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError:
        raise TokenExpiredException
    except PyJWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserNotExists
    user = await UsersDAO.find_one_or_none(user_id=int(user_id))
    if not user:
        raise UserNotExists
    return user
