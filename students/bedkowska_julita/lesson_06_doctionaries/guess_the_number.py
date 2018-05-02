scope = int(input('Give the range: '))
possible_numbers = set(range(1, scope + 1))
while True:
    Beatrice_guess = input('Give numbers or ask for HELP: ')
    if Beatrice_guess != 'HELP':
        guess_set = set(int(s) for s in Beatrice_guess.split())
        answer = input('Is secret number in the set? ')
        if answer == 'YES':
            possible_numbers &= guess_set
        if answer == 'NO':
            possible_numbers -= guess_set
    else:
        break
print('Possible numbers:')
print(' '.join([str(x) for x in sorted(possible_numbers)]))
