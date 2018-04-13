#!/usr/bin/env python3


def capitalize(lower_case_word):
    first_char_ascii = ord(lower_case_word[0])
    if first_char_ascii >= ord('a') and first_char_ascii <= ord('z'):
        print(chr(first_char_ascii - 32) + lower_case_word[1:], end=" ")
    else:
        print(lower_case_word, end=" ")


def main():
    words = input()
    for word in words.split(" "):
        capitalize(word)


if __name__ == "__main__":
    main()
