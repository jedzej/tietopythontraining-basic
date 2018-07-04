#!/usr/bin/env python3


def swap_words(message):
    space_pos = message.find(' ')
    return "{} {}".format(message[space_pos + 1:], message[:space_pos])


def main():
    input_message = input("Please write 2 words separated with space\n")
    print(swap_words(input_message))


if __name__ == "__main__":
    main()
