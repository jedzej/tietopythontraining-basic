"""
Given a string consisting of exactly two words separated
by a space. Print a new string with the first and second
word positions swapped (the second word is printed first).

This task should not use loops and if.
"""


def main():
    line = input()
    line = line[line.find(' ') + 1:] + ' ' + line[:line.find(' ')]
    print(line)


if __name__ == '__main__':
    main()
