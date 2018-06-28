def print_the_set(myset):
    for s in myset:
        print(s, end=" ")


guess_set = set()
n = int(input())
Possible_set = set(range(1, n+1))

while True:
    inp = input().split(" ")

    if inp[0] == 'HELP':
        print_the_set(Possible_set)

    else:
        Beatrices_set = set()

        for i in inp:
            Beatrices_set.add(int(i))

        answer = input()

        if answer == "YES":
            Possible_set.intersection_update(Beatrices_set)
        if answer == "NO":
            Possible_set.difference_update(Beatrices_set)
