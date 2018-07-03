def main():
    example = Example(1, 0.2, 'atrybut', ['elementy', 'listy'])
    att_dict = object_inspector(example)
    print(att_dict)


def object_inspector(example):
    attributes_dict = {}
    attributes = dir(example)
    for attribute in attributes:
        value = getattr(example, attribute)
        if isinstance(value, (str, int, float)):
            attributes_dict[attribute] = value
    return attributes_dict


class Example:
    """This is example class
        attributes: i, f, s, t
    """

    def __init__(self, i, f, s, t):
        self.i = i
        self.f = f
        self.s = s
        self.t = t

    def __dir__(self):
        return ['i', 'f', 's', 't']


if __name__ == '__main__':
    main()
