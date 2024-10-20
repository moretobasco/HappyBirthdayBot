from app.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import UniqueConstraint, ForeignKey


class CorporateEmail(Base):
    __tablename__ = 'corporatemails'

    email_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(ForeignKey('users.email'))

    corporate_email: Mapped['Users'] = relationship(foreign_keys=email, back_populates='corporate_email')

    def __str__(self):
        return f'{self.email}'
