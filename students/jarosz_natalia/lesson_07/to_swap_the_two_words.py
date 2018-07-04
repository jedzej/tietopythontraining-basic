def swap_the_two_words():
    s = input()
    first_word = s[:s.find(' ')]
    second_word = s[s.find(' ') + 1:]
    print(second_word + ' ' + first_word)


def main():
    swap_the_two_words()


if __name__ == '__main__':
    main()
