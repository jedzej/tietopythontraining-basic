#!/usr/bin/env python3


def number_of_distinct_words(message):
    words_set = set(message.split())
    return len(words_set)


def main():
    try:
        number_of_lines = int(input("Please enter integer number of lines\n"))
    except ValueError:
        print("It was wrong number, try again\n")
        exit

    input_text = ''
    for line in range(number_of_lines):
        input_text += input("Please enter line of message\n") + '\n'

    print(number_of_distinct_words(input_text))


if __name__ == "__main__":
    main()
