
def frequency_analysis():

    n = int(input())
    counts = {}

    for _ in range(n):
        for word in input().split():
            counts[word] = counts.get(word, 0) + 1

    frequency = [(-count, word) for (word, count) in counts.items()]

    for i, word in sorted(frequency):
        print(word)


if __name__ == '__main__':
    frequency_analysis()
