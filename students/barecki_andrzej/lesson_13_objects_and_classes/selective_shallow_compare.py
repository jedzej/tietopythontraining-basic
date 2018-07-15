class TestObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def selective_object_compare(obj_1, obj_2, attributes):
    """Create dictionary based on objects"""
    dict_from_obj_1 = obj_1.__dict__
    dict_from_obj_2 = obj_2.__dict__

    for attribute in attributes:
        if attribute in dict_from_obj_1 and attribute in dict_from_obj_2:
            if dict_from_obj_1[attribute] != dict_from_obj_2[attribute]:
                return False
    return True


def main():
    obj_1 = TestObject('one', 2, 3.0)
    obj_2 = TestObject('one', 2, 3.0)
    obj_3 = TestObject('two', 2, 4.0)
    attributes = ['x', 'y', 'z']

    """Test 1: obj_1 vs obj_2 """
    res = selective_object_compare(obj_1, obj_2, attributes)
    if res:
        print("Objects abj_1 and obj_2 are equal")
    else:
        print("Objects abj_1 and obj_2 are different")

    """Test 2: obj_2 vs obj_3 """
    res = selective_object_compare(obj_2, obj_3, attributes)
    if res:
        print("Objects abj_2 and obj_3 are equal")
    else:
        print("Objects abj_2 and obj_3 are different")


if __name__ == '__main__':
    main()
