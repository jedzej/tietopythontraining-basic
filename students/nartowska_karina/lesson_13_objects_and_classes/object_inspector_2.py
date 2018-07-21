class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age


def dictionary(obj):
    new_dict = obj.__dict__
    for j in new_dict.keys():
        if isinstance(new_dict[j], str):
            print("key=", j, "value=", new_dict[j])
        elif isinstance(new_dict[j], int):
            print("key=", j, "value=", new_dict[j])
        elif isinstance(new_dict[j], float):
            print("key=", j, "value=", new_dict[j])


def main():
    animal_1 = Animal("shark", "Edward", 5)
    dictionary(animal_1)


if __name__ == '__main__':
    main()
