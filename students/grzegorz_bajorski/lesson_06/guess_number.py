num_range = int(input())

numbers = wrong_numbers = set(range(1, num_range + 1))

while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = set([int(i) for i in guess.split()])
    answer = input()
    if answer == 'YES':
        numbers &= guess
    elif answer =='NO':
        numbers &= wrong_numbers - guess

print(' '.join(str(i) for i in sorted(numbers)))
