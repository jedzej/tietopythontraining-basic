def main():
    print("Result:")
    lines = int(input())
    words = {}
    for i in range(lines):
        for word in input().split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    sorted_words = sorted([(-i, word) for word, i in words.items()])
    for i, word in sorted_words:
        print(word)


if __name__ == '__main__':
    main()
