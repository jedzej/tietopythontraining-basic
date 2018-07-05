#! python3
import pprint
"""
Task:
Write a function that for a given object returns dictionary with names and
values of all object's attributes that are instances of string, integer or
float.
"""


class TestObject:
    def __init__(self, x, y, text, somelist):
        self.integer = x
        self.float = y
        self.string = text
        self.mylist = somelist


def dump_object_selected_attributes(obj):
    """Return object's attributes that are instances of string, integer or
    float."""

    return dict((i, getattr(obj, i)) for i in dir(obj) if isinstance(getattr(
        obj, i), (str, int, float)))


def main():
    p = TestObject(23, 66.543, "test", [1, 2, 3])
    # The last, list attribute, should not be returned and printed out.
    attr_dump = dump_object_selected_attributes(p)
    print("Number of matching attributes: {}".format(len(attr_dump)))
    pprint.pprint(attr_dump)


if __name__ == '__main__':
    main()
