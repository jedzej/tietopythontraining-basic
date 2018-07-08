"""
Selective shallow compare - write a function that for given 2 objects
and list of attribute names checks if objects' attributes are equal.
"""


class Point:
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


def compere_objects(instance1, instance2, keys):
    instance1_all = instance1.__dict__
    instance2_all = instance2.__dict__
    compare_result = {key: (instance1_all[key] == instance2_all[key])
                      for key in keys}
    return(compare_result)


def main():
    ainspector = Point()
    ainspector.g = 7
    ainspector.x = 12
    ainspector.b = [77, 88]
    ainspector.c = 4
    ainspector.y = {'c': 77, 'g': 88}
    ainspector.s = 'sssss'
    ainspector.p = 4.564744
    ainspector.q = 5
    ainspector.m = 4.564744

    binspector = Point()
    binspector.g = 7
    binspector.x = 5
    binspector.b = [22, 88]
    binspector.c = 4
    binspector.y = {'c': 77, 'g': 88}
    binspector.s = 'ssassss'
    binspector.p = 4.564744
    binspector.q = 5
    ainspector.m = 4.564744

    attributes = ['b', 'x', 'y', 'p', 's']
    print(compere_objects(ainspector, binspector, attributes))


if __name__ == "__main__":
    main()
