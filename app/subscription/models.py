from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base


class Subscriptions(Base):
    __tablename__ = 'Subscriptions'

    subscription_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('Users.user_id'))
    user_sub_id: Mapped[int] = mapped_column(ForeignKey('Users.user_id'))
    notify_before_days: Mapped[list[int]] = mapped_column(JSONB)
    notify_on_day: Mapped[bool]

    __tableargs__ = (UniqueConstraint('user_id', 'user_sub_id', name='unique_subscription'),)

    subscriber_id: Mapped['Users'] = relationship(back_populates='subscriber_id')
    subscribed_to_id: Mapped['Users'] = relationship(back_populates='subscribed_to_id')

