import pytest
from lesson_03.the_length_of_the_segment import distance


class TestDistance(object):

    def test_1(self):
        with pytest.raises(TypeError):
            distance(None)

    def test_2(self):
        with pytest.raises(TypeError):
            distance('aoeu', 6, 2, 5)

    def test_zero(self):
        assert distance(0, 0, 0, 0) == 0

    def test_negative(self):
        assert distance(-1, -1, -3, -5) == 4.47213595499958

    def test_vertical(self):
        assert distance(3, 6, 3, 9) == 3

    def test_horizontal(self):
        assert distance(6, 8, 10, 5) == 5

    def test_typical_conditions(self):
        assert distance(4, 7, 6, 9) == 2.8284271247461903

    def test_order_of_points(self):
        assert distance(-3, 3, 1, 6) == distance(1, 6, -3, 3)
