def cubes_set(size):
    blocks = set()
    for i in range(size):
        blocks.add(int(input()))
    return blocks


def print_set(s):
    print(len(s))
    for i in sorted(s):
        print(i)


alice, bob = [int(i) for i in input().split(' ')]

alice_set = cubes_set(alice)
bob_set = cubes_set(bob)

print_set(alice_set.intersection(bob_set))
print_set(alice_set.difference(bob_set))
print_set(bob_set.difference(alice_set))

