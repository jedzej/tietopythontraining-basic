def reverse_the_sequence():
    value = int(input())
    if value != 0:
        reverse_the_sequence()
    print(value)


def main():
    print("Result:")
    reverse_the_sequence()


if __name__ == '__main__':
    main()
