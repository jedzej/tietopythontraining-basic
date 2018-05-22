def swap_two_words(user_word):
    return ' '.join(user_word.split()[::-1])


def main():
    print(swap_two_words(input()))


if __name__ == '__main__':
    main()
