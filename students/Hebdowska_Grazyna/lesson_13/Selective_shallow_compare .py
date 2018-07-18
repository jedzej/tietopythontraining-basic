class Car:

    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age


def compare(object1, object2, atribute_names):
    object1_atr = []
    object2_atr = []
    for i in atribute_names:
        object1_atr.append(getattr(object1, i))
        object2_atr.append(getattr(object2, i))
    if object1_atr == object2_atr:
        print("Atributes are equal")
    else:
        print("Atributes are not equal")


def main():
    auto1 = Car("fiat", "white", 2)
    auto2 = Car("fiat", "red", 2)
    compare(auto1, auto2, ["age", "colour"])


if __name__ == '__main__':
    main()
