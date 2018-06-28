def print_the_set(myset):
    for s in myset:
        print(s)


print("Enter the number of blocks in Alice's and Bob's sets:")
N, M = [int(i) for i in input().split()]
Alices_set = set()
Bobs_set = set()

print("Enter the number numerical colors in in Alice's set:")
for n in range(N):
    Alices_set.add(int(input()))

print("Enter the number numerical colors in in Bob's set:")
for m in range(M):
    Bobs_set.add(int(input()))

# The numerical colors of cubes in both sets
Both_set = Alices_set.intersection(Bobs_set)
print(len(Both_set))
print_the_set(Both_set)

# The numerical colors of cubes only in Alice's set
Alices_only_set = Alices_set.difference(Bobs_set)
print(len(Alices_only_set))
print_the_set(Alices_only_set)

# The numerical colors of cubes only in Bob's set
Bobs_only_set = Bobs_set.difference(Alices_set)
print(len(Bobs_only_set))
print_the_set(Bobs_only_set)
