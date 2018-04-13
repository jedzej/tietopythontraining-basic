#!/usr/bin/env python3


def main():
    n = int(input())
    words_set = set()

    for i in range(0, n):
        for word in input().split():
            words_set.add(word)

    print(len(words_set))


if __name__ == "__main__":
    main()