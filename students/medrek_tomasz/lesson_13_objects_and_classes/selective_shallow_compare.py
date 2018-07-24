#!/usr/bin/env python3


import logging
from object_inspector_2 import ChocolateBar, Sweet


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def selective_shallow_compare(obj1, obj2, attribute_names):
    for attribute in attribute_names:
        logger.debug("{} ?= {}".format(getattr(obj1, attribute),
                                       getattr(obj2, attribute)))
        if getattr(obj1, attribute) != getattr(obj2, attribute):
            print("Attribute values of given objects are not the same")
            return False

    print("Attribute values {} of given objects are equal"
          .format(attribute_names))
    return True


def main():
    original_nussbeisser = ChocolateBar(Sweet(100, 40.5), 6, ["milk", "nuts"],
                                        "nutty", 15.7)
    alpengold_nussbeisser = ChocolateBar(Sweet(100, 46.5), 6, ["milk", "nuts"],
                                         "nutty", 14.5)

    selective_shallow_compare(original_nussbeisser, alpengold_nussbeisser,
                              ["flavor", "ingredients", "num_of_bars"])
    selective_shallow_compare(original_nussbeisser, alpengold_nussbeisser,
                              ["flavor", "ingredients", "saturated_fat"])


if __name__ == "__main__":
    main()
