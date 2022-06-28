def comma_code(list_value):
    string = '\''
    for value in list_value:
        if value is not list_value[list_value.__len__() - 1]:
            string += str(value) + ", "
        else:
            string += str(value)
    string += "\'"
    return string


def main():
    numbers = [1, 2, 3, 4, 5]
    spam = ['apples', 'bananas', 'tofu', 'cats']
    words_numbers = [1, 2, 'aum', 7, 'trrr']
    print(comma_code(numbers))
    print(comma_code(spam))
    print(comma_code(words_numbers))


if __name__ == '__main__':
    main()
