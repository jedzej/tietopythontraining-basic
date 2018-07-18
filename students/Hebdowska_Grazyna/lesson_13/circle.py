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

    def __init__(self, one_corner, height, width):
        self.one_corner = one_corner
        self.height = height
        self.width = width


def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def point_in_circle(circle, point):
    if distance(circle.center, point) <= circle.radius:
        return True
    else:
        return False


def corner_point(rectangle):
    secound = Point
    third = Point
    fourth = Point
    secound.x = rectangle.one_corner.x
    secound.y = rectangle.one_corner.y + rectangle.height
    third.x = rectangle.one_corner.x + rectangle.width
    third.y = secound.y
    fourth.x = third.x
    fourth.y = rectangle.one_corner.y
    return secound, third, fourth


def rect_in_circle(circle, rectangle):
    p1 = rectangle.one_corner
    p2, p3, p4 = corner_point(rectangle)
    if distance(circle.center, p1) > circle.radius:
        return False
    elif distance(circle.center, p2) > circle.radius:
        return False
    elif distance(circle.center, p3) > circle.radius:
        return False
    elif distance(circle.center, p4) > circle.radius:
        return False
    else:
        return True


def rect_circle_overlap(cicle, rectangle):
    p1 = rectangle.one_corner
    p2, p3, p4 = corner_point(rectangle)
    if distance(cicle.center, p1) < cicle.radius:
        return True
    elif distance(cicle.center, p2) < cicle.radius:
        return True
    elif distance(cicle.center, p3) < cicle.radius:
        return True
    elif distance(cicle.center, p4) < cicle.radius:
        return True
    else:
        return False


def main():
    circle_center = Point(150, 100)
    circle = Circle(circle_center, 75)
    one_corner = Point(1, 50)
    rectangle = Rectangle(one_corner, 20, 50)
    point = Point(9, 120)
    if point_in_circle(circle, point):
        print("the Point lies in"
              " or on the boundary of the circle.")
    else:
        print("the Point doesn't lay"
              " in or on the boundary of the circle.")

    if rect_in_circle(circle, rectangle):
        print("the Rectangle lies entirely"
              " in or on the boundary of the circle.")
    else:
        print("the Rectangle doesn't lay entirely"
              " in or on the boundary of the circle.")

    if rect_circle_overlap(circle, rectangle):
        print("some of the corners"
              " of the Rectangle fall inside the circle")
    else:
        print("the corners of the Rectangle"
              " are outside the circle")


if __name__ == '__main__':
    main()
