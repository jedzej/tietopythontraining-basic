def main():
    number = int(input())
    set_of_ints = set(range(1, number + 1))
    possible_ints = set_of_ints

    while True:
        guess = input()
        if guess == 'HELP':
            break
        guess = {int(i) for i in guess.split()}
        answer = input()
        if answer == 'YES':
            possible_ints &= guess
        else:
            possible_ints &= set_of_ints - guess

    print(' '.join([str(i) for i in sorted(possible_ints)]))


if __name__ == '__main__':
    main()
