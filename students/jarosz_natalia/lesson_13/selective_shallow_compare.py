ATTRIBUTES = ['i', 'f', 's']


def compare_attributes(obj1, obj2, attributes):
    for attribute in attributes:
        if getattr(obj1, attribute) != getattr(obj2, attribute):
            return False
    return True


class Object:
    """This is test class
        attributes: int, float, string
    """

    def __init__(self, i, f, s):
        self.i = i
        self.f = f
        self.s = s

    def __str__(self):
        return 'Example: i = {}, f = {}, s = {}'\
            .format(self.i, self.f, self.s)


def main():
    obj1 = Object(1, 2.3, 'test')
    obj2 = Object(5, 6.7, 'test2')
    obj3 = Object(1, 2.3, 'test')

    equal = compare_attributes(obj1, obj2, ATTRIBUTES)
    print('{} is equal {} {}'.format(obj1, obj2, equal))

    equal = compare_attributes(obj1, obj3, ATTRIBUTES)
    print('{} is equal {} {}'.format(obj1, obj3, equal))


if __name__ == '__main__':
    main()
