class Something:
    def __init__(self, dot, point, comma):
        self.dot = dot
        self.point = point
        self.comma = comma


def give_names_and_values_of_object(obj, attributes):
    result = {}
    for name in attributes:
        result[name] = obj.__getattribute__(name)
    return result


st = Something(1, 3, 5)
print(give_names_and_values_of_object(st, ['dot', 'comma']))
