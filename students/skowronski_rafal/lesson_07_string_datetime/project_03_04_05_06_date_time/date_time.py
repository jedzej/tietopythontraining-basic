from datetime import datetime
from datetime import tzinfo
from datetime import timezone
from dateutil.relativedelta import relativedelta


def from_timestamp(timestamp, tz: tzinfo=None) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=tz)


def add(dt: datetime, years=0, days=0, hours=0, minutes=0) ->datetime:
    return dt + relativedelta(
        years=years, days=days, hours=hours, minutes=minutes)


def get_days_difference(dt1: datetime, dt2: datetime):
    return (dt1 - dt2).days


def get_pretty_date_time_string(date_time: datetime) -> str:
    return '{0:%A}, {1} {0:%B %Y}, {2}:{0:%M:%S}'.format(
        date_time, date_time.day, date_time.hour)


if __name__ == '__main__':
    timestamp = 0
    now = datetime.now()
    future = now + relativedelta(years=11)
    years_to_add = 11
    hours_to_add = 3

    print('Early ages: {0}'.format(get_pretty_date_time_string(
        from_timestamp(timestamp, timezone.utc))))
    print('Now: {0}'.format(get_pretty_date_time_string(now)))
    print('Now + 11 years + 3 hours: {0}'.format(get_pretty_date_time_string(
        add(now, years=11, hours=3))))
    print('[(Now + 11 years) - now] in days: {0}'.format(
        get_days_difference(future, now)))
