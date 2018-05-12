def capitalize(lower_case_word):
    letter = lower_case_word[0]
    return chr(ord(letter) - 32) + lower_case_word[1:]


def main():
    text = input().split(' ')
    result = []
    for word in text:
        result.append(capitalize(word))
    print(result)


if __name__ == "__main__":
    main()
