#!/usr/bin/env python3


import logging
from math import sqrt
from math import floor
from copy import copy


logging.basicConfig(level=logging.CRITICAL, format='%(message)s')
logger = logging.getLogger()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def distance_btwn_points(self, p2):
        return sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)


class Rectangle:
    def __init__(self, lower_left_corner=Point(0, 0), width=0, height=0):
        self.corner = lower_left_corner
        self.width = width
        self.height = height


class Circle:
    def __init__(self, center=Point(0, 0), radius=0):
        self.center = center
        self.radius = radius

    def point_in_circle(self, point):
        return distance_btwn_points(self.center, point) <= self.radius

    def rect_in_circle(self, rectangle):
        corner = copy(rectangle.corner)
        if not self.point_in_circle(corner):
            return False

        corner.x += rectangle.width
        if not self.point_in_circle(corner):
            return False

        corner.y += rectangle.height
        if not self.point_in_circle(corner):
            return False

        corner.x -= rectangle.width
        if not self.point_in_circle(corner):
            return False

        return True

    def rect_circle_overlap(self, rectangle):
        points_on_rect = []
        distances_rect_point_circ_center = []

        # We must slice rectangle fair enough to have two points lying on
        # the same side of the rectangle closest to the center of circle
        width_points = floor(20 * rectangle.width
                             / (rectangle.height + rectangle.width)
                             + 1)
        height_points = floor(20 * rectangle.height
                              / (rectangle.height + rectangle.width)
                              + 1)

        point_on_rect = copy(rectangle.corner)
        for _ in range(width_points):
            point_on_rect.x += (rectangle.width / width_points)
            points_on_rect.append(copy(point_on_rect))
        for _ in range(height_points):
            point_on_rect.y += (rectangle.height / height_points)
            points_on_rect.append(copy(point_on_rect))
        for _ in range(width_points):
            point_on_rect.x -= (rectangle.width / width_points)
            points_on_rect.append(copy(point_on_rect))
        for _ in range(height_points - 1):
            point_on_rect.y -= (rectangle.height / height_points)
            points_on_rect.append(copy(point_on_rect))

        for point in points_on_rect:
            if self.point_in_circle(point):
                return True
            distances_rect_point_circ_center.append(
                (distance_btwn_points(point, self.center), point))

        # Computing triangle's height with help of Heron's formula
        # Triangle's nodes are 1) centre of circle, 2) point on rectangle
        # closest to centre of circle, 3) second closest point
        try:
            distances_rect_point_circ_center.sort()
        except TypeError:
            pass  # sort can complain about Point if some distances are equal

        a = distances_rect_point_circ_center[0][0]
        b = distances_rect_point_circ_center[1][0]
        c = distance_btwn_points(distances_rect_point_circ_center[0][1],
                                 distances_rect_point_circ_center[1][1])

        area = sqrt((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c)) / 4
        triangle_height = 2 * area / c

        logger.debug(a)
        logger.debug(b)
        logger.debug(c)
        logger.debug(triangle_height)

        if round(self.radius, 14) >= round(triangle_height, 14):
            return True
        else:
            return False


def distance_btwn_points(point, point2):
    return point.distance_btwn_points(point2)


def point_in_circle(circle, point):
    return circle.point_in_circle(point)


def rect_in_circle(circle, rectangle):
    return circle.rect_in_circle(rectangle)


def rect_circle_overlap(circle, rectangle):
    return circle.rect_circle_overlap(rectangle)


def main():
    circle = Circle(Point(150, 100), 75)
    fitting_point = Point(200, 150)
    print(point_in_circle(circle, fitting_point))


if __name__ == "__main__":
    main()
