if __name__ == '__main__':
    lines_count = int(input('Enter lines number: '))

    words_dict = {}
    print('Enter lines: ')
    for i in range(lines_count):
        for word in input().split():
            words_dict[word] = words_dict.get(word, 0) + 1

    sorted_items = sorted(words_dict.items(),
                          key=lambda item: (-item[1], item[0]))

    print()
    for k, v in sorted_items:
        print(k)
