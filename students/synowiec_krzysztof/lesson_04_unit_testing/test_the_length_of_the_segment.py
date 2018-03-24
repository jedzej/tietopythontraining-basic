import pytest
from math import sqrt


# Function under test
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def test_distance_none_parameters():
    with pytest.raises(TypeError):
        distance(None, None, None, None)


def test_distance_string_parameters():
    # Test that it crashes with ValueError when called on 'aoeu' - why?
    with pytest.raises(TypeError):
        distance('aoeu', 'aoeu', 'aoeu', 'aoeu')


def test_distance_corner_case():
    assert distance(2, 2, 2, 2) == 0
    assert distance(-1, -1, -4, -5) == 5
    assert distance(0, 1, 0, 2) == 1
    assert distance(0, 1, 4, 1) == 4


def test_distance_typical_case():
    assert distance(0, 0, 3, 4) == 5


def test_distance_order_doesnt_matter():
    assert distance(0, 0, 3, 4) == distance(3, 4, 0, 0)
