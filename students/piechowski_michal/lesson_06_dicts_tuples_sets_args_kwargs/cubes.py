#!/usr/bin/env python3


def print_set(set_to_be_printed):
    print(len(set_to_be_printed))
    for element in sorted(set_to_be_printed):
        print(element)


def main():
    n, m = [int(x) for x in input().split()]
    alice_set = set()
    bob_set = set()

    for i in range(0, n):
        alice_set.add(int(input()))

    for i in range(0, m):
        bob_set.add(int(input()))

    common_elements = alice_set.intersection(bob_set)
    alice_unique_elements = alice_set.difference(bob_set)
    bob_unique_elements = bob_set.difference(alice_set)

    print_set(common_elements)
    print_set(alice_unique_elements)
    print_set(bob_unique_elements)


if __name__ == "__main__":
    main()
