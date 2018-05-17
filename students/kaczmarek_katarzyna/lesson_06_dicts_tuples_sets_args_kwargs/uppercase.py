def capitalize(lower_case_word):
    ascii_code = ord(lower_case_word[0])
    if 97 <= ascii_code <= 122:
        first_letter_big = chr(ascii_code - ord('a') + ord('A'))
    else:
        first_letter_big = lower_case_word[0]

    return first_letter_big + lower_case_word[1:]


def main():
    words = [word for word
             in input("Type lowercase words (space separated): ").split()]
    for word in words:
        print(capitalize(word), end=" ")


if __name__ == '__main__':
    main()
