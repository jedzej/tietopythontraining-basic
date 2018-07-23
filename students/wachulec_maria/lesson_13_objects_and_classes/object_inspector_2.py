class Something:
    pass


def give_attributes_of_object(obj):
    result = {}
    types_list = [str, int, float]
    for name in dir(obj):
        if type(obj.__getattribute__(name)) in types_list:
            result[name] = obj.__getattribute__(name)
    return result


st = Something()
st.dot = 1
st.point = 3
st.comma = 5.4
print(give_attributes_of_object(st))
