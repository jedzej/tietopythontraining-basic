# Find three sets: the numerical colors of cubes in both sets, the numerical
#  colors of cubes only in Alice's set, and the numerical colors of cubes
# only in Bob's set. For each set, print the number of elements in the set,
# followed by the numerical color elements, sorted in ascending order.


def main():
    blocks_number_alice, blocks_number_bob = (
        int(a) for a in input('Enter Alice and Bob blocks: ').split())
    blocks_alice = []
    blocks_bob = []
    for i in range(blocks_number_alice):
        blocks_alice.append(int(input()))
    for j in range(blocks_number_bob):
        blocks_bob.append(int(input()))

    both_sets = set(blocks_alice) & set(blocks_bob)
    alice_only_set = set(blocks_alice) - set(blocks_bob)
    bob_only_set = set(blocks_bob) - set(blocks_alice)

    print("Both sets: " + str(len(both_sets)))
    print(both_sets)

    print("Alice only: " + str(len(alice_only_set)))
    print(alice_only_set)

    print("Bob only set: " + str(len(bob_only_set)))
    print(bob_only_set)


if __name__ == "__main__":
    main()
