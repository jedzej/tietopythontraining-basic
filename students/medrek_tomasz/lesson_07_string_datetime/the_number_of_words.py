#!/usr/bin/env python3


def number_of_words(message):
    return message.count(' ') + 1


def main():
    input_message = input("Please write a message separated with spaces\n")
    print(number_of_words(input_message))


if __name__ == "__main__":
    main()
