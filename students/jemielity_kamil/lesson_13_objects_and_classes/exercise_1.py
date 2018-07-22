import math
import copy


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def point_in_circle(circle, point):
    distance = math.sqrt((circle.center.x - point.x) ** 2 +
                         (circle.center.y - point.y) ** 2)
    if distance <= circle.radius:
        return True
    else:
        return False


def rect_in_circle(rectangle, circle):

    copy_rectangle_point = copy.copy(rectangle.corner)
    if not point_in_circle(circle, copy_rectangle_point):
        return False

    copy_rectangle_point.x += rectangle.width
    if not point_in_circle(circle, copy_rectangle_point):
        return False

    copy_rectangle_point.y -= rectangle.height
    if not point_in_circle(circle, copy_rectangle_point):
        return False

    copy_rectangle_point.y -= rectangle.width
    if not point_in_circle(circle, copy_rectangle_point):
        return False

    return True


def rect_circle_overlap(circle, rectangle):

    copy_rectangle_point = copy.copy(rectangle.corner)
    if point_in_circle(circle, copy_rectangle_point):
        return True

    copy_rectangle_point.x += rectangle.width
    if point_in_circle(circle, copy_rectangle_point):
        return True

    copy_rectangle_point.y -= rectangle.height
    if point_in_circle(circle, copy_rectangle_point):
        return True

    copy_rectangle_point.y -= rectangle.width
    if point_in_circle(circle, copy_rectangle_point):
        return True

    return False


def main():
    point = Point(10, 10)
    circle_point = Point(150, 100)
    circle = Circle(circle_point, 75)
    rectangle = Rectangle(10, 15, point)

    print(point_in_circle(circle, point))
    print(rect_in_circle(rectangle, circle))
    print(rect_circle_overlap(circle, rectangle))


if __name__ == "__main__":
    main()
