#!/usr/bin/env python3


class Cat:
    name = "Miauk"
    age = 7
    favourite_food = ["fish", "ham", "chicken"]


def object_inspector(some_object):
    dictionary = {}

    for attribute in dir(some_object):
        value = getattr(some_object, attribute)
        if isinstance(value, (int, float, str)):
            dictionary[attribute] = value

    return dictionary


def main():
    cat_miauk = Cat()

    cat_tom = Cat()
    cat_tom.name = "Tom"
    cat_tom.age = 12
    cat_tom.favourite_food = ["mice", "cheese"]

    print(object_inspector(cat_miauk))
    print(object_inspector(cat_tom))


if __name__ == "__main__":
    main()
