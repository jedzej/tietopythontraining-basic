def swap_two_words(user_word):
    return ' '.join(user_word.split()[::-1])


def main():
    print(swap_two_words(input('Input the words which you wanna swap: ')))


if __name__ == '__main__':
    main()
