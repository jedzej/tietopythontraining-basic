import math
import pytest
from lesson_03.length_of_the_segment import distance


class TestDistanceFunction(object):

    def test_input_none(self):
        with pytest.raises(TypeError):
            distance(None, 1, 2, 3)

    def test_input_string(self):
        with pytest.raises(TypeError):
            distance('aoeu', 1, 2, 3)

    def test_zero_distance(self):
        assert distance(1, 1, 1, 1) == 0

    def test_corner_cases(self):
        assert distance(-1, -1, -2, -2) == math.sqrt(2)
        assert distance(0, 1, 0, 2) == 1
        assert distance(1, 0, 2, 0) == 1

    def test_typical_conditions(self):
        assert distance(1, 2, 3, 4) == math.sqrt(8)

    def test_order_of_points(self):
        assert distance(1, 2, 3, 4) == distance(3, 4, 1, 2)
        assert distance(5, 6, 7, 8) == distance(7, 8, 5, 6)
