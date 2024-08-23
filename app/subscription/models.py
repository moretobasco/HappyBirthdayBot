from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import JSONB
from datetime import date, timedelta
from app.database import Base


class Subscriptions(Base):
    __tablename__ = 'subscriptions'

    subscription_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    user_sub_id: Mapped[int]
    notify_before_days: Mapped[list[int]] = mapped_column(JSONB)
    notify_on_day: Mapped[bool]

