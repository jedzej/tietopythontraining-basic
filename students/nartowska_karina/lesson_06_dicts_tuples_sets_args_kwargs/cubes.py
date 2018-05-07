def cubes(number_of_blocks):
    cubes = set()
    for i in range(number_of_blocks):
        block = int(input())
        cubes.add(block)
    return cubes


def main():
    print("Result:")
    number_of_blocks_alice, number_of_blocks_bob \
        = [int(i) for i in input().split()]
    alice_cube = cubes(number_of_blocks_alice)
    bob_cube = cubes(number_of_blocks_bob)
    alice_bob = sorted(alice_cube.intersection(bob_cube))
    only_alice_cube = sorted(alice_cube.difference(bob_cube))
    only_bob_cube = sorted(bob_cube.difference(alice_cube))
    print(len(alice_bob))
    for i in alice_bob:
        print(i)
    print(len(only_alice_cube))
    for i in only_alice_cube:
        print(i)
    print(len(only_bob_cube))
    for i in only_bob_cube:
        print(i)


if __name__ == '__main__':
    main()
