#!/usr/bin/env python3
"""Inspector 1 exercise"""

from lesson_13_objects.exercise1 import Circle, Point


def obj_insp(obj, obj_attrs):
    """Object inspector"""
    result = {}
    for attr in obj_attrs:
        val = getattr(obj, attr)
        result[attr] = val
    return result


def main():
    """Main function"""
    circle = Circle(Point(50, 50), 75)
    circle_attr = ['c', 'r']
    point_attr = ['x', 'y']
    result = obj_insp(circle, circle_attr)
    print(result)
    result = obj_insp(circle.c, point_attr)
    print(result)


if __name__ == '__main__':
    main()
