A_set = set(range(1, int(input()) + 1))
guess = input()
while guess != "HELP":
    B_set = set([int(x) for x in guess.split()])
    answer = input()
    if answer == "NO":
        A_set = A_set.difference(B_set)
    elif answer == "YES":
        A_set = A_set.intersection(B_set)
    guess = input()

for x in A_set:
    print(x, end=" ")
