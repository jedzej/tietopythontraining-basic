"""
Object inspector 1 - write a function that for
a given object and list of attribute names returns
dictionary with names and values of object's attributes.
"""


class Point:
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


def object_inspector1(instance, keys):
    instance_all = instance.__dict__
    selected_keys = {key:instance_all[key] for key in keys}
    return(selected_keys)


def main():
    ainspector = Point()
    ainspector.g = 7
    ainspector.x = 12
    ainspector.b = [77, 88]
    ainspector.c = 4
    ainspector.y = {'c':77, 'g':88}
    ainspector.s = "sssss"
    ainspector.p = 4.564744
    ainspector.q = 5
    ainspector.m = 4.564744

    a = ['b', 'x', 'y', 'p', 's']
    print(object_inspector1(ainspector, a))


if __name__ == "__main__":
    main()
