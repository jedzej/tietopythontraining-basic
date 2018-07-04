def frequency():
    n = int(input())
    counts = {}
    for _ in range(n):
        for word in input().split():
            counts[word] = counts.get(word, 0) + 1

    freqs = [(-count, word) for (word, count) in counts.items()]
    for c, word in sorted(freqs):
        print(word)


def main():
    frequency()


if __name__ == '__main__':
    main()
