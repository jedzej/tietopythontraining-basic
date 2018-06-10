def get_number_of_words(user_word):
    return user_word.count(' ') + 1


def main():
    print(get_number_of_words(input()))


if __name__ == '__main__':
    main()
