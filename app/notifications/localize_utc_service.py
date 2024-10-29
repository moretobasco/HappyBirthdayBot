import pytz
from pytz import timezone, UTC
from datetime import datetime, timedelta, date, time


def localize_utc(time_zone: str, birthday, notification_hour: int):
    user_timezone = pytz.timezone(time_zone)
    local_birthday = datetime.strptime(birthday, '%Y-%m-%d')
    notification_local_time = datetime.combine(local_birthday, time(notification_hour))
    notification_utc_time = user_timezone.localize(notification_local_time).astimezone(pytz.UTC)
    return notification_utc_time


# print(localize_utc('Europe/Moscow', '2024-01-01', 12))