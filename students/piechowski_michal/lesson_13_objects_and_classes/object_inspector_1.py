#!/usr/bin/env python3


class Cat:
    name = "Miauk"
    age = 7
    favourite_food = ["fish", "ham", "chicken"]


def object_inspector(some_object, attributes):
    dictionary = {}

    for attribute in attributes:
        value = getattr(some_object, attribute)
        dictionary[attribute] = value

    return dictionary


def main():
    cat_miauk = Cat()

    cat_tom = Cat()
    cat_tom.name = "Tom"
    cat_tom.age = 12
    cat_tom.favourite_food = ["mice", "cheese"]

    print(object_inspector(cat_miauk, ["name", "age"]))
    print(object_inspector(cat_tom, ["name", "favourite_food"]))


if __name__ == "__main__":
    main()
