# Write a function named collatz() that has one parameter named number.

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return (3 * number + 1)


def main():
    print('Provide number')
    number = int(input())
    while number != 1:
        number = collatz(number)

if __name__ == "__main__":
    main()