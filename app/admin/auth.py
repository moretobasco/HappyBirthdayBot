from typing import Union, Optional

from fastapi import HTTPException
from pydantic import EmailStr
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from passlib.context import CryptContext
from app.users.dao import UsersDAO
from app.exceptions import IncorrectEmailOrPasswordException
from datetime import datetime, timedelta
from app.config import settings
import jwt
from app.admin.dependencies import get_current_admin
from app.exceptions import UserIsNotAdmin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password_admin(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    role = 'user'
    if data.get('email') == settings.ADMIN_MAIL:
        role = 'admin'
    to_encode.update({'exp': expire, 'role': role})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not (user and verify_password_admin(password, user.hashed_password)):
        raise IncorrectEmailOrPasswordException
    return user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form['username'], form['password']
        user = await authenticate_user(email=email, password=password)
        if user:
            access_token = create_access_token({'sub': str(user.user_id), 'email': str(user.email)})
            if jwt.decode(access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])['role'] == 'admin':
                request.session.update({'token': access_token})
            elif jwt.decode(access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])['role'] == 'user':
                raise UserIsNotAdmin
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        token = request.session.get('token')

        if not token:
            return RedirectResponse(request.url_for('admin:login'), status_code=302)

        user = await get_current_admin(token)
        if not user:
            return RedirectResponse(request.url_for('admin:login'), status_code=302)
        return True


authentication_backend = AdminAuth(secret_key=settings.SECRET_KEY)
