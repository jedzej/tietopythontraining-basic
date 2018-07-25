class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius, x, y):
        self.center = Point(x, y)
        self.radius = radius


class Rectangle:
    def __init__(self, x, y, width, height):
        self.bottom_left = Point(x, y)
        self.bottom_right = Point(x + width, y)
        self.top_right = Point(x + width, y + height)
        self.top_left = Point(x, y + height)

    def __dir__(self):
        return self.__dict__.items()


def point_in_circle(circle, point):
    if (point.x - circle.center.x) + (point.y - circle.center.y)\
            <= circle.radius ** 2:
        return True
    else:
        return False


def rect_in_circle(circle, rectangle):
    for i in dir(rectangle):
        if not point_in_circle(circle, i[1]):
            return False
    return True


def rect_circle_overlap(circle, rectangle):
    for i in dir(rectangle):
        if point_in_circle(circle, i[1]):
            return True
    return False


c = Circle(75, 150, 100)
p = Point(160, 100)
r = Rectangle(100, 50, 500, 5)
print(point_in_circle(c, p))
print(rect_in_circle(c, r))
print(rect_circle_overlap(c, r))
