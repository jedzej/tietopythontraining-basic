"""
Augustus and Beatrice play the following game.
Augustus thinks of a secret integer number from 1 to n.
Beatrice tries to guess the number by providing a set
of integers. Augustus answers YES if his secret number
exists in the provided set, or NO, if his number does not
exist in the provided numbers. Then after a few questions
Beatrice, totally confused, asks you to help her
determine Augustus's secret number.

Given the value of n in the first line, followed by the a
sequence Beatrice's guesses, series of numbers seperated by
spaces and Agustus's responses, or Beatrice's plea for HELP.
When Beatrice calls for help, provide a list of all the
remaining possible secret numbers, in ascending order,
separated by a space.
"""


def answer():
    reply = str(input())
    return reply == "YES"


def main():
    upper_range = int(input())
    number_range = set(range(1, upper_range + 1))
    result_set = number_range
    while True:
        line = input()
        if line == "HELP":
            break
        else:
            line_set = set(int(i) for i in list(line.split()))
            if answer():
                result_set &= line_set
            else:
                result_set -= line_set

    print(' '.join(str(i) for i in list(sorted(result_set))))


if __name__ == '__main__':
    main()
