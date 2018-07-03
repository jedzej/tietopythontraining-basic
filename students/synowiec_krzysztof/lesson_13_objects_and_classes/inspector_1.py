def main():
    example = Example(1, 2, 3)
    attributes = ['x', 'y', 'z']
    att_dict = object_inspector(example, attributes)
    print(att_dict)


def object_inspector(example, attributes):
    attributes_dict = {}
    for attribute in attributes:
        value = getattr(example, attribute)
        attributes_dict[attribute] = value
    return attributes_dict


class Example:
    """This is example class
        attributes: x, y, z
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    main()
