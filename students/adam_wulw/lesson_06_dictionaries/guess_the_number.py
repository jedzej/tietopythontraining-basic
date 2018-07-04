secret_num_range = int(input())
secret_set = set(range(1, secret_num_range + 1))

question = input()
while question != "HELP":
    guess_list = map(int, question.split())
    guess_set = set()
    for guess in guess_list:
        guess_set.add(guess)
    answer = input()
    if answer == 'YES':
        secret_set.intersection_update(guess_set)
    if answer == 'NO':
        secret_set.difference_update(guess_set)
    question = input()

for num in secret_set:
    print(num, end=' ')
