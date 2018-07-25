class Something:
    def __init__(self, dot, point, comma):
        self.dot = dot
        self.point = point
        self.comma = comma


def give_attributes_of_object(obj):
    result = {}
    types_list = [str, int, float]
    for name in dir(obj):
        if type(obj.__getattribute__(name)) in types_list:
            result[name] = obj.__getattribute__(name)
    return result


st = Something(1, 3, 5.4)
print(give_attributes_of_object(st))
