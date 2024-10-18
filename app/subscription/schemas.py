from datetime import date
from typing import Optional
from datetime import date

from pydantic import BaseModel, ConfigDict, model_serializer


class SSubscriptions(BaseModel):
    subscription_id: int
    user_id: int
    user_sub_id: int
    notify_before_days: [list[int]]
    notify_on_day: bool
    user_role: Optional[str] = None
    birthday: Optional[date] = None
    email: Optional[str] = None
    telegram: Optional[str] = None

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
