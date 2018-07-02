from object_insp import Bunny


def shallow_compare(obj1, obj2, attributes):
    for key in attributes:
        if getattr(obj1, key) != getattr(obj2, key):
            return False
        return True


def main():
    peter = Bunny("Peter", 7, "red")
    fluffy = Bunny("Fluffy", 2.5, "blue")
    fluffy2 = Bunny("Fluffy", 2.5, "blue")

    attributes = ['name', 'age', 'colour']

    print("Are {} and {} equal?".format(peter.name, fluffy.name),
          shallow_compare(peter, fluffy, attributes))
    print("Are {} and {} equal?".format(fluffy2.name, fluffy.name),
          shallow_compare(fluffy2, fluffy, attributes))


if __name__ == '__main__':
    main()
