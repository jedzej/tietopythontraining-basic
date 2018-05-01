def reverse():
    val = int(input('value: '))
    if val != 0:
        reverse()
    print(val)


def main():
    reverse()


if __name__ == "__main__":
    main()
