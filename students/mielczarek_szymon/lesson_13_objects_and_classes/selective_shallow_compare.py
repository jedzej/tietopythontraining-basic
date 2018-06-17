#! python3
import logging
import copy
"""
Task:
Write a function that for given 2 objects and list of attribute names checks
if objects' attributes are equal.
"""
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class Point:
    """Represents a point in 2-D space."""


def are_equal_shallow(obj1, obj2, attributes):
    """Shallow compare given attributes of two objects.

    :param obj1: First object
    :type obj1: object
    :param obj2: Second object
    :type obj2: object
    :param attributes: Names of attributes
    :type attributes: list
    :return: Whether all compared attributes of two given objects are equal
    :rtype: bool
    """
    for attr in attributes:
        if not hasattr(obj1, attr) or not hasattr(obj2, attr):
            logging.debug("One of the objects does not have attribute with name: {}."
                          .format(attr))
            return False
        if getattr(obj1, attr) is not getattr(obj2, attr):
            logging.debug("Attribute {} is not equal for compared objects."
                          .format(attr))
            return False
    return True


def main():
    p1 = Point()
    p1.x = 5.0
    p1.y = 4.0
    p2 = copy.copy(p1)

    if are_equal_shallow(p1, p2, ['x', 'y']):
        logging.info("Compared objects are equal.")
    else:
        logging.info("Compared objects are not equal!")


if __name__ == '__main__':
    main()
