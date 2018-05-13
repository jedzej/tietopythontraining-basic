import os


def main():
    """"set range of secret number"""
    range_for_secret = int(input())

    """"Create total secret set"""
    total_secret_set = set([int(x) for x in range(1, range_for_secret + 1)])

    beatrice_guess = input()
    while True:
        if beatrice_guess == "HELP":
            break
        else:
            secret_set = set([int(x) for x in beatrice_guess.split(" ")])
            augustus_answer = input()

            if augustus_answer == "YES":
                """"Secret number exist in provided set"""
                total_secret_set = total_secret_set.intersection(secret_set)
            elif augustus_answer == "NO":
                """"Secret number does not exist in provided set"""
                total_secret_set = total_secret_set.difference(secret_set)
            else:
                raise NameError('Incorrect Augustus answer')
            beatrice_guess = input()

    """"Print HELP for Beatrice"""
    print_set(total_secret_set)


def print_set(set_of_elements):
    for elem in sorted(set_of_elements):
        print(elem, end=' ')
    print(os.linesep)


if __name__ == '__main__':
    main()
