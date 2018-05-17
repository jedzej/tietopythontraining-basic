def distinct():
    rows = int(input())
    word = set()

    for i in range(rows):
        text = set(input().split())
        word.update(text)
    return len(word)


def main():
    print(distinct())


if __name__ == '__main__':
    main()
