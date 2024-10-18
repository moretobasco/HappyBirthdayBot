from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class SBirthdays(BaseModel):
    user_id: int
    user_name: str
    birthday: date
    email: Optional[EmailStr] = None
    telegram: Optional[int] = None