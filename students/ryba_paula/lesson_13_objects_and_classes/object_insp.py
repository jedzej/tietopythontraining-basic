class Bunny:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def __dir__(self):
        return ['name', 'age', 'colour']


def object_inspector1(obj):
    attributes = dir(obj)
    return dict((key, getattr(obj, key)) for key in attributes)


def object_inspector2(obj):
    attributes = dir(obj)
    return dict((key, getattr(obj, key)) for key in attributes
                if isinstance(getattr(obj, key), (int, float, str)))


def main():
    bunny = Bunny("Peter", 3, "black")
    print(object_inspector1(bunny))

    bunny2 = Bunny("Tuptus", 8.5, [1,2])
    print(object_inspector2(bunny2))


if __name__ == '__main__':
    main()
