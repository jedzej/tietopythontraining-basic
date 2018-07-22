class Point:
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


def object_inspector2(instance, keys):
    instance_all = instance.__dict__
    selected_keys = {key: instance_all[key] for key in keys
                     if (isinstance(instance_all[key], int) or
                     isinstance(instance_all[key], str) or
                     isinstance(instance_all[key], float))}
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
    print(object_inspector2(ainspector, a))

if __name__ == "__main__":
    main()