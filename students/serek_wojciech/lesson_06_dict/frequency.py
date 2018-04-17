#!/usr/bin/env python3
"""Frequency analysis exercise"""


def main():
    """Main function"""
    words = {}
    for _ in range(int(input())):
        line = input().split()
        for word in line:
            words[word] = words.get(word, 0) + 1

    words = sorted(words.items(), key=lambda x: (-x[1], x[0]))
    for item in words:
        print(item[0])


if __name__ == '__main__':
    main()
