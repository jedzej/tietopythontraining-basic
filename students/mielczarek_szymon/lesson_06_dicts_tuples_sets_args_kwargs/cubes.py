def print_set(my_set):
    print(len(my_set), *sorted(my_set), sep='\n')


n, m = [int(i) for i in input().split()]
alice_set = set()
bob_set = set()
for _ in range(n):
    alice_set.add(int(input()))
for _ in range(m):
    bob_set.add(int(input()))

print_set(alice_set & bob_set)
print_set(alice_set - bob_set)
print_set(bob_set - alice_set)
