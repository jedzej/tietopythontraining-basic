def get_words(n):
    words = set()
    for i in range(n):
        line = [s for s in input().split()]
        words.update(line)
    return words


if __name__ == '__main__':
    n = int(input())
    print(len(get_words(n)))
