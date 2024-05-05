from app.database import Base
from sqlalchemy.orm import Mapped


class Verification(Base):
    __tablename__ = 'verification'

    email: Mapped[str]
    verified: Mapped[bool]
