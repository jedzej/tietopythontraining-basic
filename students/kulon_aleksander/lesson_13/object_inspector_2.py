def object_inspector(obj):
    attr_dict = {}
    attributes = dir(obj)
    for attribute in attributes:
        value = getattr(obj, attribute)
        if isinstance(value, (str, int, float)):
            attr_dict[attribute] = value
    return attr_dict


class Test:
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
    obj = Test(1, 2.3, 'cztery')
    att_dict = object_inspector(obj)
    print(att_dict)


if __name__ == '__main__':
    main()
