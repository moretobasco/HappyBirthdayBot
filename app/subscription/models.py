from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base
from typing import Optional


class Subscriptions(Base):
    __tablename__ = 'subscriptions'

    subscription_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    user_sub_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    notify_before_days: Mapped[Optional[list[int]]] = mapped_column(JSONB, nullable=False)
    notify_on_day: Mapped[bool] = mapped_column(nullable=False)
    notification_hour: Mapped[int] = mapped_column(default=int(12))

    __table_args__ = (UniqueConstraint('user_id', 'user_sub_id', name='unique_subscription'),)

    subscriber_id: Mapped['Users'] = relationship(foreign_keys=user_id, back_populates='subscriber_id')
    subscribed_to_id: Mapped['Users'] = relationship(foreign_keys=user_sub_id, back_populates='subscribed_to_id')

    def __str__(self):
        return f'Subscription #{self.subscription_id}'
