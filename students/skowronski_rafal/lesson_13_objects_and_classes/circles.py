import math


class Point:
    """Represents a point.

    attributes: x, y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    """Represents a circle.

    attributes: center, radius
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Rectangle:
    """Represents a rectangle.

    attributes: origin, width, height
    """
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def get_top_left_corner(self):
        return self.origin

    def get_top_right_corner(self):
        return Point(self.origin.x + self.width, self.origin.y)

    def get_bottom_left_corner(self):
        return Point(self.origin.x, self.origin.y + self.height)

    def get_bottom_right_corner(self):
        return Point(self.origin.x + self.width, self.origin.y + self.height)


def _is_point_in_circle(point, circle):
    center = circle.center
    distance = math.hypot(center.x - point.x, center.y - point.y)
    return distance <= circle.radius


def point_in_circle(point, circle):
    return _is_point_in_circle(point, circle)


def rect_in_circle(rect, circle):
    return _is_point_in_circle(rect.get_top_left_corner(), circle) \
        and _is_point_in_circle(rect.get_top_right_corner(), circle) \
        and _is_point_in_circle(rect.get_bottom_left_corner(), circle) \
        and _is_point_in_circle(rect.get_bottom_right_corner(), circle)


def rect_circle_overlap(rect, circle):
    return _is_point_in_circle(rect.get_top_left_corner(), circle) \
        or _is_point_in_circle(rect.get_top_right_corner(), circle) \
        or _is_point_in_circle(rect.get_bottom_left_corner(), circle) \
        or _is_point_in_circle(rect.get_bottom_right_corner(), circle)


if __name__ == '__main__':
    box = Rectangle(Point(50, 50), 100, 200)
    print(box.origin.x)
    print(box.origin.y)

    circle = Circle(Point(150, 100), 75)
    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.origin, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))
