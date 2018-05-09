def capitalize(lower_case_word):
    return lower_case_word[0].upper() + lower_case_word[1:]


def main():
    text = input("Input text: ").split()
    for word in text:
        print(capitalize(word), end=" ")


if __name__ == '__main__':
    main()
