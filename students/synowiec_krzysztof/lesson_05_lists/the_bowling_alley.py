def main():
    number_of_pins, bowls = [int(x) for x in input().split()]
    pins = [x for x in range(1, number_of_pins + 1)]

    overall_removed_pins = set()
    for x in range(0, bowls):
        first, last = [int(x) for x in input().split()]
        for x in range(first, last + 1):
            overall_removed_pins.add(x)

    for x in overall_removed_pins:
        pins.remove(x)

    for x in range(1, number_of_pins + 1):
        if x in pins:
            print("I", end="")
        else:
            print(".", end="")


if __name__ == '__main__':
    main()
