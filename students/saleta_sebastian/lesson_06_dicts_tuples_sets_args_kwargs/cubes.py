def print_set(cubes_set):
    print(len(cubes_set))
    print(*[str(item) for item in sorted(cubes_set)])


def cubes():
    alice_cube, bob_cube = [int(s) for s in input().split()]
    alice_colors_set = {int(input()) for s in range(alice_cube)}
    bob_colors_set = {int(input()) for s in range(bob_cube)}

    intersection = alice_colors_set & bob_colors_set
    only_alice = alice_colors_set - bob_colors_set
    only_bob = bob_colors_set - alice_colors_set
    print_set(intersection)
    print_set(only_alice)
    print_set(only_bob)


def main():
    cubes()


if __name__ == '__main__':
    main()
