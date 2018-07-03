class Person:

    def __init__(self, name, surname, age, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight


def inspect_object(checked_object):
    obj_dictionary = checked_object.__dict__
    for key in obj_dictionary.keys():
        if isinstance(obj_dictionary[key], (int, float, str)):
            print('key=', key, ' value=', obj_dictionary[key])


def main():
    person1 = Person('Marek', 'Nowak', 45, 72.3)
    inspect_object(person1)


if __name__ == "__main__":
    main()
