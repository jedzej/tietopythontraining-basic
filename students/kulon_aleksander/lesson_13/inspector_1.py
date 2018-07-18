from lesson_13.exercise_1 import Point


def object_inspector(obj, attributes):
    attr_dict = {}
    for attribute in attributes:
        value = getattr(obj, attribute)
        attr_dict[attribute] = value
    return attr_dict


def main():

    point = Point(1, 2)
    attributes = ['x', 'y']
    att_dict = object_inspector(point, attributes)
    print(att_dict)


if __name__ == '__main__':
    main()
