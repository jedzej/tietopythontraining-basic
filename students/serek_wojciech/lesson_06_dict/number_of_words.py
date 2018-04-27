#!/usr/bin/env python3
"""The number of distinct words in some text exercise"""


def main():
    """Main function"""
    lines = int(input())
    words = set()
    for _ in range(lines):
        words.update(input().split())
    print(len(words))


if __name__ == '__main__':
    main()
