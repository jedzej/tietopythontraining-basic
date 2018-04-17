def capitalize(lower_case_word):
    table_with_letters = [i for i in lower_case_word]
    first_letter_ascii = ord(table_with_letters[0]) - 32
    table_with_letters[0] = chr(first_letter_ascii)
    print(''.join(table_with_letters), end=" ")


def main():
    print("Result:")
    text = [i for i in input().split()]
    for lower_case_word in text:
        capitalize(lower_case_word)


if __name__ == '__main__':
    main()
