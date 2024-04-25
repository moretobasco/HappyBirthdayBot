from sqlalchemy.orm import mapped_column, Mapped
from datetime import date
from sqlalchemy import Date


from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    birthday: Mapped[date] = mapped_column(Date)
