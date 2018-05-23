def print_cubes(a_set):
    print(len(a_set))
    for elem in sorted(a_set):
        print(elem)


print('Give the number of Alices and Bobs sets: ')
alice_num, bob_num = [int(s) for s in input().split()]
alice_set = set()
bob_set = set()
print('Give Alices sets: ')
for i in range(alice_num):
    alice_set.add(int(input()))
print('Give Bobs sets: ')
for i in range(bob_num):
    bob_set.add(int(input()))

print_cubes(alice_set & bob_set)
print_cubes(alice_set - bob_set)
print_cubes(bob_set - alice_set)
