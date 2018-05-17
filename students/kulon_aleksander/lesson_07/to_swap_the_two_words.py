def swap_words():
    text = str(input())
    text = text.split()
    text = text[1] + ' ' + text[0]
    print(text)


def main():
    swap_words()


if __name__ == '__main__':
    main()
