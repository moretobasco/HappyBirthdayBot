from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base
from typing import Optional
from alembic import op
from sqlalchemy import Table


class Statuses(Base):
    __tablename__ = 'statuses'

    status_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    status_name: Mapped[str]

    def __str__(self):
        return f'Status {self.status_name}'


# op.bulk_insert(
#     'statuses',
#     [
#         {
#             "status_name": "pending",
#         },
#         {
#             "name": "sent",
#         },
#         {
#             "name": "failed",
#         },
#     ],
# )