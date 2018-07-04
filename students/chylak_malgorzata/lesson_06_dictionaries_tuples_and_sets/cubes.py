def cube_set(set):
    print(len(set))
    for element in sorted(set):
        print(element)


alice_number, bob_number = [int(s) for s in input().split()]
alice_set = set()
bob_set = set()

for _ in range(alice_number):
    alice_set.add(int(input()))
for _ in range(bob_number):
    bob_set.add(int(input()))
cube_set(alice_set & bob_set)
cube_set(alice_set - bob_set)
cube_set(bob_set - alice_set)
