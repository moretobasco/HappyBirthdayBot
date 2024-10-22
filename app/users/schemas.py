from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import date


class SUserAuth(BaseModel):
    email: EmailStr
    telegram: int


class SUserRegister(SUserAuth):
    user_name: str
    birthday: date
    permanent_password: str
    admin_password: Optional[str] = None


class SAdminAuth(BaseModel):
    email: EmailStr
    password: str
