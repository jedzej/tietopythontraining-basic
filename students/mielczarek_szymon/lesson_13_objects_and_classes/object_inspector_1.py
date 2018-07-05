#! python3
import pprint

"""
Task:
Write a function that for a given object and list of attribute names returns
dictionary with names and values of object's attributes.
"""


def dump_object_attributes(obj):
    return dict((i, getattr(obj, i)) for i in dir(obj))


def main():
    x = 1
    attr_dump = dump_object_attributes(x)
    print("Number of attributes: {}".format(len(attr_dump)))
    pprint.pprint(attr_dump)


if __name__ == '__main__':
    main()
