def main():
    max = 0
    secondMax = 0
    n = int(input())
    while n != 0:
        if n > max:
            secondMax = max
            max = n
        elif n > secondMax:
            secondMax = n

        n = int(input())
    print(secondMax)


if __name__ == '__main__':
    main()