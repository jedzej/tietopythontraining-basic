#!/usr/bin/env python3

"""
geometric_figures.py: a practice project "Exercise 1" from:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import math


class Point:
    """
    Class representing a 2D point

    Attributes:
        x (float): the X coordinate
        y (float): the Y coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Circle:
    """
    Class representing a circle

    Attributes:
        center (Point): the center point of the circle
        radius (float): the radius of the circle
    """
    def __init__(self, center, radius):
        self.center = center.copy()
        self.radius = radius

    def __str__(self):
        return "({}, {})".format(self.center, self.radius)


class Rectangle:
    """
    Class representing a rectangle

    Attributes:
        left_down (float): the left down corner of the rectangle
        top_right (float): the top right corner of the rectangle
    """
    def __init__(self, left_down, top_right):
        self.left_down = left_down.copy()
        self.top_right = top_right.copy()

    def __str__(self):
        return "({}, {})".format(self.left_down, self.top_right)


def point_in_circle(circle, point):
    """
    This function determines if the point lies in or on the boundary of
    the circle
    :param Circle circle: a Circle object
    :param Point point: a Point object
    :return bool: True if the point lies in or on the boundary of the circle
    """
    return point.distance(circle.center) <= circle.radius


def rect_in_circle(circle, rect):
    """
    This function checks if the rectangle lies in the circle
    :param Circle circle: a Circle object
    :param Rectangle rect: a Rectangle object
    :return bool:  True if the Rectangle lies entirely in or on the boundary
    of the circle
    """
    return point_in_circle(circle, rect.left_down) and point_in_circle(
        circle, rect.top_right)


def rect_circle_overlap(circle, rect):
    """
    This function checks if the rectangle and the circle overlaps
    :param Circle circle: a Circle object
    :param Rectangle rect: a Rectangle object
    :return bool: True if any of the corners of the rectangle fall inside
    the circle
    """
    top_left = Point(rect.left_down.x, rect.top_right.y)
    right_down = Point(rect.top_right.x, rect.left_down.y)
    for p in [rect.top_right, rect.left_down, top_left, right_down]:
        if point_in_circle(circle, p):
            return True

    return False


def main():

    points = [Point(180, 130), Point(200, 150), Point(220, 180),
              Point(260, 210), Point(300, 250)]

    circle = Circle(points[1], 50)

    rectangles = [Rectangle(points[0], points[2]),
                  Rectangle(points[2], points[3]),
                  Rectangle(points[3], points[4])]

    for point in points:
        print("Point {} in the circle {}: {}".format(point, circle,
              point_in_circle(circle, point)))

    for rect in rectangles:
        print("Rectangle {} in Circle {}: {}"
              .format(rect, circle, rect_in_circle(circle, rect)))
        print("Rectangle {} and Circle {} overlap: {}"
              .format(rect, circle, rect_circle_overlap(circle, rect)))


if __name__ == '__main__':
    main()
