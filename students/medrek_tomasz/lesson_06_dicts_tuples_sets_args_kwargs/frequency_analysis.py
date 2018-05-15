#!/usr/bin/env python3


def main():
    words_database = {}

    try:
        number_of_lines = int(input("Please enter integer number\n"))
    except ValueError:
        print("It was not an integer number, try again\n")
        exit

    for line in range(number_of_lines):
        words_from_input_message = input("Please enter a message\n").split()
        for word in words_from_input_message:
            words_database.setdefault(word, 0)
            words_database[word] += 1

    for word, value in sorted(words_database.items(),
                              key=lambda x: (-x[1], x[0])):
        print(word)


if __name__ == "__main__":
    main()
