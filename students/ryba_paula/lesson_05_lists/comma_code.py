def comma_code(value):
    if len(value) > 0:
        return ", ".join(str(i) for i in value[:-1]) + " and " + str(value[-1])
    else:
        print("empty list")


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    numbers = [1, 2, 3, 19918, 91]
    mixed = ['some', 'text', 1, 'number', 334, 0, None]
    nothing = []
    print(comma_code(spam))
    print(comma_code(numbers))
    print(comma_code(mixed))
    print(comma_code(nothing))


if __name__ == '__main__':
    main()
