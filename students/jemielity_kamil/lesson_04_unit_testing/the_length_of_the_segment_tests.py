import pytest
import math
from students.jemielity_kamil.lesson_03_functions.the_length_of_the_segment import distance


class TestClass(object):

    def test_none_value(self):
        with pytest.raises(TypeError):
            distance(None, None, None, None)

    def test_string_value(self):
        with pytest.raises(TypeError):
            distance('aoeu', 'aoeu', 'aoeu', 'aoeu')

    def test_zero_length(self):
        assert distance(0, 0, 0, 0) == 0

    def test_negative_coordinates(self):
        total_distance = distance(-2, -3, -5, -6)
        total_distance = math.floor(total_distance * 1000)/1000
        assert total_distance == 4.242

    def test_vertical_distance(self):
        assert distance(5, 3, 8, 3) == 3.0

    def test_horizontal_distance(self):
        assert distance(5, 7, 5, 3) == 4.0

    def test_typical_conditions(self):
        total_distance = distance(1.9, 1.7, 5.2, 3.6)
        total_distance = math.floor(total_distance * 1000) / 1000
        assert total_distance == 3.807

    def test_order_of_points(self):
        assert distance(1, 7, 2, 4) == distance(2, 4, 1, 7)
