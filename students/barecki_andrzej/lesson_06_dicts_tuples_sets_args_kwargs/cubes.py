def main():
    """"set number of elements in Alice and Bob sets"""
    n, m = [int(x) for x in input().split()]

    """"Create sets for Alice and Bob"""
    alice_set = create_set(n)
    bob_set = create_set(m)

    """"Print numerical colors of cubes in both sets"""
    print_set(alice_set.intersection(bob_set))

    """"Print numerical colors only in Alice set"""
    print_set(alice_set - bob_set)

    """"Print numerical colors only in Bob set"""
    print_set(bob_set - alice_set)


def create_set(size):
    cube_set = set([int(input()) for _ in range(size)])
    return cube_set


def print_set(cube_set):
    print(len(cube_set))
    for elem in sorted(cube_set):
        print(elem)


if __name__ == '__main__':
    main()
