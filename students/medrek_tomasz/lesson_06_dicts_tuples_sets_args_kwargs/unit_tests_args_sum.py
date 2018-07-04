import pytest
from args_sum import sum_all


@pytest.mark.parametrize("test_input, expected", [
    ((1, 2, 3), 6),
    ((1, 2, -3), 0),
    ((1), 1),
    ((-1, -2, -3), -6),
    ((-1, -2, -3, -4), -10),
    ((), 0),
])
def test_eval(test_input, expected):
    try:
        assert sum_all(*test_input) == expected
    except TypeError:
        assert sum_all(test_input) == expected
