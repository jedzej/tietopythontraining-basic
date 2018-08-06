import math


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, corner, height, width):
        self.corner = corner
        self.height = height
        self.width = width


def point_in_circle(circle, point):
    if (math.sqrt((circle.center.x - point.x) ** 2 +
                  (circle.center.y - point.y) ** 2)) <= circle.radius:
        return True
    else:
        return False


def corner_point(rectangle):
    second = Point
    third = Point
    fourth = Point
    second.x = rectangle.corner.x
    second.y = rectangle.corner.y + rectangle.height
    third.x = rectangle.corner.x + rectangle.width
    third.y = second.y
    fourth.x = third.x
    fourth.y = rectangle.corner.y
    return second, third, fourth


def rect_in_circle(circle, rectangle):
    corner1 = rectangle.corner
    corner2, corner3, corner4 = corner_point(rectangle)

    if (math.sqrt((circle.center.x - corner1.x) ** 2 +
                  (circle.center.y - corner1.y) ** 2)) > circle.radius:
        return False
    elif (math.sqrt((circle.center.x - corner2.x) ** 2 +
                    (circle.center.y - corner2.y) ** 2)) > circle.radius:
        return False
    elif (math.sqrt((circle.center.x - corner3.x) ** 2 +
                    (circle.center.y - corner3.y) ** 2)) > circle.radius:
        return False
    elif (math.sqrt((circle.center.x - corner4.x) ** 2 +
                    (circle.center.y - corner4.y) ** 2)) > circle.radius:
        return False
    else:
        return True


def rect_circle_overlap(circle, rectangle):
    corner1 = rectangle.corner
    corner2, corner3, corner4 = corner_point(rectangle)

    if (math.sqrt((circle.center.x - corner1.x) ** 2 +
                  (circle.center.y - corner1.y) ** 2)) < circle.radius:
        return True
    elif (math.sqrt((circle.center.x - corner2.x) ** 2 +
                    (circle.center.y - corner2.y) ** 2)) < circle.radius:
        return True
    elif (math.sqrt((circle.center.x - corner3.x) ** 2 +
                    (circle.center.y - corner3.y) ** 2)) < circle.radius:
        return True
    elif (math.sqrt((circle.center.x - corner4.x) ** 2 +
                    (circle.center.y - corner4.y) ** 2)) < circle.radius:
        return True
    else:
        return False


def main():
    center_circle = Point(150, 100)
    circle = Circle(center_circle, 75)
    corner = Point(150, 100)
    rectangle = Rectangle(corner, 50, 50)
    point = Point(10, 100)

    if point_in_circle(circle, point):
        print("True - the Point lies in or on the boundary of the circle.")
    else:
        print("False - the Point doesn't lay in "
              "or on the boundary of the circle.")

    if rect_in_circle(circle, rectangle):
        print("True - the Rectangle lies entirely in "
              "or on the boundary of the circle.")
    else:
        print("True - the Rectangle doesn't lay entirely in "
              "or on the boundary of the circle.")

    if rect_circle_overlap(circle, rectangle):
        print("True - any of the corners of the Rectangle fall inside "
              "the circle.")
    else:
        print("False - the corners of the Rectangle are outside the circle")


if __name__ == '__main__':
    main()
