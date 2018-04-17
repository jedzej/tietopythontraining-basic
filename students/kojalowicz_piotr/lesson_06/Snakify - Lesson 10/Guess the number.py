number_of_guess = int(input())
guess = set(input().split())
for i in range(number_of_guess):
    next_guess = set(input().split())
    steps = input()
    if steps == 'YES':
        guess = guess.intersection(next_guess)
    elif steps == 'NO':
        guess = guess.difference(next_guess)
    elif steps == 'HELP':
        print(guess)
        break
    else:
        print('Rong guess')