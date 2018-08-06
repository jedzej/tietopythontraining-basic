import math


def distance(p1, p2):
    return math.sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


def point_in_circle(circle, point):
    """ Function named point_in_circle that takes a Circle
    and a Point and returns True if the Point lies in
    or on the boundary of the circle."""

    return circle.radius >= distance(circle.center, point)


def rect_in_circle(circle, rect):
    """ Function named rect_in_circle that takes a Circle and
    a Rectangle and returns True if the Rectangle lies entirely
    in or on the boundary of the circle."""

    result = True
    result &= circle.radius >= distance(circle.center, rect.p1)
    result &= circle.radius >= distance(circle.center, rect.p2)
    result &= circle.radius >= distance(circle.center, rect.p3)
    result &= circle.radius >= distance(circle.center, rect.p4)
    return result


def rect_circle_overlap(circle, rect):
    """ Function named rect_circle_overlap that takes a Circle
    and a Rectangle and returns True if any of the corners of the
    Rectangle fall inside the circle. Or as a more challenging
    version, return True if any part of the Rectangle falls inside
    the circle."""
    result = False
    result |= circle.radius >= distance(circle.center, rect.p1)
    result |= circle.radius >= distance(circle.center, rect.p2)
    result |= circle.radius >= distance(circle.center, rect.p3)
    result |= circle.radius >= distance(circle.center, rect.p4)
    return result


def main():
    circle = Circle(Point(150, 100), 75)
    point = Point(150, 100)

    if point_in_circle(circle, point):
        print("Point({0},{1}) is in circle".format(point.x, point.y))
    else:
        print("Point({0},{1}) is outside circle".format(point.x, point.y))

    rectangle = Rectangle(Point(150, 100),
                          Point(200, 100),
                          Point(200, 150),
                          Point(150, 150))

    if rect_in_circle(circle, rectangle):
        print("Rectangle is in circle")
    else:
        print("Rectangle is outside circle")

    rectangle2 = Rectangle(Point(150, 100),
                           Point(2000, 1000),
                           Point(2000, 1500),
                           Point(1500, 1500))

    if rect_circle_overlap(circle, rectangle2):
        print("Rectangle is in circle")
    else:
        print("Rectangle is outside circle")


if __name__ == '__main__':
    main()
