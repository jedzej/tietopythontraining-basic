#!/usr/bin/env python3


def main():
    n = int(input())
    frequencies_dict = {}

    for i in range(0, n):
        for word in input().split():
            frequencies_dict.setdefault(word, 0)
            frequencies_dict[word] += 1

    frequencies_list = list([-frequency, word]
                            for word, frequency in frequencies_dict.items())

    for frequency, word in sorted(frequencies_list):
        print(word)


if __name__ == "__main__":
    main()
