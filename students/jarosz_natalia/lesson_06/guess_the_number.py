def guess_the_number():
    n = int(input())
    all_nums = set(range(1, n + 1))
    possible_nums = all_nums
    while True:
        guess = input()
        if guess == 'HELP':
            break
        guess = {int(x) for x in guess.split()}
        answer = input()
        if answer == 'YES':
            possible_nums &= guess
        else:
            possible_nums &= all_nums - guess

    print(' '.join([str(x) for x in sorted(possible_nums)]))


def main():
    guess_the_number()


if __name__ == '__main__':
    main()
