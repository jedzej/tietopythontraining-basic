class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def object_inspector(obj, attributes):
    dictionary = {}
    for attribute in attributes:
        value = getattr(obj, attribute)
        dictionary[attribute] = value
    return dictionary


def main():
    point = Point(10, 20)
    print(object_inspector(point, ['x', 'y']))


if __name__ == '__main__':
    main()
