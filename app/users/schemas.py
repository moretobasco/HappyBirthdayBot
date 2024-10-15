from pydantic import BaseModel, EmailStr
from datetime import date


class SUserAuth(BaseModel):
    email: EmailStr
    telegram: int


class SUserRegister(SUserAuth):
    user_role: str
    user_name: str
    birthday: date
    permanent_password: str
