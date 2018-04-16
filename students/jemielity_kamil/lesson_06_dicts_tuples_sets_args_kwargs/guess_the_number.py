
n = int(input('Number: '))
right_set = set(range(1, n + 1))
wrong_set = set()

while True:
    numbers = input('Set of numbers: ')
    if numbers != 'HELP':
        numbers = set(numbers.split())
        bob_answer = input('Bob answer: ')
        if bob_answer == 'YES':
            right_set.intersection_update(numbers)
        else:
            wrong_set.update(numbers)
    else:
        print(*(sorted(right_set.difference(wrong_set))))
        break
