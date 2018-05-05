def prepare_cubes(n, owner):
    cubes = set()
    for x in range(n):
        cubes.add(int(input(owner + " - Numerical color of "
                            "cube #" + str(x+1) + ": ")))
    return cubes


def print_set(cubes):
    print(len(cubes))
    for x in cubes:
        print(x)


def main():
    n, m = [int(x) for x in input("Type two integers that indicate the number"
                                  " of blocks in Alice's and then Bob's sets "
                                  "(space separated): ").split()]
    alice_set = prepare_cubes(n, "Alice")
    bob_set = prepare_cubes(m, "Bob")

    intersection_set = sorted(alice_set.intersection(bob_set))
    alice_only_set = sorted(alice_set.difference(bob_set))
    bob_only_set = sorted(bob_set.difference(alice_set))

    print_set(intersection_set)
    print_set(alice_only_set)
    print_set(bob_only_set)


if __name__ == '__main__':
    main()
