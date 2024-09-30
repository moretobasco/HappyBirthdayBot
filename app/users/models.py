from sqlalchemy.orm import mapped_column, Mapped
from datetime import date, timedelta
from sqlalchemy import Date, Computed, func, cast, VARCHAR
from sqlalchemy import Interval
from sqlalchemy.dialects.postgresql import INTERVAL
from typing import Optional

from app.database import Base

"""
(birthday+MAKE_INTERVAL(EXTRACT(YEAR FROM CURRENT_DATE) :: INTEGER-EXTRACT(YEAR FROM birthday) :: INTEGER)) :: DATE - CURRENT_DATE
"""


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_role: Mapped[Optional[str]]
    user_name: Mapped[str]
    birthday: Mapped[date]
    email: Mapped[Optional[str]]
    telegram: Mapped[Optional[int]]
