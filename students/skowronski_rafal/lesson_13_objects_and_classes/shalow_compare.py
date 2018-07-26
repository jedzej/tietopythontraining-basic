def compare(obj1, obj2, attribute_names):
    for attribute_name in attribute_names:
        if not getattr(obj1, attribute_name) == getattr(obj2, attribute_name):
            return False

    return True


if __name__ == '__main__':
    type1 = type('Type1', (), {})
    obj11 = type1()
    obj11.att1 = 'Foo'
    obj11.att2 = 11

    obj12 = type1()
    obj12.att1 = 'Foo'
    obj12.att2 = 11

    obj13 = type1()
    obj13.att1 = 'Foo'
    obj13.att2 = 12

    type2 = type('Type2', (), {})
    obj21 = type2()
    obj21.att1 = 'Foo'
    obj21.att2 = 11

    print(compare(obj11, obj12, ['att1', 'att2']))
    print(compare(obj11, obj13, ['att1', 'att2']))
    print(compare(obj11, obj21, ['att1', 'att2']))
