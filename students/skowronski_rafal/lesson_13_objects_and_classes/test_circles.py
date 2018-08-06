import pytest
from circles import Point
from circles import Circle
from circles import Rectangle
from circles import point_in_circle
from circles import rect_in_circle
from circles import rect_circle_overlap


class TestCircles():
    circle_test_data = [
        (Point(0, 0), Circle(Point(0, 0), 10), True),
        (Point(10, 0), Circle(Point(0, 0), 10), True),
        (Point(5, 5), Circle(Point(0, 0), 10), True),
        (Point(37, 25), Circle(Point(30, 18), 10), True),
        (Point(37, 25), Circle(Point(27, 15), 10), False)
    ]

    rect1_test_data = [
        (Rectangle(Point(0, 0), 3, 4), Circle(Point(0, 0), 5), True),
        (Rectangle(Point(0, 0), 3, 4), Circle(Point(0, 0), 4), False),
        (Rectangle(Point(100, 100), 3, 4), Circle(Point(100, 100), 6), True),
        (Rectangle(Point(0, 0), 3, 4.5), Circle(Point(0, 0), 5), False),
        (Rectangle(Point(-3, 0), 3, 4.5), Circle(Point(0, 0), 5), False),
        (Rectangle(Point(0, -4.5), 3, 4.5), Circle(Point(0, 0), 5), False),
        (Rectangle(Point(-3, -4.5), 3, 4.5), Circle(Point(0, 0), 5), False),
        (Rectangle(Point(-3, -4), 3, 4), Circle(Point(0, 0), 5), True),
    ]

    rect2_test_data = [
        (Rectangle(Point(0, 0), 3, 4), Circle(Point(4, 5), 1), False),
        (Rectangle(Point(0, 0), 3, 4.5), Circle(Point(0, 0), 5), True),
        (Rectangle(Point(-3, 0), 3, 4.5), Circle(Point(0, 0), 5), True),
        (Rectangle(Point(0, -4.5), 3, 4.5), Circle(Point(0, 0), 5), True),
        (Rectangle(Point(-3, -4.5), 3, 4.5), Circle(Point(0, 0), 5), True),
        (Rectangle(Point(-3, -4), 3, 4), Circle(Point(0, 0), 5), True),
    ]

    @pytest.mark.parametrize('point, circle, expected', circle_test_data)
    def test_point_in_circle_on_test_data(self, point, circle, expected):
        assert point_in_circle(point, circle) == expected

    @pytest.mark.parametrize('rect, circle, expected', rect1_test_data)
    def test_rect_in_circle_on_test_data(self, rect, circle, expected):
        assert rect_in_circle(rect, circle) == expected

    @pytest.mark.parametrize('rect, circle, expected', rect2_test_data)
    def test_rect_circle_overlap_on_test_data(self, rect, circle, expected):
        assert rect_circle_overlap(rect, circle) == expected
