import pytest
from args_sum import sum_all


@pytest.mark.parametrize("test_input, expected", [
    (sum_all(1, 2, 3), 6),
    (sum_all(1, 2, -3), 0),
    (sum_all(1), 1),
    (sum_all(-1, -2, -3), -6),
    (sum_all(), 0),
])
def test_eval(test_input, expected):
    assert test_input == expected
