def main():
    word_list = [x for x in input().split()]
    for word in word_list:
        print(capitalize(word), end=" ")


def capitalize(word):
    letters = [x for x in word]
    letters[0] = letters[0].upper()
    return ''.join(letters)


if __name__ == '__main__':
    main()
