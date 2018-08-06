def object_inspector(obj):
    attr_dict = {}
    attributes = dir(obj)
    for attribute in attributes:
        value = getattr(obj, attribute)
        if isinstance(value, (str, int, float)):
            attr_dict[attribute] = value
    return attr_dict


class Object:
    """This is test class
        attributes: int, float, string
    """

    def __init__(self, i, f, s):
        self.i = i
        self.f = f
        self.s = s

    def __dir__(self):
        return ['i', 'f', 's']


def main():
    test_class = Object(7, 3.14, 'test_string')
    att_dict = object_inspector(test_class)
    print(att_dict)


if __name__ == '__main__':
    main()
