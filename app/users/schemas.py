from pydantic import BaseModel, EmailStr
from datetime import date


class SUserAuth(BaseModel):
    email: EmailStr
    telegram: int


class SUserRegister(BaseModel):
    user_role: str
    user_name: str
    birthday: date
    email: str
    telegram: int
    permanent_password: str