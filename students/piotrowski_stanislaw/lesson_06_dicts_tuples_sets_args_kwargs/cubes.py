# https://snakify.org/lessons/sets/problems/cubes/
# Cubes
# piotrsta


def output_cubes(cubes_set):
    print(len(cubes_set))
    for elem in sorted(cubes_set):
        print(elem)


if __name__ == "__main__":
    alice_num = int(input("Number of Alice's cubes: "))
    bob_num = int(input("Number of Bob's cubes: "))
    alice_set = set()
    bob_set = set()
    for i in range(alice_num):
        alice_set.add(int(input("Alice's cube number " + str(i + 1) + " has a color: ")))
    for i in range(bob_num):
        bob_set.add(int(input("Bob's cube number " + str(i + 1) + " has a color: ")))

    both_sets = alice_set.intersection(bob_set)
    alice_only = alice_set.difference(bob_set)
    bob_only = bob_set.difference(alice_set)

    print("Cubes in both sets")
    output_cubes(both_sets)
    print("Only Alice's cubes")
    output_cubes(alice_only)
    print("Only Bob's cubes")
    output_cubes(bob_only)

# TO DO
# Input Validation
