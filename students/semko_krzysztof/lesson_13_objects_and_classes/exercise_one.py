"""
Write a definition for a class named Circle with attributes
center and radius, where center is a Point object and radius
is a number.

Instantiate a Circle object that represents a circle
with its center at (150, 100) and radius 75.

Write a function named point_in_circle that takes a Circle
and a Point and returns True if the Point lies in or
on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle
and a Rectangle and returns True if the Rectangle lies
entirely in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes
a Circle and a Rectangle and returns True if any of the
corners of the Rectangle fall inside the circle.
Or as a more challenging version, return True if any
part of the Rectangle falls inside the circle.
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius


class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def point_in_circle(circle, point):
    distance = math.sqrt(
        pow(point.x - circle.center.x, 2) +
        pow(point.y - circle.center.y, 2))
    return circle.radius > distance


def rect_in_circle(circle, rectangle):
    point_width = Point(rectangle.corner.x + rectangle.width,
                        rectangle.corner.y)
    point_height = Point(rectangle.corner.x,
                         rectangle.corner.y + rectangle.height)
    point_opposite = Point(rectangle.corner.x + rectangle.width,
                           rectangle.corner.y + rectangle.height)
    return (point_in_circle(circle, rectangle.corner) and
            point_in_circle(circle, point_width) and
            point_in_circle(circle, point_height) and
            point_in_circle(circle, point_opposite))


def rect_circle_overlap(circle, rectangle):
    point_width = Point(rectangle.corner.x + rectangle.width,
                        rectangle.corner.y)
    point_height = Point(rectangle.corner.x,
                         rectangle.corner.y + rectangle.height)
    point_opposite = Point(rectangle.corner.x + rectangle.width,
                           rectangle.corner.y + rectangle.height)
    return (point_in_circle(circle, rectangle.corner) or
            point_in_circle(circle, point_width) or
            point_in_circle(circle, point_height) or
            point_in_circle(circle, point_opposite))


def main():
    """
    Example of functions use:
    """
    circle = Circle(150, 100, 75)
    point = Point(226, 100)
    rectangle_corner = Point(150, 100)
    rectangle = Rectangle(100, 50, rectangle_corner)

    print(point_in_circle(circle, point))
    print(rect_in_circle(circle, rectangle))
    print(rect_circle_overlap(circle, rectangle))


if __name__ == '__main__':
    main()
