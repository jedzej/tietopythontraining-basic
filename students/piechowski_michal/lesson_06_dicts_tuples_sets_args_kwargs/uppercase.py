#!/usr/bin/env python3


def capitalize(lower_case_word):
    first_character_ascii_code = ord(lower_case_word[0])
    if first_character_ascii_code >= ord('a') and first_character_ascii_code <= ord('z'):
        print(chr(first_character_ascii_code - 32) + lower_case_word[1:], end=" ")
    else:
        print(lower_case_word, end=" ")


def main():
    words = input()
    for word in words.split(" "):
        capitalize(word)

if __name__ == "__main__":
    main()