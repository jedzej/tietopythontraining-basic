import copy
import math


class Point:
    """Represents a point in 2-D space.

    @param x: X-axis coordinate.
    @type x: float
    @param y: Y-axis coordinate.
    @type y: float
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    """Represents a circle.

    @param center: The center point of the circle.
    @type center: Point
    @param radius: length of the line from the center to any point on its edge.
    @type radius: float
    """
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Rectangle:
    """Represents a rectangle in 2-D space.

    @param width: Rectangle's X-axis length.
    @type width: int
    @param height: Rectangle's Y-axis length.
    @type height: int
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    :param p1: First Point.
    :type p1: Point
    :param p2: Second Point.
    :type p2: Point
    :return: Distance between two Points.
    :rtype: float
    """

    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist


def point_in_circle(point, circle):
    """Takes a Circle and a Point and returns True if the Point lies
    in or on the boundary of the circle."""
    d = distance_between_points(point, circle.center)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Takes a Circle and a Rectangle and returns True if the Rectangle lies
    entirely in or on the boundary of the circle."""

    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Takes a Circle and a Rectangle and returns True if any of the corners
    of the Rectangle fall inside the circle."""

    p = copy.copy(rect.corner)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True

    return False


def main():
    point = Point(50.0, 50.0)
    box = Rectangle(100, 200, point)
    circle = Circle(Point(150.0, 100.0), 75.0)

    print(point_in_circle(point, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
