def object_inspector(obj, attributes):
    attr_dict = {}
    for attribute in attributes:
        value = getattr(obj, attribute)
        attr_dict[attribute] = value
    return attr_dict


class Person:
    age = 22
    name = "aa"
    salary = 1


person = Person()
attributes = ['name', 'age']
att_dict = object_inspector(person, attributes)
print(att_dict)
