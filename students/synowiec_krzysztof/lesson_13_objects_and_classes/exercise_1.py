import math


def main():
    center = Point(150, 100)
    radius = 75
    circle = Circle(center, radius)
    first_point = Point(100, 100)
    second_point = Point(300, 300)

    point_inside = point_in_circle(circle, first_point)
    print("{} inside {} {}"
          .format(first_point, circle, point_inside))

    point_inside = point_in_circle(circle, second_point)
    print("{} inside {} {}"
          .format(second_point, circle, point_inside))

    first_rect = Rectangle(Point(150, 100), 10, 20)
    second_rect = Rectangle(Point(150, 100), 200, 100)

    rectangle_inside = rectangle_in_circle(first_rect, circle)
    print("{} inside {} {}".format(first_rect, circle, rectangle_inside))

    rectangle_inside = rectangle_in_circle(second_rect, circle)
    print("{} inside {} {}".format(second_rect, circle, rectangle_inside))


def distance_between_points(start, end):
    diff_x = start.x - end.x
    diff_y = start.y - end.y
    distance = math.sqrt(diff_x ** 2 + diff_y ** 2)
    return distance


def point_in_circle(circle, point):
    center = circle.center
    radius = circle.radius
    return distance_between_points(center, point) <= radius


def calculate_rectangle_corners(rectangle):
    bottom_left = rectangle.corner
    bottom_right = Point(bottom_left.x + rectangle.width, bottom_left.y)
    top_right = Point(bottom_right.x, bottom_right.y + rectangle.height)
    top_left = Point(bottom_left.x, + bottom_left.y + rectangle.height)
    corners = [bottom_left, bottom_right, top_left, top_right]
    return corners


def rectangle_in_circle(rectangle, circle):
    corners = calculate_rectangle_corners(rectangle)
    for corner in corners:
        if not point_in_circle(circle, corner):
            return False
    return True


def rect_circle_overlap(rectangle, circle):
    corners = calculate_rectangle_corners(rectangle)
    for corner in corners:
        if point_in_circle(circle, corner):
            return True
    return False


class Point:
    """Represents a point in 2-D space.
        attributes: x, y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point (x = {}, y = {})"\
            .format(self.x, self.y)


class Circle:
    """Represents a circle.
        attributes: center, radius
    """

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circele (center: {} radius = {})"\
            .format(self.center, self.radius)


class Rectangle:
    """Represents a circle.
        attributes: corner (bottom-left), width, height
    """

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle (corner: {} width = {} height = {})"\
            .format(self.corner, self.width, self.height)


if __name__ == '__main__':
    main()
