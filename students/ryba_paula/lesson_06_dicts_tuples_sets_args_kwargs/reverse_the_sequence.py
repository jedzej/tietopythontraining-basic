def reverse_the_sequence():
    value = int(input())
    if value:
        reverse_the_sequence()
    print(value)


def main():
    reverse_the_sequence()


if __name__ == '__main__':
    main()
