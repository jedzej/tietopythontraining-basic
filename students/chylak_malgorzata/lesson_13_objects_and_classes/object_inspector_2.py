class Dog:

    def __init__(self, breed, legs, age):
        self.breed = breed
        self.legs = legs
        self.age = age


def dictionary_of_object(obj):
    dictionary = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (str, int, float)):
            dictionary[attr] = value

    return dictionary


def main():

    doggo = Dog('Corgi', 4, 2)
    result = dictionary_of_object(doggo)
    print(result)


if __name__ == "__main__":
    main()
