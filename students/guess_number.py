n = int(input())

answer = ''
yes_set = set()
no_set = set()
guess_set = set()

numbers = set(range(1, n + 1))

while True:
    try:
        guess_set = {int(i) for i in input().split(' ')}
    except ValueError:
        print(' '.join(str(i) for i in (list(yes_set.difference(no_set)))))
        break

    answer = input()
    if answer == "YES":
        if len(yes_set) == 0:
            yes_set.update(guess_set)
        else:
            yes_set.intersection_update(guess_set)
    elif answer == "NO":
        no_set.update(guess_set)
        