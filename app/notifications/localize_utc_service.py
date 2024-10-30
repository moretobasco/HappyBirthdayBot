from typing import Any, Union

import pytz
from pytz import timezone, UTC
from datetime import datetime, timedelta, date, time


def localize_utc(time_zone: str, local_birthday: Union[str, datetime], notification_hour: int) -> datetime:
    user_timezone = pytz.timezone(time_zone)
    if isinstance(local_birthday, str):
        local_birthday = datetime.strptime(local_birthday, '%Y-%m-%d')
    notification_local_time = datetime.combine(local_birthday, time(notification_hour))
    notification_utc_time = user_timezone.localize(notification_local_time).astimezone(pytz.UTC).replace(tzinfo=None)
    return notification_utc_time


# print(localize_utc('Europe/Moscow', '2024-01-01', 12))