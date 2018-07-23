class Something:
    pass


class Somebody:
    pass


def check_if_objects_attribute_equal(obj1, obj2, attributes):
    result = {}
    for name in attributes:
        if obj1.__getattribute__(name) == obj2.__getattribute__(name):
            result[name] = True
        else:
            result[name] = False
    return result


st = Something()
st.dot = 1
st.point = 3
st.comma = 5.4
sb = Somebody()
sb.dot = 'cos'
sb.point = 3
sb.comma = 5

print(check_if_objects_attribute_equal(st, sb, ['dot', 'point', 'comma']))
