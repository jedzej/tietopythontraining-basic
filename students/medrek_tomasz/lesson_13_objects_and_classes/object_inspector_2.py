#!/usr/bin/env python3


from pprint import pprint
from object_inspector_1 import inspect_object_attributes


class Sweet:
    def __init__(self, weight=0, sugar=0.0):
        self.weight = weight
        self.sugar = sugar


class ChocolateBar:
    def __init__(self, sweet=Sweet(0, 0), num_of_bars=0, ingredients=[],
                 flavor="natural", saturated_fat=0.0):
        self.sweet = sweet
        self.num_of_bars = num_of_bars
        self.ingredients = ingredients
        self.flavor = flavor
        self.saturated_fat = saturated_fat


def inspect_specific_object_attributes(obj):
    ret = {}

    for attr in dir(obj):
        value = getattr(obj, attr)
        if isinstance(value, (str, int, float)):
            ret.update({attr: value})

    return ret


def main():
    nussbeisser = ChocolateBar(Sweet(100, 40.5), 6, ["milk", "nuts"], "nutty",
                               15.7)
    pprint(inspect_object_attributes(nussbeisser))
    print("-----------------------------")
    pprint(inspect_specific_object_attributes(nussbeisser))


if __name__ == "__main__":
    main()
