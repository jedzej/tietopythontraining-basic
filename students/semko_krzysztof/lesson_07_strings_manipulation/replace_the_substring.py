"""
Given a string. Replace in this string
all the numbers 1 by the word one.
"""


def main():
    x = 1
    line = input()
    line = line.replace(str(x), 'one')
    print(line)


if __name__ == '__main__':
    main()
