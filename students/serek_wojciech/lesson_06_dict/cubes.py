#!/usr/bin/env python3
"""Cubes exercise"""


def main():
    """Main function"""
    n_value, m_value = [int(j) for j in input().split()]
    alice = set()
    bob = set()
    for _ in range(n_value):
        alice.add(int(input()))
    for _ in range(m_value):
        bob.add(int(input()))

    both_sets = alice.intersection(bob)
    alice_only = alice.difference(bob)
    bob_only = bob.difference(alice)

    print(len(both_sets))
    print(*sorted(both_sets))
    print(len(alice_only))
    print(*sorted(alice_only))
    print(len(bob_only))
    print(*sorted(bob_only))


if __name__ == '__main__':
    main()
