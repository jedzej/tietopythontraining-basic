#!/usr/bin/env python3


def capitalize(lower_case_word):
    first_letter_no = ord(lower_case_word[0:1])
    if first_letter_no in range(ord('a'), ord('z') + 1):
        return chr(first_letter_no - 32) + lower_case_word[1:]
    else:
        return lower_case_word


def capitalize_message(message):
    output = ' '
    words_list = []
    for word in message.split():
        words_list += [capitalize(word)]
    return output.join(words_list)


def main():
    input_message = input("Please enter your message\n")
    print(capitalize_message(input_message))


if __name__ == "__main__":
    main()
