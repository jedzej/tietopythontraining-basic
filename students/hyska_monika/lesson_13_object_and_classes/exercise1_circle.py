"""
Write a definition for a class named Circle with
attributes center and radius, where center is a Point
object and radius is a number.

Instantiate a Circle object that represents a circle
with its center at (150, 100) and radius 75.

Write a function named point_in_circle that takes a Circle
and a Point and returns True if the Point lies in or on the
boundary of the circle.

Write a function named rect_in_circle that takes a Circle and
a Rectangle and returns True if the Rectangle lies entirely
in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and
a Rectangle and returns True if any of the corners of the Rectangle
fall inside the circle. Or as a more challenging version,
return True if any part of the Rectangle falls inside the circle.
"""


import math


class Point:
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Rectangle:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.tL = topLeft
        self.tR = topRight
        self.bL = bottomLeft
        self.bR = bottomRight


def point_in_circle(point, circle):
    distance_between_points = math.sqrt((point.x - circle.center.x) ** 2 +
                                        (point.y - circle.center.y) ** 2)
    return distance_between_points <= circle.radius


def point_in_circle_bounduary(point, circle):
    distance_between_points = math.sqrt((point.x - circle.center.x) ** 2 +
                                        (point.y - circle.center.y) ** 2)
    return distance_between_points == circle.radius


def rect_circle(rectangle, circle):
    check_tL = point_in_circle_bounduary(rectangle.tL, circle)
    check_tR = point_in_circle_bounduary(rectangle.tR, circle)
    check_bL = point_in_circle_bounduary(rectangle.bL, circle)
    check_bR = point_in_circle_bounduary(rectangle.bL, circle)
    return check_tL and check_tR and check_bL and check_bR


def rect_circle_overlap(rectangle, circle):
    check_tL = point_in_circle(rectangle.tL, circle)
    check_tR = point_in_circle(rectangle.tR, circle)
    check_bL = point_in_circle(rectangle.bL, circle)
    check_bR = point_in_circle(rectangle.bL, circle)
    return check_tL and check_tR and check_bL and check_bR


def main():
    point1 = Point(370, 550)
    circle_center = Point(150, 100)
    my_circle = Circle(circle_center, 75)
    print('Is point(%s, %s) in the circle(center=(%s, %s), radious=%s)?'
          % (point1.x, point1.y, circle_center.x, circle_center.y,
             my_circle.radius))
    print(point_in_circle(point1, my_circle))

    # rectangle in circle
    # rectangle1 = Rectangle(Point(1,10),Point(6,10), Point(1,5), Point(6,5))
    rectangles_points = (Point(-2, 2), Point(2, 2),
                         Point(-2, -2), Point(2, -2))
    rectangle2 = Rectangle(*rectangles_points)
    circle_center = Point(0, 0)
    my_circle2 = Circle(circle_center, math.sqrt(8))
    print('Is rectangle:((%s,%s),(%s,%s),(%s,%s),(%s,%s)) in the circle'
          '(center=(%s, %s),radius=%s) board?'
          % (rectangle2.tL.x, rectangle2.tL.y,
             rectangle2.tR.x, rectangle2.tR.y,
             rectangle2.bL.x, rectangle2.bL.y,
             rectangle2.bL.x, rectangle2.bL.y,
             circle_center.x, circle_center.y, my_circle2.radius))
    print(rect_circle(rectangle2, my_circle2))

    # rectangle in circle overlap
    # rectangle1 = Rectangle(Point(1,10),Point(6,10), Point(1,5), Point(6,5))
    rectangles_points = (Point(1, 10), Point(6, 10), Point(1, 5), Point(6, 5))
    rectangle2 = Rectangle(*rectangles_points)
    circle_center = Point(2, 3)
    my_circle2 = Circle(circle_center, 20)
    print('Is rectangle:((%s,%s),(%s,%s),(%s,%s),(%s,%s)) in the circle'
          '(center=(%s, %s),radius=%s)?'
          % (rectangle2.tL.x, rectangle2.tL.y, rectangle2.tR.x, rectangle2.tR.y,
             rectangle2.bL.x, rectangle2.bL.y, rectangle2.bL.x, rectangle2.bL.y,
             circle_center.x, circle_center.y, my_circle.radius))
    print(rect_circle_overlap (rectangle2, my_circle2))


if __name__ == "__main__":
    main()
