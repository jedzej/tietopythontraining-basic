if __name__ == '__main__':
    number_of_lines = int(input('Enter number of lines: '))

    words = set()
    for i in range(number_of_lines):
        words |= set(input().split())

    print('Number of distinct words: {0}'.format(len(words)))
