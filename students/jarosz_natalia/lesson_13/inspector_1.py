from lesson_13.exercise_1 import Rectangle


def object_inspector(obj, attributes):
    attr_dict = {}
    for attribute in attributes:
        value = getattr(obj, attribute)
        attr_dict[attribute] = value
    return attr_dict


def main():
    rectangle = Rectangle(1, 2, 3)
    attributes = ['width', 'height', 'corner']
    att_dict = object_inspector(rectangle, attributes)
    print(att_dict)


if __name__ == '__main__':
    main()
