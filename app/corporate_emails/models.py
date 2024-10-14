from app.database import Base
from sqlalchemy.orm import mapped_column, Mapped


class CorporateEmail(Base):
    __tablename__ = 'corporatemails'

    email_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    registered: Mapped[bool]
