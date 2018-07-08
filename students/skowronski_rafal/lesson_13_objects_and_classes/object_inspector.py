import circles
import re


class TypeMatcher:
    def __init__(self, *types):
        self.types = types

    def match(self, obj):
        for t in self.types:
            if isinstance(obj, t):
                return True
        return False


def inspect_attributes(obj, type_match=lambda obj: True):
    regex = re.compile(r'^(?!__).*$(?!__)')  # get rid of private stuff
    attributes = \
        [(x, getattr(obj, x)) for x in dir(obj) if regex.match(x)]
    return dict([x for x in attributes if type_match(x[1])])


if __name__ == '__main__':
    circle = circles.Circle(circles.Point(0, 1), 15)

    print(inspect_attributes(circle))

    point_matcher = TypeMatcher(circles.Point)
    print(inspect_attributes(circle, point_matcher.match))

    int_matcher = TypeMatcher(int)
    print(inspect_attributes(circle, int_matcher.match))

    t_class = type('TestType', (), {})
    t = t_class()
    t.att1 = 'Foo'
    t.att2 = circles.Point(0, 1)
    t.att3 = 12
    t.att4 = 12.3
    t.att5 = circles.Circle(circles.Point(0, 1), 15)

    ex_matcher = TypeMatcher(int, float, str)
    print(inspect_attributes(t, ex_matcher.match))
