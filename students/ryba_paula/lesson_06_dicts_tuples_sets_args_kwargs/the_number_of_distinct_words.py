def main():
    distinct_words = set()
    for i in range(int(input())):
        distinct_words.update(input().split())
    print(len(distinct_words))


if __name__ == '__main__':
    main()
