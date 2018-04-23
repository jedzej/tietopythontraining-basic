#!/usr/bin/env python3
"""Uppercase"""


def capitalize(lower_case_word):
    """Change the first letter to uppercase"""
    return lower_case_word[0].upper() + lower_case_word[1:]


def main():
    """Main function"""
    text = input().split()
    for word in text:
        print(capitalize(word), end=' ')


if __name__ == '__main__':
    main()
