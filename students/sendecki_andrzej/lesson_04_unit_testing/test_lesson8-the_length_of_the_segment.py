#    Test that it crashes with TypeError when called on None (use pytest.raises),
#    Test that it crashes with ValueError when called on 'aoeu',
#    Test it on corner cases:
#        Zero length,
#        Negative coordinates,
#        Only vertical distance,
#        Only horizontal distance,
#    Typical conditions (difference on both coordinates),
#    Test that the order of points does not matter.


import pytest
import math

def distance(x1, y1, x2, y2):

    return math.sqrt( pow((x2-x1), 2) + pow((y2-y1), 2) )


def test_TypeError_exception():
    with pytest.raises(TypeError):
        distance(None, None, None, None)

# Principals of the test below are wrong -
# in this case the function raises "TypeError"
# Test will fail.
def test_ValueError_exception():
    with pytest.raises(ValueError):
        distance("aoeu",1,1,1)

def test_zero_length():
    assert distance(1,1,1,1) == 0

def test_negative_coordinates():
    assert distance(-1,-1,-2,-2) == 1.4142135623730951

def test_only_vertical_distance():
    assert distance(1,1,1,2) == 1

def test_only_horizontal_distance():
    assert distance(1,1,2,1) == 1

def test_typical_conditions():
    assert distance(1,1,2,2) == 1.4142135623730951

def test_order_of_points_does_not_matter():
    d1 = distance(1,1,2,2)
    d2 = distance(2,2,1,1)
    assert d1 == d2



