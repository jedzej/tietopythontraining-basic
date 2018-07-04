n, m = [int(i) for i in input().split()]

alice = set()
bob = set()
for _ in range(n):
    alice.add(int(input()))
for _ in range(m):
    bob.add(int(input()))

print(len(alice & bob))
for elements in sorted(alice & bob):
    print(elements)

print(len(alice - bob))
for elements in sorted(alice - bob):
    print(elements)

print(len(bob - alice))
for elements in sorted(bob - alice):
    print(elements)
