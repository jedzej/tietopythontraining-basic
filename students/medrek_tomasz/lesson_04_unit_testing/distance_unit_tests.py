import pytest
from the_length_of_the_segment import distance


zero_length = (1, 1, 1, 1)
negative_values = (-3, -4, 0, 0)
vertical_only = (0, 1, 0, 6)
horizontal_only = (1, 0, 6, 0)
typical_points = (4, 5, 1, 1)


@pytest.mark.parametrize("test_input, expected", [
    (zero_length, 0),
    (negative_values, 5),
    (vertical_only, 5),
    (horizontal_only, 5),
    (typical_points, 5),
])
def test_eval(test_input, expected):
    assert distance(*test_input) == expected


def test_none_input():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_aoeu_input():
    with pytest.raises(TypeError):
        distance('aoeu', 'aoeu', 'aoeu', 'aoeu')


def test_if_order_of_points_matters():
    assert distance(1, 2, 3, 4) == distance(4, 3, 2, 1)
