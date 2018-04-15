import pytest
import args_sum
import math


test_data = [
        ((1, 2, 3), 6),
        ((1.0, 2.0, 1.5, 15), 19.5),
        ((), 0),
        ((2.0001, -2.0001), 0),
    ]


@pytest.mark.parametrize('values, expected', test_data)
def test_sum_all_on_test_data(values, expected):
    assert math.isclose(args_sum.sum_all(*values), expected)
