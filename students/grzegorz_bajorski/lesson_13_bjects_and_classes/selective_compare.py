def compare_attributes(obj1, obj2, attributes):
    for attribute in attributes:
        if getattr(obj1, attribute) != getattr(obj2, attribute):
            return False
    return True


class Person:
    age = 22
    name = "aa"
    salary = 1


person = Person()
person2 = Person()
person2.age = 24
person2.name = "bb"
person2.salary = "1"

attributes = ['age', 'name', 'salary']

if compare_attributes(person, person2, attributes):
    print("Compared objects are equal")
else:
    print("Compared objects are not equal")
