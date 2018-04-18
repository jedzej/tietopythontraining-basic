n = int(input())
possible_nums = nums = set(range(1, n + 1))
while True:
    beatrice_input = input()
    if beatrice_input == 'HELP':
        break
    beatrice_guess = set([int(i) for i in beatrice_input.split()])
    augustus_answer = input()
    if augustus_answer == 'YES':
        possible_nums &= beatrice_guess
    else:
        possible_nums &= nums - beatrice_guess

print(' '.join(str(s) for s in sorted(possible_nums)))
