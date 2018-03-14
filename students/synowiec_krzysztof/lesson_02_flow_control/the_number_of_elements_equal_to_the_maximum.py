def main():
    max = 0
    countOfMaxNumber = 0
    n = int(input())
    while n != 0:
        if n > max:
            max = n
            countOfMaxNumber = 1
        elif n == max:
            countOfMaxNumber += 1
        n = int(input())
    print(countOfMaxNumber)

if __name__ == '__main__':
    main()