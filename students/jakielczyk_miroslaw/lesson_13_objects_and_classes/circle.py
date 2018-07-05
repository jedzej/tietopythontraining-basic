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

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height


def distance_between_points(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return dist


def point_in_circle(circle, point):
    if distance_between_points(point.x, point.y, circle.center.x, circle.center.y) <= circle.radius:
        return True
    else:
        return False


def rect_in_circle(circle, rectangle):
    rectangle_inside_circle = True
    rectangle_corners = [[rectangle.corner.x, rectangle.corner.y],
                         [rectangle.corner.x + rectangle.width, rectangle.corner.y],
                         [rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height],
                         [rectangle.corner.x, rectangle.corner.y + rectangle.height]]

    for rect_corner in rectangle_corners:
        if distance_between_points(rect_corner[0], rect_corner[1], circle.center.x, circle.center.y) > circle.radius:
            rectangle_inside_circle = False
            break

    if rectangle_inside_circle:
        return True
    else:
        return False


def rect_circle_overlap(circle, rectangle):
    corner_inside_circle = False
    rectangle_corners = [[rectangle.corner.x, rectangle.corner.y],
                         [rectangle.corner.x + rectangle.width, rectangle.corner.y],
                         [rectangle.corner.x + rectangle.width, rectangle.corner.y + rectangle.height],
                         [rectangle.corner.x, rectangle.corner.y + rectangle.height]]

    for rect_corner in rectangle_corners:
        if distance_between_points(rect_corner[0], rect_corner[1],
                                   circle.center.x, circle.center.y) <= circle.radius:
            corner_inside_circle = True
            break

    if corner_inside_circle:
        return True
    else:
        return False


def main():
    circle_center = Point(150, 100)
    circle = Circle(circle_center, 75)
    point = Point(225, 100)
    if point_in_circle(circle, point):
        print('Point is in a circle')
    else:
        print('Point is not in a circle')

    box_corner = Point(100, 50)
    rectangle = Rectangle(box_corner, 100, 100)
    if rect_in_circle(circle, rectangle):
        print('Rectangle is inside a circle')
    else:
        print('Rectangle is not inside a circle')

    box_2_corner = Point(10, 10)
    rectangle_2 = Rectangle(box_2_corner, 87, 37)
    if rect_circle_overlap(circle, rectangle_2):
        print('At least one corner is inside a circle')
    else:
        print('None of the corners is inside a circle')


if __name__ == '__main__':
    main()
