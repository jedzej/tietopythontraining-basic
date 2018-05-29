def print_set(a_set):
    print(len(a_set))
    for elem in sorted(a_set):
        print(elem)


alice_number, bob_number = [int(s) for s in input().split()]
alice_set = set()
bob_set = set()

for _ in range(alice_number):
    alice_set.add(int(input()))
for _ in range(bob_number):
    bob_set.add(int(input()))
print_set(alice_set & bob_set)
print_set(alice_set - bob_set)
print_set(bob_set - alice_set)
