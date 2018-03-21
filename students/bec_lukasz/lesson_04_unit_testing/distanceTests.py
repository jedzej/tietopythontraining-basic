import pytest
import math


def distance(x1, y1, x2, y2):
    if x1 is not float(x1) and x1 is not int(x1):
        raise ValueError
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

'''
x1 = float(input('x1:'))
y1 = float(input('y1:'))
x2 = float(input('x2:'))
y2 = float(input('y2:'))

print(distance(x1, y1, x2, y2))

'''


def test_type_error_none_called():
    with pytest.raises(TypeError):
        distance(None)


def test_value_error_aoeu_called():
    with pytest.raises(ValueError):
        distance('aoeu', None, None, None)


def test_zero_length():
    assert distance(0, 0, 0, 0) == 0


def test_negative_coordinates():
    assert distance(-1, -1, -3, -5) == 4.47213595499958


def test_only_vertical_values():
    assert distance(0, 2, 0, 4) == 2


def test_only_horizontal_values():
    assert distance(2, 0, 3, 0) == 1


def test_typical_values():
    assert distance(2, 4, 6, 8) == 5.656854249492381


def test_order_of_argumetns():
    x1 = 2
    y1 = 4
    x2 = 6
    y2 = 8
    assert distance(x2, y2, x1, y1) == distance(x1, y1, x2, y2)
