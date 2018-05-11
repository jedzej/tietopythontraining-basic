'''
Statement
Augustus and Beatrice play the following game.
Augustus thinks of a secret integer number from 1 to n.
Beatrice tries to guess the number by providing a set of integers.
Augustus answers YES if his secret number exists in the provided set,
or NO, if his number does not exist in the provided numbers.
Then after a few questions Beatrice, totally confused,
asks you to help her determine Augustus's secret number.
Given the value of n in the first line,
followed by the a sequence Beatrice's guesses,
series of numbers seperated by spaces and Agustus's responses,
or Beatrice's plea for HELP. When Beatrice calls for help,
provide a list of all the remaining possible secret numbers,
in ascending order, separated by a space.
'''


def guess_the_number():
    max = int(input("Enter maximum secret number:"))
    secret_set = set(range(1, max + 1))
    print("Enter Beatrice guess set of number separated by space")
    beatrice_set = {int(s) for s in input().split()}
    print("Enter Augustus answear (YES/NO):")
    augustus_answear = str(input())
    while(beatrice_set != 'HELP'):
        if(augustus_answear == 'NO'):
            secret_set = secret_set - set(beatrice_set)
        else:
            secret_set = secret_set & set(beatrice_set)
        beatrice_set = input("Enter Beatrice guess set of number \
separated by space or HELP to end: ")
        if beatrice_set != 'HELP':
            beatrice_set = [int(s) for s in beatrice_set.split()]
            augustus_answear = str(input("Enter Augustus answear (YES/NO):"))
    secret_set = list(secret_set)
    secret_set.sort()
    print("Secret number set:")
    for i in range(len(secret_set)):
        print(secret_set[i], end=" ")


if __name__ == "__main__":
    guess_the_number()
