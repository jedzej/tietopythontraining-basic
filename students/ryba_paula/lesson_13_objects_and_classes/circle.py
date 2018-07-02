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


def distance_between_points(first, second):
    dx = first.x - second.x
    dy = first.y - second.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance


def point_in_circle(circle, point):
    center = circle.center
    radius = circle.radius
    return distance_between_points(center, point) <= radius


def rectangle_points(rect):
    d_left = rect.corner
    d_right = Point(d_left.x + rect.width, d_left.y)
    u_right = Point(d_right.x, d_right.y + rect.height)
    u_left = Point(d_left.x, rect.height + d_left.y)

    points = [d_left, d_right, u_left, u_right]

    return points


def rect_in_circle(circle, rect):
    points = rectangle_points(rect)

    for p in points:
        if not point_in_circle(circle, p):
            return False

    return True


def rect_circle_overlap(circle, rect):
    points = rectangle_points(rect)

    for p in points:
        if point_in_circle(circle, p):
            return True

    return False


def main():
    circle = Circle(Point(150, 100), 75)
    point = Point(100, 100)
    rectangle = Rectangle(100, 10, point)

    print("Circle: ", circle.__dict__)
    print("Point: ", point.__dict__)
    print("Rectangle: ", rectangle.__dict__)
    print("Is point in the circle? ", point_in_circle(circle, point))
    print("Is rectangle in the circle? ", rect_in_circle(circle, rectangle))
    print("Does rectangle overlap the circle? ",
          rect_circle_overlap(circle, rectangle))


if __name__ == '__main__':
    main()
