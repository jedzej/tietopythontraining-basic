def main():
    counter = {}
    for i in range(int(input())):
        for word in input().split():
            counter[word] = counter.get(word, 0) + 1

    frequency = sorted([(-i, word) for word, i in counter.items()])
    for i, word in frequency:
        print(word)


if __name__ == '__main__':
    main()
