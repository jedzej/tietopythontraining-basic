#!/usr/bin/env python3
"""Objects: exercise 1"""

import math
import copy


class Point:
    """Point representation in 2D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Circle:
    """Circle class"""
    def __init__(self, center, radius):
        self.c = center
        self.r = radius

    def __str__(self):
        return 'center at {}: radius {}'.format(self.c, self.r)


class Rectangle:
    """Circle class"""
    def __init__(self, corner, height, width):
        self.c = corner
        self.h = height
        self.w = width

    def __str__(self):
        return 'corner {}: w {} : h {}'.format(self.c, self.w, self.h)


def point_in_circle(point, circle):
    """Checks if point is in circle"""
    dist = math.sqrt((point.x - circle.c.x)**2 + (point.y - circle.c.y)**2)
    return dist <= circle.r


def rect_in_circle(rect, circle):
    """Checks if rectangle is in circle"""
    p = copy.copy(rect.c)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.w
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.h
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.w
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks if rectangle overlaps circle"""
    p = copy.copy(rect.c)
    if point_in_circle(p, circle):
        return True

    p.x += rect.w
    if point_in_circle(p, circle):
        return True

    p.y -= rect.h
    if point_in_circle(p, circle):
        return True

    p.x -= rect.w
    if point_in_circle(p, circle):
        return True

    return False


def main():
    """Main function"""
    point_1 = Point(100, 50)
    point_2 = Point(10, 10)
    rect_1 = Rectangle(point_1, 5, 5)
    rect_2 = Rectangle(point_2, 10, 10)
    circle = Circle(Point(150, 100), 75)

    print(circle)
    print(rect_1)
    print(rect_2)

    print('Point {} in circle: {} : {}'.
          format(point_1, circle, point_in_circle(point_1, circle)))
    print('Point {} in circle: {} : {}'.
          format(point_2, circle, point_in_circle(point_2, circle)))
    print('Rect {} is in circle {} : {}'.
          format(rect_1, circle, rect_in_circle(rect_1, circle)))
    print('Rect {} is in circle {} : {}'.
          format(rect_2, circle, rect_in_circle(rect_2, circle)))

    print('Rect {} overlaps circle {} : {}'.
          format(rect_1, circle, rect_circle_overlap(rect_1, circle)))
    print('Rect {} overlaps circle {} : {}'.
          format(rect_2, circle, rect_circle_overlap(rect_2, circle)))


if __name__ == '__main__':
    main()
