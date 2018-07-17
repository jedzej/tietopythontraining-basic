import copy
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Rectangle:

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def point_in_circle(point, circle):
    return distance_between_points(point, circle.center) <= circle.radius


def rectangle_in_circle(circle, rectangle):

    point = copy.copy(rectangle.corner)

    if not point_in_circle(point, circle):
        return False

    point.x += rectangle.width
    if not point_in_circle(point, circle):
        return False

    point.y -= rectangle.height
    if not point_in_circle(point, circle):
        return False

    point.y += rectangle.height
    if not point_in_circle(point, circle):
        return False

    return True


def rectangle_circle_overlap(circle, rectangle):

    point = copy.copy(rectangle.corner)

    if point_in_circle(point, circle):
        return True

    point.x += rectangle.width
    if point_in_circle(point, circle):
        return True

    point.y -= rectangle.height
    if point_in_circle(point, circle):
        return True

    point.x -= rectangle.width
    if point_in_circle(point, circle):
        return True

    return False


def distance_between_points(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx**2 + dy**2)


def main():
    test_point = Point(20, 20)
    test_circle = Circle(Point(150, 100), 75)
    test_rectangle = Rectangle(100, 200, test_point)

    print('Point in circle: ' + str(point_in_circle(test_point, test_circle)))
    print('Rectangle in circle: ' + str(rectangle_in_circle(
        test_circle, test_rectangle)))
    print('Rectangle circle overlap: ' + str(rectangle_circle_overlap(
        test_circle, test_rectangle)))


if __name__ == '__main__':
    main()
