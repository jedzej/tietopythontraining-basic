import pytest
from datetime import date
from date_calculator import date_calculator


leap_year = date(2016, 2, 29)


@pytest.mark.parametrize("years, date_vars, expected", [
    (1, {}, date(2017, 3, 1)),
    (4, {}, date(2020, 2, 29)),
    (-4, {}, date(2012, 2, 29)),
    (0, {'days': 1}, date(2016, 3, 1)),
    (0, {'hours': 24}, date(2016, 3, 1)),
    (0, {'hours': -24}, date(2016, 2, 28)),
    (1, {'hours': -24}, date(2017, 2, 28)),
])
def test_eval(years, date_vars, expected):
    assert date_calculator(leap_year, years, date_vars) == expected
