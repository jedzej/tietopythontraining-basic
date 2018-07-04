def input_value():
    n, m = [int(i) for i in input("Numbers: ").split(" ")]
    alice = set()
    bob = set()
    for i in range(n):
        alice.add(int(input("Alice set number: ")))
    for i in range(m):
        bob.add(int(input("Bob set number: ")))
    cube = [alice, bob]
    return cube


def print_result(new_set):
    print(len(new_set))
    for i in sorted(new_set):
        print(i)


cube = input_value()
in_both = cube[0].intersection(cube[1])
print_result(in_both)
only_alice = cube[0].difference(cube[1])
print_result(only_alice)
only_bob = cube[1].difference(cube[0])
print_result(only_bob)
