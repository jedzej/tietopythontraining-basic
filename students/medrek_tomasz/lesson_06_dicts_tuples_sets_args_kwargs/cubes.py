#!/usr/bin/env python3


def print_results(data_set):
    print(len(data_set))
    for i in sorted(data_set):
        print(i)


def main():
    try:
        alice_cubes_no, bob_cubes_no = [int(s) for s in input(
            "Provide two numbers of cubes in childreen sets seperated with "
            "space.\n").split()]
        alice_set = set()
        bob_set = set()

        for i in range(int(alice_cubes_no)):
            alice_set.add(int(input("Enter integer number\n")))

        for i in range(int(bob_cubes_no)):
            bob_set.add(int(input("Enter integer number\n")))

    except ValueError:
        print("Something's wrong with your input, try again\n")
        exit()

    print_results(alice_set & bob_set)
    print_results(alice_set - bob_set)
    print_results(bob_set - alice_set)


if __name__ == "__main__":
    main()
