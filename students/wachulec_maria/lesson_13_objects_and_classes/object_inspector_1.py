class Something:
    pass


def give_names_and_values_of_object(obj, attributes):
    result = {}
    for name in attributes:
        result[name] = obj.__getattribute__(name)
    return result


st = Something()
st.dot = 1
st.point = 3
st.comma = 5
print(give_names_and_values_of_object(st, ['dot', 'comma']))
