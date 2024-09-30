from pydantic import BaseModel, ConfigDict

BaseModel.model_dump()

class SSubscriptions(BaseModel):
    subscription_id: int
    user_id: int
    user_sub_id: int
    notify_before_days: [list[int]]
    notify_on_day: bool

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
