from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import date, timedelta
from sqlalchemy import Date, Computed, func, cast, VARCHAR
from sqlalchemy import Interval
from sqlalchemy.dialects.postgresql import INTERVAL
from typing import Optional

from app.corporate_emails.models import CorporateEmail
from app.subscription.models import Subscriptions

from app.database import Base

"""
(birthday+MAKE_INTERVAL(EXTRACT(YEAR FROM CURRENT_DATE) :: INTEGER-EXTRACT(YEAR FROM birthday) :: INTEGER)) :: DATE - CURRENT_DATE
"""


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    birthday: Mapped[date]
    email: Mapped[str] = mapped_column(unique=True)
    telegram: Mapped[int] = mapped_column(unique=True)
    hashed_password: Mapped[Optional[str]]

    subscriber_id: Mapped['Subscriptions'] = relationship(foreign_keys=Subscriptions.user_id, back_populates='subscriber_id')
    subscribed_to_id: Mapped['Subscriptions'] = relationship(foreign_keys=Subscriptions.user_sub_id, back_populates='subscribed_to_id')
    corporate_email: Mapped['CorporateEmail'] = relationship(
        foreign_keys=CorporateEmail.email,
        # back_populates='corporate_email',
        primaryjoin='CorporateEmail.email == Users.email',
        viewonly=True
    )

    def __str__(self):
        return f'{self.email}'

