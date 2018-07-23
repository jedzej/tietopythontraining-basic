#!/usr/bin/env python3
"""Selective shallow compare exercise"""

from lesson_13_objects.insp_2 import TestObject


def compare(obj1, obj2, attrs):
    """Compare objects"""
    for attr in attrs:
        if getattr(obj1, attr) != getattr(obj2, attr):
            return False
    return True


def main():
    """Main function"""
    obj1 = TestObject(1, 1.1, 'Object')
    obj2 = TestObject(1, 1.1, 'Object')
    obj3 = TestObject(3, 3.1, 'Object3')

    attrs = dir(obj1)

    print('Objects: {}, {} equals: {}'.
          format(obj1, obj2, compare(obj1, obj2, attrs)))
    print('Objects: {}, {} equals: {}'.
          format(obj1, obj3, compare(obj1, obj3, attrs)))
    print('Objects: {}, {} equals: {}'.
          format(obj3, obj2, compare(obj1, obj3, attrs)))


if __name__ == '__main__':
    main()
