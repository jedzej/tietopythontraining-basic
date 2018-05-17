
def guess_the_number():

    number_to_guess = int(input())
    all_numbers = set(range(1, number_to_guess + 1))
    possible_numbers = all_numbers

    while True:
        guess = input()
        if guess == 'HELP':
            break

        guess = {int(x) for x in guess.split()}
        answer = input()

        if answer == 'YES':
            possible_numbers &= guess
        else:
            possible_numbers &= all_numbers - guess

    numbers = ' '.join([str(x) for x in sorted(possible_numbers)])
    print(numbers)


if __name__ == '__main__':
    guess_the_number()
