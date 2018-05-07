import math
import pytest


def distance(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def test_typeerror_when_called_none_on_function_distance():
    """Test that it crashes with TypeError when called on None"""
    with pytest.raises(TypeError):
        distance(None, 2, 3, 4)


def test_typeerror_when_called_aoue_on_function_distance():
    """Test that it crashes with ValueError when called on 'aoeu'"""
    with pytest.raises(TypeError):
        distance('aoeu', 2, 3, 4)


def test_zero_length_on_function_distance():
    """Test zero length"""
    assert distance(1, 6, 1, 6) == 0


def test_negative_coordinates_on_function_distance():
    """Negative coordinates"""
    assert distance(-5, -10, -5, -20) == 10


def test_only_vertical_on_function_distance():
    """Only vertical distance"""
    assert distance(1, 2, 1, 4) == 2


def test_only_horizontal_on_function_distance():
    """Only horizontal distance"""
    assert distance(2, 1, 8, 1) == 6


def test_typical_conditions_on_function_distance():
    """Typical conditions"""
    assert distance(1, 3, 2, 4) == math.sqrt(2)


def test_order_no_matter_on_function_distance():
    """order of points does not matter"""
    dist1 = distance(1, 5, 8, 10)
    dist2 = distance(8, 10, 1, 5)
    assert dist1 == dist2
