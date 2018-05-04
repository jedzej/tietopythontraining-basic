import pytest
from numbers_filter import numbers_filter


@pytest.mark.parametrize("test_input, test_filter, expected", [
    (['2', '0', '8', '3'], 3, [8, 3]),
    (['2', '0', '8', '3'], 4, [8]),
    (['2', '0', '8', '3'], 2, [2, 8, 3]),
    (['2', '0', '8', '3'], 0, [2, 0, 8, 3]),
    (['2', '0', '8', '3'], -1, [2, 0, 8, 3]),
    (['-2', '-1', '8', '3'], -1, [-1, 8, 3]),
    (['2', '0', '8', '3'], 9, []),
])
def test_eval(test_input, test_filter, expected):
    assert numbers_filter(test_input, test_filter) == expected


def test_character_in_input_list():
    with pytest.raises(ValueError):
        numbers_filter(['a', '0', '8', '3'], 0)
