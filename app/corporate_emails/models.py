from app.database import Base


class CorporateEmailRegistry(Base):
    email: str
    registered: bool
