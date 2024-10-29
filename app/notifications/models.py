from sqlalchemy import UniqueConstraint, ForeignKey, TIMESTAMP, func, text
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base
from typing import Optional
from datetime import date, datetime


class Notifications(Base):
    __tablename__ = 'notifications'

    notification_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    subscription_id: Mapped[int] = mapped_column(ForeignKey('subscriptions.subscription_id', ondelete='CASCADE'),
                                                 nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    user_sub_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    notification_date: Mapped[date] = mapped_column(nullable=False)
    notification_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(ForeignKey('statuses.status_id'), nullable=False, server_default=text('1'))
    sent_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))

    __table_args__ = (UniqueConstraint('user_id', 'user_sub_id', 'notification_date', name='unique_notification'),)

    def __str__(self):
        return f'Notification #{self.notification_id}'
