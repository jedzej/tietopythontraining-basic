#!/usr/bin/env python3


from students.piechowski_michal.lesson_03_functions.the_length_of_the_segment import distance


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Rectangle:
    top_left_corner = Point(0, 0)
    width = 0
    height = 0

    def __init__(self, top_left_corner, width, height):
        self.top_left_corner = top_left_corner
        self.width = width
        self.height = height

    def __str__(self):
        return "[top left: " + str(self.top_left_corner) +\
               ", width: " + str(self.width) +\
               ", height: " + str(self.height) + "]"


class Circle:
    center = Point(0, 0)
    radius = 0

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "(center: " + str(self.center) + ", r: " + str(self.radius) + ")"

    def is_point_in_circle(self, point):
        return distance(self.center.x, self.center.y, point.x, point.y) <= self.radius

    def is_rectangle_in_circle(self, rectangle):
        top_right = Point(rectangle.top_left_corner.x + rectangle.width,
                          rectangle.top_left_corner.y)

        bottom_left = Point(rectangle.top_left_corner.x,
                            rectangle.top_left_corner.y - rectangle.height)

        bottom_right = Point(rectangle.top_left_corner.x + rectangle.width,
                             rectangle.top_left_corner.y - rectangle.height)

        return (self.is_point_in_circle(rectangle.top_left_corner) and
                self.is_point_in_circle(top_right) and
                self.is_point_in_circle(bottom_left) and
                self.is_point_in_circle(bottom_right))

    def is_rectangle_overlapping_circle(self, rectangle):
        top_right = Point(rectangle.top_left_corner.x + rectangle.width,
                          rectangle.top_left_corner.y)

        bottom_left = Point(rectangle.top_left_corner.x,
                            rectangle.top_left_corner.y - rectangle.height)

        bottom_right = Point(rectangle.top_left_corner.x + rectangle.width,
                             rectangle.top_left_corner.y - rectangle.height)

        return (self.is_point_in_circle(rectangle.top_left_corner) or
                self.is_point_in_circle(top_right) or
                self.is_point_in_circle(bottom_left) or
                self.is_point_in_circle(bottom_right))


def point_in_circle(circle, point):
    return circle.is_point_in_circle(point)


def rect_in_circle(circle, rectangle):
    return circle.is_rectangle_in_circle(rectangle)


def rect_circle_overlap(circle, rectangle):
    return circle.is_rectangle_overlapping_circle(rectangle)


def main():
    circle = Circle(Point(150, 100), 75)

    points = [Point(0, 0), Point(100, 100), Point(150, 75), Point(200, 300)]

    print("Checking if points are in circle\n")
    for point in points:
        print("Is point " + str(point))
        print("In circle " + str(circle))
        print("-> " + str(point_in_circle(circle, point)) + "\n")

    rectangles = [Rectangle(Point(0, 0), 1000, 1000),
                  Rectangle(Point(100, 100), 50, 50),
                  Rectangle(Point(300, 300), 1, 1),
                  Rectangle(Point(100, 100), 75, 75)]

    print("Checking if rectangles are in circle\n")
    for rectangle in rectangles:
        print("Is rectangle " + str(rectangle))
        print("In circle " + str(circle))
        print("-> " + str(rect_in_circle(circle, rectangle)) + "\n")

    print("Checking if rectangles overlap circle\n")
    for rectangle in rectangles:
        print("Is rectangle " + str(rectangle))
        print("In circle " + str(circle))
        print("-> " + str(rect_circle_overlap(circle, rectangle)) + "\n")


if __name__ == "__main__":
    main()
