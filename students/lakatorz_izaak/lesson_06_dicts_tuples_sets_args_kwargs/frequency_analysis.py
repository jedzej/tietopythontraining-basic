def get_key(item):
    return item[1]


def main():
    word_frequency = dict()
    line_number = int(input())

    for i in range(line_number):
        line = input().split(' ')
        for word in line:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    list_frequency = list(word_frequency.items())
    list_frequency = sorted(list_frequency, key=get_key)
    list_frequency.reverse()

    for i in list_frequency:
        print(i[0])


if __name__ == '__main__':
    main()
