def distinct_words():
    words = set()
    for _ in range(int(input())):
        words.update(input().split())
    print(len(words))


def main():
    distinct_words()


if __name__ == '__main__':
    main()
