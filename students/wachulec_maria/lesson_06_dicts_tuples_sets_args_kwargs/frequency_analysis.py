def frequency_analysis():
    words_frequency = {}
    for i in range(int(input())):
        words = input().split()
        for j in words:
            words_frequency.setdefault(j, 0)
            words_frequency[j] += 1
    frequency_list = sorted(sorted(list(words_frequency.items()),
                            key=lambda elem: elem[0], reverse=False),
                            key=lambda elem: elem[1], reverse=True)
    print(' \n'.join([elem[0] for elem in frequency_list]))


frequency_analysis()
