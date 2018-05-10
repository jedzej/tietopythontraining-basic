'''
Statement
Alice and Bob like to play with colored cubes.
Each child has its own set of cubes and each cube has a distinct color,
but they want to know how many unique colors exist if they combine
their block sets. To determine this, the kids enumerated each distinct
color with a random number from 0 to 108. At this point their
enthusiasm dried up, and you are invited to help them finish the task.
Given two integers that indicate the number of blocks in Alice's and
then Bob's sets N and M. The following N lines contain the numerical
color value for each cube in Alice's set. Then the last M rows
contain the numberical color value for each cube in Bob's set.

Find three sets: the numerical colors of cubes in both sets,
the numerical colors of cubes only in Alice's set,
and the numerical colors of cubes only in Bob's set.
For each set, print the number of elements in the set,
followed by the numerical color elements, sorted in ascending order.

'''


def display(list):
    print("Set size:")
    list.sort()
    print(len(list))
    print("Set elements:")
    for i in list:
        print(i)


if __name__ == "__main__":
    n, m = [int(i) for i in input(
        "Enter size of Alice and Bob sets (separated by space):").split()]
    alice = set()
    bob = set()
    print("Enter Alice set elements:")
    for i in range(n):
        alice.add(int(input()))
    print("Enter Bob set elements:")
    for j in range(m):
        bob.add(int(input()))
    print("Alice & Bob")
    display(list(alice & bob))
    print("Alice - Bob")
    display(list(alice - bob))
    print("Bob - Alice")
    display(list(bob - alice))
