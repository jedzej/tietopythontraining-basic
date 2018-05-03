#!/usr/bin/env python3


def capitalize(lower_case_word):
    print(lower_case_word[0].upper() + lower_case_word[1:], end=" ")


def main():
    words = input()
    for word in words.split(" "):
        capitalize(word)


if __name__ == "__main__":
    main()
