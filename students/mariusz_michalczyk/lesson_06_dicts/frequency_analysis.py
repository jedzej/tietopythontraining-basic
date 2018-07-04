def get_words(lines):
    list_of_words = []
    for line in range(lines):
        line_words = [s for s in input().split()]
        for word in line_words:
            list_of_words.append(word)
    return list_of_words


def get_freqs(list):
    freqs = []
    for word in list:
        counter = list.count(word)
        freq = (-counter, word)
        if freq not in freqs:
            freqs.append(freq)
    return freqs


if __name__ == '__main__':
    lines = int(input())
    list_of_words = get_words(lines)
    freqs = get_freqs(list_of_words)
    freqs.sort()
    for freq in freqs:
        print(freq[1])
