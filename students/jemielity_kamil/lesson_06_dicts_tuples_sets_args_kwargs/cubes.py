
n, m = [int(i) for i in input('Numbers: ').split()]
alice_set = set()
bob_set = set()
for i in range(n):
    alice_set.add(int(input('Alice set number: ')))

for i in range(m):
    bob_set.add(int(input('Bob set number: ')))


intersection = sorted(alice_set.intersection(bob_set))
print(len(intersection))
for i in intersection:
    print(i)

difference = sorted(alice_set.difference(bob_set))
print(len(difference))
for i in difference:
    print(i)

difference_update = sorted(bob_set.difference(alice_set))
print(len(difference_update))
for i in difference_update:
    print(i)
