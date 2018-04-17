def print_set_of_cubs(set_of_cubs):
    print(len(set_of_cubs))
    for element in sorted(set_of_cubs):
        print(element)


elements_of_set = input().split()
elements_of_alice_set = int(elements_of_set[0])
elements_of_bob_set = int(elements_of_set[1])


alice_set = set()
bob_set = set()

for i in range(elements_of_alice_set):
    alice_set.add(int(input()))
for i in range(elements_of_bob_set):
    bob_set.add(int(input()))

print_set_of_cubs(alice_set & bob_set)
print_set_of_cubs(alice_set - bob_set)
print_set_of_cubs(bob_set - alice_set)
