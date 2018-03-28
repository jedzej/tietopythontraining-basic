import pytest
import math
from the_length_of_the_segment import distance


class TestDistanceFunction(object):
    def test_none_as_first_parameter(self):
        with pytest.raises(TypeError):
            distance(None, 1, 2, 2)

    def test_none_as_second_parameter(self):
        with pytest.raises(TypeError):
            distance(1, None, 2, 2)

    def test_none_as_third_parameter(self):
        with pytest.raises(TypeError):
            distance(1, 1, None, 2)

    def test_none_as_fourth_parameter(self):
        with pytest.raises(TypeError):
            distance(1, 1, 2, None)

    def test_string_as_first_parameter(self):
        with pytest.raises(TypeError):
            distance('aoeu', 1, 2, 2)

    def test_string_as_second_parameter(self):
        with pytest.raises(TypeError):
            distance(1, 'aoeu', 2, 2)

    def test_string_as_third_parameter(self):
        with pytest.raises(TypeError):
            distance(1, 1, 'aoeu', 2)

    def test_string_as_fourth_parameter(self):
        with pytest.raises(TypeError):
            distance(1, 1, 2, 'aoeu')

    def test_zero_length(self):
        assert distance(1, 1, 1, 1) == 0

    def test_only_vertical_distance(self):
        assert distance(5, 3, 5, 1) == 2

    def test_only_horizontal_distance(self):
        assert distance(3, 2, 7, 2) == 4

    def test_different_points_1(self):
        assert math.isclose(distance(1, 1, 2, 2), math.sqrt(2))

    def test_different_points_2(self):
        assert math.isclose(distance(0, 5, 1, 3), math.sqrt(5))

    def test_order_of_points(self):
        assert distance(1, 1, 4, 5) == distance(4, 5, 1, 1)
