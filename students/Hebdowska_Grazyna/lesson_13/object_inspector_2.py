class Car:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age


def create_dictionary(object):
    new_dictionary = object.__dict__
    for i in new_dictionary.keys():
        if isinstance(new_dictionary[i], int):
            print("key=", i, "value=", new_dictionary[i])
        elif isinstance(new_dictionary[i], float):
            print("key=", i, "value=", new_dictionary[i])
        elif isinstance(new_dictionary[i], str):
            print("key=", i, "value=", new_dictionary[i])


def main():
    auto = Car("fiat", "white", 2)
    create_dictionary(auto)


if __name__ == '__main__':
    main()
