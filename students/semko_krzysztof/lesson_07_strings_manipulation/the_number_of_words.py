"""
Given a string consisting of words separated by spaces.
Determine how many words it has. To solve the problem,
use the method count.
"""


def main():
    line = input()

    print(line.count(' ') + 1)


if __name__ == '__main__':
    main()
