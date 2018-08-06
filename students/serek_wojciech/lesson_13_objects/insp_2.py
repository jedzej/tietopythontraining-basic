#!/usr/bin/env python3
"""Inspector 2 exercise"""


def obj_insp_2(obj):
    """Object inspector"""
    result = {}
    obj_attr = dir(obj)
    for attr in obj_attr:
        val = getattr(obj, attr)
        if isinstance(val, (str, int, float)):
            result[attr] = val
    return result


class TestObject:
    """Test class"""
    def __init__(self, i, f, s):
        self.i = i
        self.f = f
        self.s = s

    def __dir__(self):
        return ['i', 'f', 's']

    def __str__(self):
        return '(i: {}, f: {}, s: {})'.format(self.i, self.f, self.s)


def main():
    """Main function"""
    print(obj_insp_2(TestObject(5, 10.5, 'Test')))


if __name__ == '__main__':
    main()
