def object_inspector(objects):
    attr_dict = {}
    for attribute in dir(objects):
        value = getattr(objects, attribute)
        if isinstance(value, (str, int, float)):
            attr_dict[attribute] = value
    return attr_dict


class Person:
    age = 22
    name = "aa"
    salary = 1


person = Person()
person2 = Person()
person2.age = 30
person2.name = "bb"

print(object_inspector(person))
print(object_inspector(person2))
