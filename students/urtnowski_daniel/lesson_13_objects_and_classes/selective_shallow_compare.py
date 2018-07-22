#!/usr/bin/env python3

"""
selective_shallow_compare.py: a practice projects "Selective shallow compare"
from:
Lesson 13 - Objects and classes
"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import geometric_figures


def compare(first, second, attributes):
    """
    This function for given 2 objects and list of attribute names checks if
    objects' attributes are equal
    :param first: first object to be compared
    :param second: second object to be compared
    :param list attributes: list of strings
    :return bool: True if all the attributes are equal in the both objects
    """
    for attr in attributes:

        first_has_attr = hasattr(first, attr)
        second_has_attr = hasattr(second, attr)

        if first_has_attr and second_has_attr:
            if getattr(first, attr) is not getattr(second, attr):
                return False
        elif first_has_attr or second_has_attr:
            # only one of the objects has the attribute
            return False
        else:
            # none of the objects has the attribute, so there is equality here
            continue

    return True


def main():

    point = geometric_figures.Point(100, 200)
    circle = geometric_figures.Circle(point, 50)
    point_copy = point.copy()
    circle2 = geometric_figures.Circle(point_copy, 50)

    for name1, name2, ob1, ob2, attr in [
        ('point', 'point_copy', point, point_copy, ['x', 'y']),
        ('circle', 'circle', circle, circle, ['center', 'radius']),
        ('circle', 'circle2', circle, circle2, ['center', 'radius']),
        ('circle', 'circle2', circle, circle2, ['radius'])
    ]:
        print('{} is equal to {} (comparing attributes: {}): {}'
              .format(name1, name2, attr, compare(ob1, ob2, attr)))


if __name__ == '__main__':
    main()
