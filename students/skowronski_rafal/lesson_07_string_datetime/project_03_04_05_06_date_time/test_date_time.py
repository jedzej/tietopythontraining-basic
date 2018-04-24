import date_time
import pytest
from datetime import timezone
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


timestamp_data = [
    (0, timezone.utc, datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc)),
    (0, timezone(timedelta(hours=1)),
     datetime(1970, 1, 1, 0, 0, 0, 0, timezone.utc)),
    (20, timezone.utc, datetime(1970, 1, 1, 0, 0, 20, 0, timezone.utc)),
    (20, timezone.utc, datetime(1970, 1, 1, 0, 0, 20, 0, timezone.utc))
]


add_data = [
    (datetime(1970, 1, 1, 0, 0, 0, 0),
     dict(years=1, days=4, hours=5, minutes=6),
     datetime(1971, 1, 5, 5, 6, 0, 0)),
    (datetime(1970, 1, 1, 0, 0, 0, 0),
     dict(days=400),
     datetime(1971, 2, 5, 0, 0, 0, 0)),
    (datetime(1971, 2, 5, 0, 0, 0, 0),
     dict(days=-400),
     datetime(1970, 1, 1, 0, 0, 0, 0)),
]


difference_data = [
    (datetime(1970, 1, 1, 0, 0, 0, 0),
     datetime(1970, 1, 1, 0, 0, 0, 0) + relativedelta(days=1234),
     1234),
    (datetime(1970, 1, 1),
     datetime(1970, 1, 1),
     0)
]


@pytest.mark.parametrize('timestamp, utc, expected', timestamp_data)
def test_from_timestamp_on_test_data(timestamp, utc, expected):
    assert date_time.from_timestamp(timestamp, utc) == expected


@pytest.mark.parametrize('base_dt, offset, expected', add_data)
def test_add_on_test_data(base_dt, offset, expected):
    assert date_time.add(base_dt, **offset) == expected


@pytest.mark.parametrize('dt1, dt2, expected_difference', difference_data)
def test_get_days_difference_on_test_data(dt1, dt2, expected_difference):
    assert date_time.get_days_difference(dt2, dt1) == expected_difference
