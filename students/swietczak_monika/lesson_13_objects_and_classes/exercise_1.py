class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)


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
    if (point.x - circle.center.x) * (point.x - circle.center.x) + (point.y - circle.center.y) * (
            point.y - circle.center.y) <= circle.radius * circle.radius:
        return True
    else:
        return False


def rectangle_points(rect):
    left_down = rect.corner
    left_up = Point(left_down.x, left_down.y + rect.height)
    right_down = Point(left_down.x + rect.width, left_down.y)
    right_up = Point(left_down.x + rect.width, left_down.y + rect.height)
    result = [left_down, left_up, right_up, right_down]
    return result


def rect_in_circle(rectangle, circle):
    points = rectangle_points(rectangle)
    for point in points:
        if not point_in_circle(point, circle):
            return False
        else:
            return True


def rect_circle_overlap(rectangle, circle):
    points = rectangle_points(rectangle)
    for point in points:
        if point_in_circle(point, circle):
            return True
        else:
            return False


def main():
    circle = Circle(Point(150, 100), 75)
    point = Point(50, 100)
    rectangle = Rectangle(20, 10, Point(120, 100))
    print("Point:" + str(point))
    print("Is point inside the circle? " + str(point_in_circle(point, circle)))
    print("Is rectangle inside the circle? " + str(rect_in_circle(rectangle, circle)))
    print("Is rectangle overlapping the circle? " + str(rect_circle_overlap(rectangle, circle)))


if __name__ == '__main__':
    main()
