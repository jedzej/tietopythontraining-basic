"""
Selective shallow compare - write a function that
for given 2 objects and list of attribute names checks
if objects' attributes are equal.
"""

from exercise_one import Point
from object_inspectors import Person


class Alien:
    def __init__(self, last_name, age, weight, point, power_level):
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.point = point
        self.power_level = power_level

    def __dir__(self):
        return ['last_name', 'age', 'weight', 'point', 'power_level']


def compare_objects(object_1, object_2, attributes):
    for key in attributes:
        if getattr(object_1, key) != getattr(object_2, key):
            return False
    return True


def main():
    janusz = Person("Janusz", "Polak", 41, 105.5, Point(10, 20))
    wladek = Person("Wladek", "Polak", 41, 105.5, Point(30, 40))
    ufok = Alien("Qctrl", 1201, 22, Point(77, 99), 9000)

    attributes = ['last_name', 'age', 'weight']
    print(compare_objects(janusz, ufok, attributes))
    print(compare_objects(janusz, wladek, attributes))


if __name__ == '__main__':
    main()
