def list_of_words(lines):
    wrds_array = []
    for line in range(lines):
        words = [s for s in input().split()]
        for word in words:
            wrds_array.append(word)
    return wrds_array


def get_freqs(list):
    freqs = []
    for word in list:
        counter = 0
        for i in range(len(list)):
            if word == list[i]:
                counter += 1
        freq = (-counter, word)
        if freq not in freqs:
            freqs.append(freq)
    return freqs


if __name__ == '__main__':
    lines = int(input())
    list = list_of_words(lines)
    freqs = get_freqs(list)
    freqs.sort()
    for freq in freqs:
        print(freq[1])
