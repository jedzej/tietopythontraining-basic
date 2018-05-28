def capitalize(lower_case_word):
    line = lower_case_word[0].upper()
    line = line + lower_case_word[1:]
    return line


def main():
    sentence = input().split()
    for word in sentence:
        print(capitalize(word), end=' ')


if __name__ == '__main__':
    main()
