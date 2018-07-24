import pytest
from circle import Circle, Point, Rectangle,\
    point_in_circle, rect_in_circle, rect_circle_overlap


circle = Circle(Point(150, 100), 75)
fitting_point = Point(200, 150)
not_fitting_point = Point(226, 150)
fitting_rectangle = Rectangle(Point(100, 50), 30, 20)
not_fitting_rectangle = Rectangle(Point(100, 50), 126, 20)
rect_touching_circle = Rectangle(Point(225, 75), 50, 150)
rect_not_touching_circle = Rectangle(Point(226, 25), 50, 150)
rect_lapping_circle = Rectangle(Point(200, 0), 400, 400)


@pytest.mark.parametrize("test_input, expected", [
    (fitting_point, True),
    (not_fitting_point, False),
])
def test_point_in_circle(test_input, expected):
    assert point_in_circle(circle, test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (fitting_rectangle, True),
    (not_fitting_rectangle, False),
])
def test_rect_in_circle(test_input, expected):
    assert rect_in_circle(circle, test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (rect_touching_circle, True),
    (rect_not_touching_circle, False),
    (rect_lapping_circle, True),
])
def test_circle_overlap(test_input, expected):
    assert rect_circle_overlap(circle, test_input) == expected
