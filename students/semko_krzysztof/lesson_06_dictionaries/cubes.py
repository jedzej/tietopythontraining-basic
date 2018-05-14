"""
Alice and Bob like to play with colored cubes.
Each child has its own set of cubes and each cube has a
distinct color, but they want to know how many unique
colors exist if they combine their block sets. To determine
this, the kids enumerated each distinct color with a random
number from 0 to 108. At this point their enthusiasm
dried up, and you are invited to help them finish the task.

Given two integers that indicate the number of blocks
in Alice's and then Bob's sets N and M. The following
N lines contain the numerical color value for each
cube in Alice's set. Then the last M

rows contain the numerical color value
for each cube in Bob's set.

Find three sets: the numerical colors of cubes in both sets,
the numerical colors of cubes only in Alice's set, and the
numerical colors of cubes only in Bob's set. For each set,
print the number of elements in the set, followed by
the numerical color elements, sorted in ascending order.
"""


def print_set(example_set):
    print(len(example_set))
    for i in example_set:
        print(i)


def main():
    cubes = [int(cubes) for cubes in input().split()]
    alice_cubes = set()
    bob_cubes = set()
    for i in range(cubes[0]):
        alice_cubes.add(int(input()))
    for i in range(cubes[1]):
        bob_cubes.add(int(input()))

    intersection = alice_cubes & bob_cubes
    alice_only = alice_cubes - bob_cubes
    bob_only = bob_cubes - alice_cubes
    sorted(intersection)
    sorted(alice_only)
    sorted(bob_only)

    print_set(intersection)
    print_set(alice_only)
    print_set(bob_only)


if __name__ == '__main__':
    main()
