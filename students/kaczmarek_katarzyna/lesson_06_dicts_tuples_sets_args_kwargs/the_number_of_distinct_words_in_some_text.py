def main():
    words = set()
    for _ in range(int(input("Number of lines: "))):
        words.update(input("Type line of text: ").split())
    print("Number of distinct words: " + str(len(words)))


if __name__ == '__main__':
    main()
