# Add try and except statements to the previous project//
# to detect whether the user types in a noninteger string.


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return (3 * number + 1)


def main():
    print('Provide number')
    try:
        number = int(input())
        while number != 1:
            number = collatz(number)
    except ValueError:
        print('Number did not enter')


if __name__ == "__main__":
    main()
