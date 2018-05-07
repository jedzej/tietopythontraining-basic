n = int(input('Number: '))
possible_set = set(range(1, n + 1))

while True:
    numbers = input('Set of numbers: ')
    if numbers == 'HELP':
        break
    numbers = set(int(a) for a in numbers.split())
    bob_answer = input('Bob answer: ')
    if bob_answer == 'YES':
        possible_set.intersection_update(numbers)
    else:
        possible_set.difference_update(numbers)

print(" ".join(str(s) for s in sorted(possible_set)))
