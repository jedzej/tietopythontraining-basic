"""
Object inspector 1 - write a function that for a given
object and list of attribute names returns dictionary
with names and values of object's attributes.

Object inspector 2 - write a function that for a given
object returns dictionary with names and values of all
object's attributes that are instances of string,
integer or float.
"""

from exercise_one import Point


class Person:
    def __init__(self, first_name, last_name, age, weight, point):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.point = point

    def __dir__(self):
        return ['first_name', 'last_name', 'age', 'weight', 'point']


def object_inspector_1(obj):
    attributes = dir(obj)
    obj_dict = {}
    for key in attributes:
        obj_dict[key] = getattr(obj, key)
    return obj_dict


def object_inspector_2(obj):
    attributes = dir(obj)
    obj_dict = {}
    for key in attributes:
        if isinstance(getattr(obj, key), (int, float, str)):
            obj_dict[key] = getattr(obj, key)
    return obj_dict


def main():
    person = Person("Adam", "Borowy", 42, 84.34, Point(10, 20))

    """ Test object_inspector_1() function """
    print(object_inspector_1(person))

    """ Test object_inspector_2() function """
    print(object_inspector_2(person))


if __name__ == '__main__':
    main()
