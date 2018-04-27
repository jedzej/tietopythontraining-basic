def main():
    n, m = [int(x) for x in input().split()]
    alice_set = prepare_cubes(n)
    bob_set = prepare_cubes(m)

    intersection_set = sorted(alice_set.intersection(bob_set))
    alice_only_set = sorted(alice_set.difference(bob_set))
    bob_only_set = sorted(bob_set.difference(alice_set))

    print_set(intersection_set)
    print_set(alice_only_set)
    print_set(bob_only_set)


def prepare_cubes(n):
    cubes = set()
    for x in range(n):
        cubes.add(int(input()))
    return cubes


def print_set(cubes):
    print(len(cubes))
    for x in cubes:
        print(x)


if __name__ == '__main__':
    main()
