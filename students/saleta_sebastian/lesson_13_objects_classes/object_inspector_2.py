class UserTestObj:

    def __init__(self, a, b, usr_string, usr_list):
        self.a = a
        self.b = b
        self.usr_string = usr_string
        self.usr_list = usr_list

    def __dir__(self):
        return ['a', 'b', 'usr_string', 'usr_list']


def get_attributes(user_object):
    attr_dict = {}
    attributes = dir(user_object)
    for attribute in attributes:
        val = getattr(user_object, attribute)
        if isinstance(val, (str, int, float)):
            attr_dict[attribute] = val
    return attr_dict


def main():
    test_object = UserTestObj(10, 11.243, 'testowy', [1, 2, 3])
    print(get_attributes(test_object))


if __name__ == '__main__':
    main()
