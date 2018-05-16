def print_info(setX):
    print(len(setX))
    print(*[str(i) for i in sorted(setX)])


def main():
    alice_set, bob_set = [int(i) for i in input().split()]
    alice_colors, bob_colors = set(), set()

    for i in range(alice_set):
        alice_colors.add(int(input()))
    for i in range(bob_set):
        bob_colors.add(int(input()))

    print_info(alice_colors & bob_colors)
    print_info(alice_colors - bob_colors)
    print_info(bob_colors - alice_colors)


if __name__ == '__main__':
    main()
