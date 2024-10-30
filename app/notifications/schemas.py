from datetime import date, datetime
from typing import Optional
from datetime import date

from pydantic import BaseModel, ConfigDict, model_serializer


class SNotifications(BaseModel):
    notification_id: int
    subscription_id: int
    user_id: int
    user_sub_id: int
    created_at: datetime
    notification_date: date
    notification_time: datetime
    birthday: Optional[date] = None
    email: Optional[str] = None
    telegram: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
