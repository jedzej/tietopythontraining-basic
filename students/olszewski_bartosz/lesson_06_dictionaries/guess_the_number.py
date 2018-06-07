a_set = set(range(1, int(input()) + 1))
guess = input()
while guess != "HELP":
    b_set = set([int(x) for x in guess.split()])
    answer = input()
    if answer == "NO":
        a_set = a_set.difference(b_set)
    elif answer == "YES":
        a_set = a_set.intersection(b_set)
    guess = input()

for x in a_set:
    print(x, end=" ")
