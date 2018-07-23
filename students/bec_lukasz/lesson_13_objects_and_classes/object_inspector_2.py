class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Sth:
    def __init__(self, v, x, y, z):
        self.v = v
        self.x = x
        self.y = y
        self.z = z


def object_inspector2(obj):
    attributes = dir(obj)
    dictionary = {}
    for i in attributes:
        if isinstance(getattr(obj, i), (int, float, str)):
            value = getattr(obj, i)
            dictionary[i] = value
    return dictionary


def main():
    point = Point(10, 20)
    sth = Sth(point, 10, 20.0, 'trzydziesci')
    print(object_inspector2(sth))


if __name__ == '__main__':
    main()
