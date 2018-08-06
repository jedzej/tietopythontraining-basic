class Something:
    def __init__(self, dot, point, comma):
        self.dot = dot
        self.point = point
        self.comma = comma


class Somebody:
    def __init__(self, dot, point, comma):
        self.dot = dot
        self.point = point
        self.comma = comma


def check_if_objects_attribute_equal(obj1, obj2, attributes):
    result = {}
    for name in attributes:
        if obj1.__getattribute__(name) == obj2.__getattribute__(name):
            result[name] = True
        else:
            result[name] = False
    return result


st = Something(1, 3, 5.4)
sb = Somebody('cos', 3, 5)

print(check_if_objects_attribute_equal(st, sb, ['dot', 'point', 'comma']))
