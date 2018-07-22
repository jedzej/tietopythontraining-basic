#!/usr/bin/env python3

"""
object_inspectors.py: a practice projects "Object inspector 1" and  "Object
inspector 2" from:
Lesson 13 - Objects and classes

"""

__author__ = "Daniel Urtnowski"
__version__ = "0.1"


import geometric_figures


def object_inspector_1(obj, attributes, stringify_values=False):
    """
    This function for a given object and list of attribute names returns
    dictionary with names and values of object's attributes
    :param obj: object of any class
    :param list attributes: list of the attributes of the object
    :param bool stringify_values: if set to True, the values in the returned
    dictionary are converted to strings
    :return: a dictionary
    """
    ret = {}

    if stringify_values:
        def modify(x):
            return str(x)
    else:
        def modify(x):
            return x

    for attr in attributes:
        ret[attr] = modify(getattr(obj, attr))

    return ret


def object_inspector_2(obj, exclude_builtin=False):
    """
    This function for a given object returns dictionary with names and values
    of all object's attributes that are instances of string, integer or float
    :param obj: object of any class
    :param bool exclude_builtin: if set to True, the built-in attributes are
    omitted
    :return: a dictionary
    """
    ret = {}

    if exclude_builtin:
        attributes = [attr for attr in dir(obj) if not attr.startswith('__')]
    else:
        attributes = dir(obj)

    for attr in attributes:
        val = getattr(obj, attr)
        if isinstance(val, (str, int, float)):
            ret[attr] = val

    return ret


def main():

    point = geometric_figures.Point(100, 200)
    circle = geometric_figures.Circle(point, 50)
    rect = geometric_figures.Rectangle(point, geometric_figures.Point(150,
                                                                      300))
    print('INSPECTOR 1:')
    for name, obj, attr in [('point', point, ['x', 'y']),
                            ('circle', circle, ['center', 'radius']),
                            ('rect', rect, ['left_down', 'top_right'])]:
        print('{}: {}'.format(name, object_inspector_1(obj, attr, True)))

    print('\nINSPECTOR 2:')
    for name, obj in [('point', point), ('circle', circle), ('rect', rect)]:
        print('{}: {}'.format(name, object_inspector_2(obj, True)))


if __name__ == '__main__':
    main()
