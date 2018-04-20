def capitalize(lower_case_word):
    lower_case_word = list(lower_case_word)
    lower_case_word[0] = chr(ord(lower_case_word[0]) - 32)
    return ''.join(lower_case_word)


def main():
    words_list = input().split(' ')
    [print(capitalize(element), end=' ') for element in words_list]


if __name__ == "__main__":
    main()
