def main():
    attributes = ['i', 'f', 's']
    example_one = Example(1, 0.1, 'lama')
    example_two = Example(2, 0.2, 'kaczka')
    example_three = Example(1, 0.1, 'lama')

    equal = compare_objects(example_one, example_two, attributes)
    print('{} is equal {} {}'.format(example_one, example_two, equal))

    equal = compare_objects(example_one, example_three, attributes)
    print('{} is equal {} {}'.format(example_one, example_three, equal))


def compare_objects(e1, e2, attributes):
    for attribute in attributes:
        if getattr(e1, attribute) != getattr(e2, attribute):
            return False
    return True


class Example:
    """This is example class
        attributes: i, f, s
    """

    def __init__(self, i, f, s):
        self.i = i
        self.f = f
        self.s = s

    def __str__(self):
        return 'Example: i = {}, f = {}, s = {}'\
            .format(self.i, self.f, self.s)


if __name__ == '__main__':
    main()
