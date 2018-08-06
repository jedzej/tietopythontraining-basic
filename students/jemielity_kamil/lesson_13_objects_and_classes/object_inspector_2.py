class Animal:

    def __init__(self, animal_type, legs, age):
        self.animal_type = animal_type
        self.legs = legs
        self.age = age


def dictionary_of_object(obj):
    dictionary = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (str, int, float)):
            dictionary[attr] = value

    return dictionary


def main():

    dog = Animal('dog', 4, 10)
    result = dictionary_of_object(dog)
    print(result)


if __name__ == "__main__":
    main()
