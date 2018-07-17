#!/usr/bin/env python3


class Cat:
    name = "Miauk"
    age = 7
    favourite_food = ["fish", "ham", "chicken"]


def shallow_compare(some_object, other_object, attributes):
    for attribute in attributes:
        some_value = getattr(some_object, attribute)
        other_value = getattr(other_object, attribute)
        if some_value != other_value:
            print("Values of given objects are not the same")
            return

    print("Values of given objects are the same")


def main():
    cat_miauk = Cat()

    cat_tom = Cat()
    cat_tom.name = "Tom"
    cat_tom.age = 12
    cat_tom.favourite_food = ["mice", "cheese"]

    cat_catsper = Cat()
    cat_catsper.name = "Catsper"
    cat_catsper.age = 12
    cat_catsper.favourite_food = ["mice", "cheese"]

    print("Comparing Miauk and Tom:")
    shallow_compare(cat_miauk, cat_tom, ["name", "age"])
    print("Comparing Tom and Catsper:")
    shallow_compare(cat_tom, cat_catsper, ["favourite_food", "age"])


if __name__ == "__main__":
    main()
