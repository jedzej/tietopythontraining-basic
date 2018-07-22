def compare_attributes(obj1, obj2, attributes):
    for attribute in attributes:
        if getattr(obj1, attribute) != getattr(obj2, attribute):
            return False
    return True


class Test:
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
    attributes = ['i', 'f', 's']
    obj1 = Test(1, 2.3, 'cztery')
    obj2 = Test(5, 6.7, 'osiem')
    obj3 = Test(1, 2.3, 'cztery')

    equal = compare_attributes(obj1, obj2, attributes)
    print('{} is equal {} {}'.format(obj1, obj2, equal))

    equal = compare_attributes(obj1, obj3, attributes)
    print('{} is equal {} {}'.format(obj1, obj3, equal))


if __name__ == '__main__':
    main()
