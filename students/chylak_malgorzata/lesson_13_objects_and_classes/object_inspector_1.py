class Cat:

    def __init__(self, name, color, age, weight):
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight


def dictionary_of_object(obj):
    dictionary = {}

    for attr, value in obj.__dict__.items():
        dictionary[attr] = value

    return dictionary


def main():
    sample = Cat('Meowington', 'ginger', 2, 3.5)
    result = dictionary_of_object(sample)
    print(result)


if __name__ == "__main__":
    main()
