#!/usr/bin/env python3


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

    print(len(common_elements))
    for element in sorted(common_elements):
        print(element)

    print(len(alice_unique_elements))
    for element in sorted(alice_unique_elements):
        print(element)

    print(len(bob_unique_elements))
    for element in sorted(bob_unique_elements):
        print(element)


if __name__ == "__main__":
    main()