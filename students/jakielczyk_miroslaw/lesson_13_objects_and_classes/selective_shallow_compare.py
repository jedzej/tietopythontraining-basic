class Person:

    def __init__(self, name, surname, age, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight


def compare_objects(object1, object2, attributes):
    for attribute in attributes:
        if getattr(object1, attribute) == getattr(object2, attribute):
            print('Attribute', attribute, 'are equal')
        else:
            print('Attribute', attribute, 'are not equal')


def main():
    person1 = Person('Marek', 'Nowak', 45, 72.3)
    person2 = Person('Marek', 'Kowalski', 45, 90.5)
    compare_objects(person1, person2, ['name', 'surname', 'age', 'weight'])


if __name__ == "__main__":
    main()
