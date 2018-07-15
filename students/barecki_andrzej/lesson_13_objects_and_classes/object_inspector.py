import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s '
                                                '- %(message)s')


class ObjectForInspector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def object_inspector_1(inspected_object, attributes):
    """Create dictionary based on object"""
    dict_from_object = inspected_object.__dict__

    inspected_dict = {}
    for attribute in attributes:
        if attribute in dict_from_object:
            inspected_dict[attribute] = dict_from_object[attribute]

    return inspected_dict


def object_inspector_2(inspected_object):
    """Create dictionary based on object"""
    dict_from_object = inspected_object.__dict__

    inspected_dict = {}
    for key in dict_from_object.keys():
        if isinstance(dict_from_object[key], (int, float, str)):
            inspected_dict[key] = dict_from_object[key]

    return inspected_dict


def main():
    my_object = ObjectForInspector('one', 2, 3.0)
    attributes = ['x', 'y']

    """Object inspector 1"""
    dict_inspector_1 = object_inspector_1(my_object, attributes)

    logging.debug("Dictionary from object_inspector_1:")
    for key in dict_inspector_1.keys():
        logging.debug("key: {0}, value: {1}".format(key,
                                                    dict_inspector_1[key]))

    """Object inspector 2"""
    dict_inspector_2 = object_inspector_2(my_object)

    logging.debug("Dictionary from object_inspector_2:")
    for key in dict_inspector_2.keys():
        logging.debug("key: {0}, value: {1}".format(key,
                                                    dict_inspector_2[key]))


if __name__ == '__main__':
    main()
