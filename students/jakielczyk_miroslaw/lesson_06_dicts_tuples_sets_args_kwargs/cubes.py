entry = input().split(' ')
n = int(entry[0])
m = int(entry[1])
alice_set = set()
bob_set = set()
for alice_cub in range(n):
    alice_set.add(int(input()))
for bob_cub in range(m):
    bob_set.add(int(input()))
both_set = alice_set.intersection(bob_set)
alice_set, bob_set = \
    alice_set.difference(bob_set), bob_set.difference(alice_set)
print(len(both_set))
if len(both_set) != 0:
    [print(str(cub)) for cub in sorted(both_set)]
else:
    print('')
print(len(alice_set))
if len(alice_set) != 0:
    [print(str(cub)) for cub in sorted(alice_set)]
else:
    print('')
print(len(bob_set))
if len(bob_set) != 0:
    [print(str(cub)) for cub in sorted(bob_set)]
else:
    print('')
